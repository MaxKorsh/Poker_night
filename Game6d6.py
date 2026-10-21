import random
from collections import Counter
def Calculate(dice):
    # данная функция считает кол-во очков кубиков игрока
    counts = Counter(dice)
    total_score = 0
    for number,count in counts.items():
        # суммируем одинаковые числа и умножаем на их количество в квадрате
        total_score += number * (count ** 2)
    return total_score
def Game():
    while True:
        # Создаем проверку бул для возможности переиграть не выходя в основное меню
        has_winner = False
        print()
        # Игрок и робот кидают 6 шестигранников
        game_dice = [random.randint(1, 6) for _ in range(6)]
        print(f"кубики врага: {game_dice}")
        user_dice = [random.randint(1, 6) for _ in range(6)]
        print(f"твои кубики: {user_dice}")

        # Проверяем, на "стрит" - что кому-то выпали кубики от 1 до 6
        winning_row = {1, 2, 3, 4, 5, 6}
        game_has_row = set(game_dice) == winning_row
        user_has_row = set(user_dice) == winning_row
        # проверка победа по стриту
        if game_has_row and user_has_row:
            print("Вау! Ничья с двумя стритами! Следующий раунд!")
            print()
            continue
        elif game_has_row:
            print("Робот получил стрит! Победа робота!")
            print()
            has_winner = True
        elif user_has_row:
            print("Ты получил стрит! Победа твоя!")
            print()
            has_winner = True

        # если стрит не выпал, считаем по очкам
        game_score = Calculate(game_dice)
        print(f"Сумма очков робота: {game_score}")
        user_score = Calculate(user_dice)
        print(f"Твоя сумма очков: {user_score}")
        # проверка победы по очкам
        if game_score > user_score:
            print("Победил робот!")
            has_winner = True
        elif user_score > game_score:
            print("Вы победили!")
            has_winner = True
        else:
            print("Ничья! Следующий раунд!")
        print()
        if has_winner:
            rematch=input("Сыграем ещё раз?\n1.Да\n2.Нет, меню\n> ")
            match rematch:
                case "1":
                    continue
                case _:
                    return

    

def Choice():


    #основное меню
    while True:
        user_input=input("\nВведите номер требуемой задачи \n1. Правила игры\n2. Играть в игру\n3. Закончить работу\n> ")
        match user_input:
            case "1":
                print("\n- Одинаковые числа суммируются и умножаются на их количество\n- Выпадение ряда чисел от 1 до 6 означает автоматический выигрыш.\n")
            case "2":
                Game()
            case "3":
                print("Завершение работы.")
                exit()
print("Добро пожаловать в игру!")
Choice()