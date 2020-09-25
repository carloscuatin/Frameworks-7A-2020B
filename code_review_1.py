# script: Number race
from os import system
from random import randint

# functions


def generate_dice():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    total = d1 + d2

    return [d1, d2, total]


def generate_launches_number(n):
    i = 1
    sum_total = 0

    while i <= n:
        dices = generate_dice()
        sum_total = sum_total + dices[2]

        print('d1: ', dices[0])
        print('d2: ', dices[1])
        print('Total: ', dices[2])

        if dices[2] == 12:
            break

        i += 1

        if i <= n:
            key = input('::: Lanzar nuevamente :::')

    return sum_total


def get_even_odd(sum):
    i = 1
    even = 0
    odd = 0

    while i <= sum:
        if (i % 2) == 0:
            even += 1
        else:
            odd += 1

        i += 1

    return [even, odd]


def main():
    num_times = int(input('::: Ingrese el número de veces a lanzar :::'))

    if num_times > 0:
        total = generate_launches_number(num_times)
        num_even_odd = get_even_odd(total)

        print('\n')
        print('Acumulación de lanzamientos:', total)
        print('Pares:', num_even_odd[0])
        print('Impares:', num_even_odd[1])
    else:
        print('El número debe ser mayor a 0')
        main()


# main
system('clear')
main()
