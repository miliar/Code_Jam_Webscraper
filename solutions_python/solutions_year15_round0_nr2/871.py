import sys

# sys.setrecursionlimit(1500)

def memoize(function):
    table = {}
    def new(arg):
        if tuple(arg) in table:
            return table[tuple(arg)]
        else:
            n = function(arg)
            table[tuple(arg)] = n
            return n
    return new

def optimise_old(plates):
    # print(plates)
    if all(p in {0, 1} for p in plates):
        return 1
    else:
        options = []
        option = [p-1 if p > 0 else 0 for p in plates]
        options.append(option)
        # for i in range(len(plates)):
        #     new_plates = plates[:]
        #     if new_plates[i] > 1:
        #         item = new_plates.pop(i)
        #         for p in range(1, item):
        #             options.append(new_plates + [p, item - p])
        new_plates = sorted(plates)
        tallest = new_plates.pop()
        for p in range(1, tallest):
            options.append(new_plates + [p, tallest - p])
        for i in range(len(options)):
            option = options[i]
            option = [o for o in option if o != 0]
            options[i] = option
        return min(1 + optimise(o) for o in options)
    
optimise = memoize(optimise_old)

if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        input()
        plates = list(map(int, input().split()))
        answer = optimise(plates)
        print("Case #{}: {}".format(i + 1, answer))
        