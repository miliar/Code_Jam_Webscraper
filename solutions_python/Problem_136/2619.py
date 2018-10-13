# -*- coding: utf-8 -*-

import sys, decimal

def solve(c, f, x):
    """
    2/sek - bazowy zysk
    c - koszt farmy
    f - zysk dodatkowy z każdej farmy
    x - ile należy uzbierać
    wynik: czas przy idealnej strategii

    Obserwacja: jeżeli mam budować farmę, to powinienem to zrobić jak najszybciej
    się da, bo koszt i tak poniosę więc niech zarabia jak najwcześniej. Tak więc,
    pytaniem jest, ile farm zbudować. Albo, inaczej, ilekroć uzbieram na następną
    farmę, jest punkt decyzji czy ją robić, czy nie.
    """
    return solve_with_base(2.0, c, f, x)

def solve_with_base(b, c, f, x):
    """
    Jak wyżej, tylko b to ile już mam za darmo na sekundę

    b - ile już produkuję na sekundę
    c - koszt farmy
    f - zysk dodatkowy z każdej farmy
    x - ile należy uzbierać
    wynik: czas przy idealnej strategii
    """
    # Czas jeśli nie zbuduję farmy
    time_without_farm = x / b

    if x <= c:
        # Nie ma sensu budować farmy, taniej skończyć
        return time_without_farm

    best_time = time_without_farm
    time_spent = 0.0
    while True:
        # Budujemy kolejną farmę 
        time_spent += c/b
        b += f
        # Może już nie ma sensu
        if time_spent >= best_time:
            break
        # sprawdzamy koszt jeśli to będzie ostatnia z farm
        cost_here = time_spent + x / b
        if cost_here < best_time:
            best_time = cost_here
    return best_time


name, output_name = None, None
if len(sys.argv) > 1:
    name = sys.argv[1]
    if name.endswith(".in"):
        output_name = name.replace(".in", ".out")

if not (name and output_name):
    print "Uruchamianie: {0} plik.in".format(sys.argv[0])

with open(name, "r") as input:
    with open(output_name, "w") as output:
        test_cases_count = int(input.readline())
        for case_no in range(1, test_cases_count+1):
            c, f, x = [float(item) for item in input.readline().split()]
            solution = solve(c, f, x)
            reply = "Case #{0}: {1:0.7f}\n".format(case_no, solution)
            output.write(reply)
            print reply,

print "Wynik zapisany w {0}".format(output_name)
