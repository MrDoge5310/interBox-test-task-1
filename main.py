from prettytable import PrettyTable  # в більш масштабних проєктах можна було б використати pandas
import requests


class DataManager:
    def __init__(self):
        self.__base_link = "https://restcountries.com/v3.1"
        self.__data = None
        self.__th = ['№', 'Name', 'Capital', 'Png flag link']  # створюємо стовпці таблиці
        self.__table = PrettyTable(self.__th)  # ініціалізація об'єкта таблиці

    def get_data(self, county_name):
        link = self.__base_link + f"/name/{county_name}"  # в документації цей endpoint мені здався найбільш зручним
        response = requests.get(link)

        if response.status_code == 404:
            self.__data = None
            print("Nothing found")
        else:
            self.__data = response.json()

    def print_data(self):
        if self.__data:
            for i, el in enumerate(self.__data, 1):
                el.setdefault('capital', 'Has no capital')  # Якщо країна не має столиці встановлюється відповідне значення

                # додаємо рядки до таблиці з необхідними значеннями
                self.__table.add_row([i, el['name']['common'], el['capital'], el['flags']['png']])
            print(self.__table)
        else:
            print("There's nothing to print")


dm = DataManager()
dm.get_data("u")  # тут можна зробити введення через input або будь-якими іншими методами
dm.print_data()
