import json

import choiceQR_api as api


class ChoiceQr_Menu(api.ChoiceQR_api):
    def __init__(self, startpoint, token):
        super().__init__(startpoint, token)
        self.sections = []

    def getMenuJSON(self):
        with open("choiceQR_models.json", "r", encoding='utf-8') as file:
            menu = json.load(file)

        return menu

        # return self.getFullMenu()

    def get_menu(self):
        for section in self.sections:
            print(section)
            section.get_categories()

    def init_sections(self):
        fullMenu = self.getMenuJSON()
        for section in fullMenu['sections']:
            menuSection = ChoiceQr_Section(section["_id"], section["name"], section["active"])
            for category in fullMenu['categories']:
                menuCategory = ChoiceQr_Category(category["_id"], category["name"], category["active"], category["section"])
                for dish in fullMenu['menu']:
                    menuDishCreator = ChoiceQr_DishCreator(
                        dishId=dish["_id"],
                        price=int(dish["price"]) / 100,
                        isActive=dish["active"],
                        name=dish["name"],
                        description=dish["description"],
                        media=dish["media"],
                        weight=dish["weight"],
                        menuLabels=dish["menuLabels"],
                        menuOptions=dish["menuOptions"],
                        categoryId=dish["category"]
                    )
                    menuDish = menuDishCreator.init_dishes()
                    if menuCategory.get_id() == menuDishCreator.get_category_id():
                        menuCategory.add_dish(menuDish)
                if menuCategory.get_section_id() == menuSection.get_id():
                    menuSection.add_category(menuCategory)

            self.sections.append(menuSection)


class ChoiceQr_Section:
    def __init__(self, sectionId, name, isActive):
        self.sectionId = sectionId
        self.name = name
        self.isActive = isActive
        self.categories = []

    def get_id(self):
        return self.sectionId

    def get_categories(self):
        for category in self.categories:
            print(category)
            category.get_dishes()

    def add_category(self, category):
        return self.categories.append(category)

    def __str__(self):
        return f'''Section: {self.sectionId} - {self.name}'''


class ChoiceQr_Category:
    def __init__(self, categoryId, name, isActive, sectionId):
        self.categoryId = categoryId
        self.name = name
        self.isActive = isActive
        self.sectionId = sectionId
        self.dishes = []

    def get_id(self):
        return self.categoryId

    def get_section_id(self):
        return self.sectionId

    def get_dishes(self):
        for dish in self.dishes:
            print(dish)

    def add_dish(self, dishes):
        for dish in dishes:
            self.dishes.append(dish)

    def __str__(self):
        return f'''>>> Category: {self.categoryId} - {self.name} '''


class ChoiceQr_DishCreator:
    def __init__(self, dishId, price, isActive, name, description, media, weight, menuLabels, menuOptions, categoryId):
        self.dishId = dishId
        self.price = price
        self.isActive = isActive
        self.name = name
        self.description = description
        self.media = media
        self.weight = weight
        self.menuLabels = menuLabels
        self.menuOptions = menuOptions
        self.categoryId = categoryId

    def get_category_id(self):
        return self.categoryId

    def init_dishes(self):
        output = []

        if self.menuLabels == []:
            ...
        else:
            self.name = f"⭐ {self.name}"

        self.media = self.media[0].get("url") if self.media is not None else None

        if self.menuOptions == []:
            output = [ChoiceQr_Dish(self.name, self.price, self.isActive, self.description, self.media, self.categoryId)]
        else:
            for optionList in self.menuOptions:
                for option in optionList["list"]:
                    name = self.name + ' ' + option["name"]
                    if option["price"] != 0:
                        price = int(option["price"]) / 100
                    else:
                        price = self.price
                    output.append(ChoiceQr_Dish(
                        name,
                        price,
                        self.isActive,
                        self.description,
                        self.media,
                        self.categoryId
                    ))

        return output


class ChoiceQr_Dish:
    def __init__(self, name, price, isActive, description, media, categoryId):
        self.price = price
        self.isActive = isActive
        self.name = name
        self.description = description
        self.media = media
        self.categoryId = categoryId

    def __str__(self):
        return f'''>>> >>> Dish: {self.name} {self.price}'''


if __name__ == '__main__':
    startpoint = 'https://test.choiceqr.com'
    token = 'token.token.token'

    partner = ChoiceQr_Menu(startpoint=startpoint, token=token)
    # print(json.dumps(menu := partner.getMenu(), indent=4, ensure_ascii=False).encode('utf-8').decode())

    partner.init_sections()
    partner.get_menu()
