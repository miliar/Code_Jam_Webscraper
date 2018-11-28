import sys
import numpy as np

input_file = "B-large.in"
output_file = "B-large.out"

def solve(n):
    current_highest_nr = n[0]
    done = False
    if len(n) == 1:
        done = True
    while not done:
        for i in range(1, len(n)):
            current_highest_nr = np.max([current_highest_nr, n[i-1]])
            if n[i] < current_highest_nr:
                n[i-1] = n[i-1]-1
                for j in range(i, len(n)):
                    n[j] = 9
                current_highest_nr = n[0]
                break
            elif i == len(n)-1:
                done = True
    return int("".join([str(j) for j in n]))

def main():
    t = int(input())
    for i in range(1, t + 1):
        n = [int(j) for j in input()]
        print("Case #{}: {}".format(i, solve(n)))

if __name__ == "__main__":
    sys.stdin = open(input_file)
    sys.stdout = open(output_file, 'w+')
    main()