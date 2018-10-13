def all_happy(pancakes):
    all = True
    blank = '-'

    for pancake in pancakes:
        if pancake is blank:
            all = False

    return all

def flip(pancakes, size_flipper):
    pancakes = list(pancakes)
    blank = '-'
    happy = '+'
    flips = 0

    for pancake in range(len(pancakes)):
        if all_happy(pancakes):
            break
        if pancake+(size_flipper) > len(pancakes):
            return "IMPOSSIBLE"
        if pancakes[pancake] is blank:
            for p in range(size_flipper):
                if pancakes[pancake+p] is blank:
                    pancakes[pancake+p] = happy
                else:
                    pancakes[pancake+p] = blank
            flips += 1

    if all_happy(pancakes):
        return str(flips)

    return "IMPOSSIBLE"

test_cases = int(input())
output = ""

for t in range(test_cases):
    temp = input().split(" ")
    s = temp[0]
    k = int(temp[1])

    output += ("Case #"+str(t+1)+": "+flip(s, k))+"\n"

print(output)