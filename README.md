# Кодим 🍕.py

### Используя ООП необходимо: 
- описать рецепты классами;
- использовать два размера пиццы `L` и `XL`;
- использовать метод словарь для вывода рецепта пиццы;
- *использовать `__eq__()` для сравнения.

**бонусное действие*

| **Margherita** 🧀 | **Pepperoni** 🍕 | **Hawaiian** 🍍 |
| ---------------- | --------------- | -------------- |
| tomato sauce     | tomato sauce    | tomato sauce   |
| mozzarella       | mozzarella      | mozzarella     |
| tomatoes         | pepperoni       | chicken        |
|                  |                 | pineapple      |

### Используя библиотеку `click` написать две команды (функции):
- `order` - готовит пиццу, отправляет курьера (флаг `--delivery`)
- `menu` - выводит меню

Блюпринт `click` для команд:
```
import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) :
    """Готовит и доставляет пиццу"""

@cli.command()
def menu():
    """Выводит меню"""

if __name__ = '__main__':
    cli()
```

### Используя ФП написать:
- функцию `bake` *"Готовит пиццу"*
- функцию `delivery` *"Доставляет пиццу"*
- функцию `pickup` *"Самовывоз пиццы"*
- декоратор `@log`, который выводит имя
функции и время выполнения (`randint()`)
- *декоратор `@log` принимает шаблон, в который
подставляется время (`@log("🛵 Доставили за { }c!")`)

### *Бонусы:
- Тесты
- Докстринги
- Аннотации
- **pep**

### Ожидания
- Написание читаемого и понятного кода
- Тщательное покрытие кода тестами
- Свободное владение встроенными типами данных и знание их алгоритмических сложностей
- Разделение кода на функции, классы, модули
- Владением idea, git
- Понимание концепции декораторов
- Понимание основ функционального программирования


