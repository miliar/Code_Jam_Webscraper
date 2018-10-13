
import sys
sys.setrecursionlimit(1500)

def pancake_reverse(pancakes):
    result = ""
    for pancake in pancakes:
        if pancake == '-':
            result += '+'
        elif pancake == '+':
            result += '-'
        else:
            raise Exception("Impossible!")
    return result

def solve(pancakes, flipper):
    if len(pancakes) == flipper:
        if pancakes == flipper * '+':
            return 0
        if pancakes == flipper * '-':
            return 1
        return "IMPOSSIBLE"
    if pancakes[0] == '-':
        rec = solve(pancake_reverse(pancakes[1:flipper]) + pancakes[flipper:], flipper)
        if rec == "IMPOSSIBLE":
            return "IMPOSSIBLE"
        return 1 + rec
    else:
        rec = solve(pancakes[1:], flipper)
        if rec == "IMPOSSIBLE":
            return "IMPOSSIBLE"
        return rec

def main():
    cases = int(input())
    for i in range(1, cases+1):
        pancakes, flipper = input().rstrip().split(" ")
        flipper = int(flipper)
        print("Case #%d: %s" % (i, solve(pancakes, flipper)))

if __name__ == '__main__':
    main()

        