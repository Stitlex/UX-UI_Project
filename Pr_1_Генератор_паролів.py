import random
import string


def generate_password(complexity, length=None):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    if complexity in ["простий", "1"]:
        default_length = 8
        characters = letters + numbers
    elif complexity in ["середній", "2"]:
        default_length = 12
        characters = letters + numbers + symbols
    elif complexity in ["складний", "3"]:
        default_length = 16
        characters = letters + numbers + symbols
    else:
        return None

    length_range = length if length and isinstance(length, int) and length > 0 else default_length
    password = ''.join(random.choice(characters) for _ in range(length_range))
    return password


def submenu_password_generation():
    while True:
        print("\n--- Генератор паролів ---")
        print("1. Простий (8 символів: літери та цифри)")
        print("2. Середній (12 символів: літери, цифри, символи)")
        print("3. Складний (16 символів: літери, цифри, символи)")
        print("4. Повернутися в головне меню")
        print("0. Вихід з програми")

        user_choice = input("Виберіть рівень складності (1-3), або інший пункт: ").lower()

        if user_choice in ["0", "вихід", "вихід з програми"]:
            print("Програма завершена.")
            exit()

        if user_choice == "4":
            return

        valid_choices = ["1", "2", "3", "простий", "середній", "складний"]
        if user_choice not in valid_choices:
            print("Невірне значення! Спробуйте ще раз.")
            continue

        user_length_input = input("Введіть довжину пароля або натисніть Enter для стандартної довжини: ")
        try:
            user_length = int(user_length_input) if user_length_input else None
            if user_length is not None and user_length <= 0:
                print("Довжина повинна бути більше нуля. Використовується стандартна довжина.")
                user_length = None
        except ValueError:
            user_length = None
            print("Невірне значення довжини! Використовується стандартна довжина.")

        password = generate_password(user_choice, user_length)
        print("\nВаш згенерований пароль:", password)
        print(f"Довжина пароля: {len(password)} символів\n")


def submenu_theory():
    print("\n--- Теоретичний матеріал ---")
    print("Надійний пароль має бути довгим (12+ символів) і включати:\n"
          "- великі та малі літери\n"
          "- цифри\n"
          "- спеціальні символи (!, @, #, $, ...)\n"
          "Рівні складності в цій програмі:\n"
          "  Простий – мінімальний захист\n"
          "  Середній – рекомендований для більшості сайтів\n"
          "  Складний – для максимальної безпеки\n")
    input("Натисніть Enter, щоб повернутися в головне меню...")


def submenu_author():
    print("\n--- Про автора ---")
    print("Програму створив: Максим Юрковський\n"
          "Студент, спеціальність: IT (розробка ПЗ)\n")
    input("Натисніть Enter, щоб повернутися в головне меню...")


def main():
    while True:
        print("\n====== ГОЛОВНЕ МЕНЮ ======")
        print("1. Генерація пароля")
        print("2. Теоретичний матеріал")
        print("3. Про автора")
        print("0. Вихід з програми")

        choice = input("Ваш вибір (0–3): ")

        if choice == "1":
            submenu_password_generation()
        elif choice == "2":
            submenu_theory()
        elif choice == "3":
            submenu_author()
        elif choice == "0":
            print("Програма завершена.")
            exit()
        else:
            print("Невірний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
    main()