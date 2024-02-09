import requests
import json


# CHOICEQR TOKEN EXTRACTOR
def extractToken(code):
    url = "https://open-api.choiceqr.com/auth/connect/token"
    headers = {"Content-type": "application/json"}

    client_id = "client_id"
    client_secret = "client_secret"

    # Prepare the request body
    data = {
        "code": code,
        "clientId": client_id,
        "secret": client_secret
    }

    # Make the POST request
    response = requests.post(url, json=data, headers=headers)

    # Print the response
    print(response.status_code)
    print(response.json())


class ChoiceQR_api:
    def __init__(self, startpoint, token):
        self.startpoint = startpoint
        self.token = token

    def getFullMenu(self):
        url = self.startpoint + '/menu/uk/full/list'
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Host": "open-api.choiceqr.com"
        }

        # Make the GET request
        response = requests.get(url, headers=headers)

        # Print the response
        print(response.status_code)
        print(json.dumps(response.json(), indent=4, ensure_ascii=False).encode('utf-8').decode())

        return response.json()

    def getMenuSections(self):
        url = self.startpoint + "/menu/uk/sections/list"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Host": "open-api.choiceqr.com"
        }

        # Make the GET request
        response = requests.get(url, headers=headers)

        return response.json()

    def getCategoriesFromSections(self, sectionId):
        url = self.startpoint + f"/menu/uk/categories/list/{sectionId}"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Host": "open-api.choiceqr.com"
        }

        # Make the GET request
        response = requests.get(url, headers=headers)

        return response.json()

    def getDishesFromCategory(self, categoryId):
        url = self.startpoint + f"/menu/uk/dishes/list/{categoryId}"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Host": "open-api.choiceqr.com"
        }

        # Make the GET request
        response = requests.get(url, headers=headers)

        return response.json()

    def getDishDetails(self, dishId):
        url = self.startpoint + f"/menu/uk/dishes/{dishId}"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Host": "open-api.choiceqr.com"
        }

        # Make the GET request
        response = requests.get(url, headers=headers)

        return response.json()
