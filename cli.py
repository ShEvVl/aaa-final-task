import random
import time
from typing import Dict, List, Tuple

import click


class Pizza:
    """Класс пицца.
    Имеет три функции:
        - инициализация параметров (__init__());
        - сравнение (__eq__());
        - запрос ингридиентов (get_ingredients()).
    """

    ingredients: List[str] = []
    img: str = ""

    def __init__(self, size: str = "L") -> None:
        if size not in ("L", "XL"):
            raise ValueError("Размер пиццы должен быть 'L' или 'XL'")
        self.name = self.__class__.__name__
        self.size = size
        self.ingredients = self.__class__.ingredients
        self.img = self.__class__.img

    def __eq__(self, other) -> bool:
        """Сравнивает два экземпляра класса:
            - по названию пиццы;
            - ингридиентам (отсортированные);
            - размеру пиццы.

        Args:
            other (class): другой экземпляр класса

        Returns:
            bool: True - если все равны, False - если хоть один нет
        """
        if isinstance(other, Pizza):
            return (
                self.name == other.name
                and sorted(self.ingredients) == sorted(other.ingredients)
                and self.size == other.size
            )
        return False

    def get_ingredients(self) -> Dict[str, List[str]]:
        """Функция запроса ингридиентов пиццы
        Returns:
            Dict[str, List[str]]: словарь, где ключ название пиццы,
            значение - список ингридиентов
        """
        return {self.name: self.ingredients}


class Margherita(Pizza):
    """Класс пиццы Маргарита.
    Состав: "tomato sauce", "mozzarella", "tomatoes"
    """

    ingredients = ["tomato sauce", "mozzarella", "tomatoes"]
    img = "🧀"


class Pepperoni(Pizza):
    """Класс пиццы Пепперони.
    Состав: "tomato sauce", "mozzarella", "pepperoni"
    """

    ingredients = ["tomato sauce", "mozzarella", "pepperoni"]
    img = "🍕"


class Hawaiian(Pizza):
    """Класс Гавайской пиццы.
    Состав: "tomato sauce", "mozzarella", "chicken", "pineapple"
    """

    ingredients = ["tomato sauce", "mozzarella", "chicken", "pineapple"]
    img = "🍍"


class PizzaMenu:
    """Класс меню пиццерии.
    Имеет одну функцию:
        - запрос меню пиццерии (menu()) декоратор @staticmethod
    """

    @staticmethod
    def menu() -> Dict[str, Tuple[str, Tuple[str, str], List[str]]]:
        """Меню пиццерии.

        Returns:
            Dict: название пиццы: (изображение, (варианты размеров), состав)
        """
        recipes = {
            "Margherita": (
                "🧀",
                ("L", "XL"),
                ["tomato sauce", "mozzarella", "tomatoes"],
            ),
            "Pepperoni": (
                "🍕",
                ("L", "XL"),
                ["tomato sauce", "mozzarella", "pepperoni"],
            ),
            "Hawaiian": (
                "🍍",
                ("L", "XL"),
                ["tomato sauce", "mozzarella", "chicken", "pineapple"],
            ),
        }
        return recipes


def log(message_template: str):
    """Функция-декоратор оболочки сообщения.

    Args:
        message_template (str): кастомный ввод сообщения
    """

    def decorator(func):
        """Декоратор

        Args:
            func (func): передача функции дальше
        """

        def wrapper(*args, **kwargs):
            """Обертка

            Returns:
                result: результат функции
            """
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            message = f"{message_template} {elapsed_time:.0f} c!"
            print(message)
            return result

        return wrapper

    return decorator


@log("🧑‍🍳 Приготовили за")
def bake(pizza_obj: Pizza):
    """Готовит пиццу"""
    name, ingredients = list(pizza_obj.get_ingredients().items())[0]
    time.sleep(random.randint(2, 5))
    print(f"Пицца {name!r} приготовлена\n Состав: {', '.join(ingredients)}")


@log("🛵 Доставили за")
def delivery(pizza: str):
    """Доставляет пиццу"""
    time.sleep(random.randint(2, 5))
    print(f"Пицца {pizza!r} доставлена")


@log("🏠 Забрали за")
def pickup(pizza: str):
    """Самовывоз"""
    time.sleep(random.randint(2, 5))
    print(f"Пиццу {pizza!r} забрали")


@click.group()
def cli():
    pass


@cli.command()
@click.option("--courier", default=False, is_flag=True)
@click.argument("pizza")
@click.argument("size")
def order(pizza: str, size: str, courier: bool):
    """Готовит и доставляет пиццу"""
    call = {
        "Margherita": Margherita(size),
        "Pepperoni": Pepperoni(size),
        "Hawaiian": Hawaiian(size),
    }
    pizza = pizza.capitalize()
    pizza_obj = call[pizza]

    if courier:
        print(
            f"Готовим и доставляем {pizza_obj.__class__.__name__!r} "
            f"размер {pizza_obj.size!r}"
        )
        bake(pizza_obj)
        delivery(pizza)
    else:
        print(
            f"Готовим на самовывоз {pizza_obj.__class__.__name__!r} "
            f"размер {pizza_obj.size!r}"
        )
        bake(pizza_obj)
        pickup(pizza)


@cli.command()
def menu():
    """Выводит меню"""
    for name, (img, size, ingredients) in PizzaMenu.menu().items():
        print(
            f"- {name} {img} size:({size[0]!r}/{size[1]!r}): "
            f"{', '.join(ingredients)}"
        )


if __name__ == "__main__":
    cli()
