import sys
sys.setrecursionlimit(5000)

def do_it(pancakes, flipper_size):
    #print(pancakes, len(pancakes), flipper_size)

    if (len(pancakes) == 0): return 0
    if (pancakes[0] == "+"): return do_it(pancakes[1:], flipper_size)

    if (len(pancakes) < flipper_size): return -1
    else:
        for i in range(flipper_size): 
            if (pancakes[i] == "+"): pancakes[i] = "-"
            else: pancakes[i] = "+"

        recurse_answer = do_it(pancakes[1:], flipper_size)
        if (recurse_answer == -1): return -1
        else: return 1 + recurse_answer

cases = int(input(""))

for i in range(1, cases+1):
    (pancakes_str, flipper_size_str) = input("").split(" ")
    flipper_size = int(flipper_size_str)
    pancakes = list(pancakes_str)

    answer = do_it(pancakes, flipper_size)

    print("Case #%d: %s" % (i, "IMPOSSIBLE" if (answer == -1) else answer))