#!/usr/bin/env python3

def solution(l):
    current_nb = l[0]
    friends = 0

    for shyness, nb_persons in enumerate(l[1:], start=1):
        if current_nb < shyness and nb_persons > 0:
            friends += (shyness - current_nb)
            current_nb += friends
        current_nb += nb_persons
    return friends

def generate_arguments(input_str):
    str_max, l = input_str.split()
    str_max = int(str_max)
    ret_l = [int(c) for c in l]

    return str_max, ret_l

def main():
    nb_test = int(input())

    for i in range(nb_test):
        input_str = input()
        str_max, l = generate_arguments(input_str)
        sol = solution(l)
        print("Case #{}: {}".format(i + 1, sol))

main()
