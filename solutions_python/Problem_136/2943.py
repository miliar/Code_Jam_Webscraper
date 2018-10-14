#!/usr/bin/python3
from sys import argv

def process(C, F, X):
    old_wait_to_farm = 0
    if X > C or C <= X/2:
        per_second = 2
        old_wait_time = X / per_second
        while True:
            wait_to_farm = C / per_second + old_wait_to_farm
            per_second += F
            next_wait_time = X / per_second
            total_next_wait_time = wait_to_farm + next_wait_time
            if old_wait_time < total_next_wait_time:
                return old_wait_time
            old_wait_time = total_next_wait_time
            old_wait_to_farm = wait_to_farm
    else:
       return X / 2 


def main():
    with open(argv[1], "r") as f:
        T = int(f.readline())
        lines = f.readlines()

    for case_number in range(T):
        line = lines[case_number]

        C, F, X = line.split()
        wait_time = process(
            float(C),
            float(F),
            float(X)
            )
        
        print("Case #{0}: {1}".format(case_number+1, wait_time))

if __name__ == '__main__':
    main()