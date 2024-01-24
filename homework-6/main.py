from src.item import Item
from config import OPERATIONS_PATH, TEST_PATH, DAMAGE_PATH

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(OPERATIONS_PATH)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(OPERATIONS_PATH)
    # InstantiateCSVError: Файл item.csv поврежден
