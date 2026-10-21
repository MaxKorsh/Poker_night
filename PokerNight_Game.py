
from random import shuffle
from time import sleep
from collections import Counter
SUITS = ['крести', 'бубны', 'червы', 'пики']
RANKS = ['2','3','4','5','6','7','8','9','10','Валет','Дама','Король','Туз']
RANK_INDEX = {r: i for i, r in enumerate(RANKS)}


# функция создания руки из 5 карт
def make_hand(deck):
    return [deck.pop() for _ in range(5)]


def print_hand(hand):
    print("|", end=' ')
    for card in hand:
        print(f"{card[1]} {SUITS[card[0]]}", end=" | ")
    print()


def make_deck():
    deck = [(s, r) for s in range(4) for r in RANKS]
    shuffle(deck)
    return deck


# Подсчёт комбинаций
def evaluate_hand(hand):
    # Проверка на флеши
    suit_ids = [c[0] for c in hand]
    values = sorted(RANK_INDEX[c[1]] for c in hand)

    # колесо A-2-3-4-5: туз считаем младшим
    if values == [0, 1, 2, 3, 12]:
        values = [-1, 0, 1, 2, 3]
    is_flush = len(set(suit_ids)) == 1
    is_straight = values == list(range(values[0], values[0] + 5))
    if is_flush and is_straight and values[0] == RANK_INDEX['10']:
        return (8,)  # Роял-флеш 8
    if is_flush and is_straight:
        return (7, values[0])  # Стрит-флеш 7
    if is_flush:
        return (4, *values[::-1])  # Флеш 4
    if is_straight:
        return (3, values[0])  # Стрит 3


    # проверка на повторы
    counts = Counter(values)
    groups = sorted(counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    group_counts = [g[1] for g in groups]
    group_values = [g[0] for g in groups]

    if group_counts == [4, 1]:
        return (6, group_values[0], group_values[1])  # Каре 6
    if group_counts == [3, 2]:
        return (5, group_values[0], group_values[1])  # Фулл хаус 5
    if group_counts == [3, 1, 1]:
        return (2, group_values[0], *sorted(group_values[1:], reverse=True))  # Сет 2
    if group_counts == [2, 2, 1]:
        return (1, group_values[0], group_values[1], group_values[2])  # Две пары 1
    if group_counts == [2, 1, 1, 1]:
        return (0, group_values[0], *sorted(group_values[1:], reverse=True))  # Пара 0 
    return (-1, *values[::-1])  # старшая карта -1


def rank_name(score):
    names = {
        8: "Роял-флеш",
        7: "Стрит-флеш",
        6: "Каре",
        5: "Фулл хаус",
        4: "Флеш",
        3: "Стрит",
        2: "Сет",
        1: "Две пары",
        0: "Пара",
        -1: "Старшая карта"
    }
    return names[score[0]]


def game():
    min_deck = 10
    deck = make_deck()
    while True:
        if len(deck) < min_deck:
            print("Колода закончилась - тасуем заново")
            sleep(2)
            deck = make_deck()
            print("Готово!")
        # Создать 5 карт в руку игрока
        player_hand = make_hand(deck)
        # Создать 5 карт в руку противника
        enemy_hand = make_hand(deck)

        sleep(1)
        print()
        print("Рука игрока:")
        print_hand(player_hand)
        sleep(1)
        print("Рука противника:")
        print_hand(enemy_hand)
        sleep(1)

        player_score = evaluate_hand(player_hand)
        enemy_score = evaluate_hand(enemy_hand)

        print("Игрок:", rank_name(player_score))
        print("Враг:", rank_name(enemy_score))
        if player_score > enemy_score:
            print("Победил игрок!")
        elif player_score < enemy_score:
            print("Победил враг!")
        else:
            print("Ничья!")


        rematch = input("Сыграем ещё раз?\n1. Да\n2. Нет, меню\n> ")
        if rematch != "1":
            return


def main():
    print("Добро пожаловать в За стол!")
    choice()

         
def choice():
    while True:
        user_input = input("\nЧто хотите?\n1.Сыграть\n2.Узнать правила\n3.Выйти\n\n")
        match user_input:
            case "1":
                game()
            case "2":
                print("Правила игры в покер:\n")
                print("1. Каждому игроку раздаётся по 5 карт.\n2. Побеждает игрок с самой сильной комбинацией карт.\n3. Комбинации карт оцениваются по стандартным правилам покера.\n")
            case "3":
                print("Выход из игры.")
                return
            case _:
                print("\nНекорректный ввод. Пожалуйста, выберите 1, 2 или 3.")


if __name__ == "__main__":
    main()