
min = 9999999999999999

def flip(ch):
    if ch == '+':
        return '-'
    return '+'

def checkPancakes(pancakes):
    if (pancakes.count('-') == 0):
        return True
    return False

def flipRecursive(pancakes, index, k, count):
    i = 0
    global min
    if (checkPancakes(pancakes)):
        if count < min:
            min = count
            return
    pancakes = list(pancakes)
    while i < k:
        pancakes[index + i] = flip(pancakes[index + i])
        i += 1
    count += 1
    if (checkPancakes(pancakes)):
        if count < min:
            min = count
            return
    while index + k < len(pancakes):
        flipRecursive(list(pancakes[:]), index + 1, k, count)
        index += 1



t = input()
p = 1
while t:
    t -= 1
    min = 9999999999999999
    string, k = raw_input().split()
    k = int(k)
    string = list(string)
    i = 0
    while i + k <= len(string):
        flipRecursive(string[:], i, k, 0)
        i += 1
    if min == 9999999999999999:
        min = "IMPOSSIBLE"
    print "Case #" + str(p) + ": " + str(min)
    p += 1

