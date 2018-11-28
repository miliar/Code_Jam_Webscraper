import sys
import os

case_win = "Case #%s: "

def make_work(input='input.txt', output='output.txt'):
    file_in = open(input)
    cases_number = int(file_in.readline().strip())
    for n in xrange(1, cases_number + 1):
        answer = get_answer(file_in)
        print((case_win % n) + str(answer))

def get_answer(file_in):
    """
        C = Farm cost
        F = Farm produce cookies
        X = Goal
    """
    cps = float(2)
    past_seconds = float(0)
    (C, F, X) = map(float, file_in.readline().strip().split())

    found_soultion = False

    while not found_soultion:
        nothing_secons = X / cps
        buy_farm_seconds = C / cps + X / (cps + F)
        if buy_farm_seconds < nothing_secons:
            past_seconds += C / cps
            cps += F
        else:
            past_seconds += nothing_secons 
            found_soultion = True

    return "%.7f" % past_seconds

if len(sys.argv) >= 2:
    make_work(input=sys.argv[1])
else:
    make_work()