import pytest
from click.testing import CliRunner

from cli import (
    Hawaiian,
    Margherita,
    Pepperoni,
    PizzaMenu,
    bake,
    delivery,
    order,
    pickup,
)


@pytest.fixture(name="margherita")
def margherita_fixture():
    return Margherita()


@pytest.fixture(name="pepperoni")
def pepperoni_fixture():
    return Pepperoni()


@pytest.fixture(name="hawaiian")
def hawaiian_fixture():
    return Hawaiian()


def test_margherita_creation(margherita):
    assert margherita.name == "Margherita"
    assert margherita.size in ("L", "XL")
    assert margherita.ingredients == ["tomato sauce", "mozzarella", "tomatoes"]
    assert margherita.img == "🧀"


def test_pepperoni_creation(pepperoni):
    assert pepperoni.name == "Pepperoni"
    assert pepperoni.size in ("L", "XL")
    assert pepperoni.ingredients == ["tomato sauce", "mozzarella", "pepperoni"]
    assert pepperoni.img == "🍕"


def test_hawaiian_creation(hawaiian):
    assert hawaiian.name == "Hawaiian"
    assert hawaiian.size in ("L", "XL")
    assert hawaiian.ingredients == [
        "tomato sauce",
        "mozzarella",
        "chicken",
        "pineapple",
    ]
    assert hawaiian.img == "🍍"


def test_pizza_equality():
    margherita1 = Margherita()
    margherita2 = Margherita()
    pepperoni1 = Pepperoni()
    hawaiian1 = Hawaiian()
    hawaiian2 = Hawaiian("XL")

    assert margherita1 == margherita2
    assert margherita1 != pepperoni1
    assert hawaiian1 != hawaiian2


def test_bake():
    margherita = Margherita()
    bake(margherita)


def test_delivery():
    pizza_name = "Margherita"
    delivery(pizza_name)


def test_pickup():
    pizza_name = "Margherita"
    pickup(pizza_name)


def test_order_with_courier():
    pizza_name = "Margherita"
    size = "L"
    runner = CliRunner()
    result = runner.invoke(order, [pizza_name, size, "--courier"])
    assert result.exit_code == 0


def test_order_without_courier():
    pizza_name = "Margherita"
    size = "L"
    runner = CliRunner()
    result = runner.invoke(order, [pizza_name, size])
    assert result.exit_code == 0


def test_menu():
    menu = PizzaMenu.menu()
    assert "Margherita" in menu
    assert "Pepperoni" in menu
    assert "Hawaiian" in menu


def test_menu_contents():
    menu = PizzaMenu.menu()

    margherita = menu["Margherita"]
    assert margherita[0] == "🧀"
    assert margherita[1] == ("L", "XL")
    assert margherita[2] == ["tomato sauce", "mozzarella", "tomatoes"]

    pepperoni = menu["Pepperoni"]
    assert pepperoni[0] == "🍕"
    assert pepperoni[1] == ("L", "XL")
    assert pepperoni[2] == ["tomato sauce", "mozzarella", "pepperoni"]

    hawaiian = menu["Hawaiian"]
    assert hawaiian[0] == "🍍"
    assert hawaiian[1] == ("L", "XL")
    assert hawaiian[2] == [
        "tomato sauce",
        "mozzarella",
        "chicken",
        "pineapple",
    ]
