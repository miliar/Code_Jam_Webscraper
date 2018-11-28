def minusfinder(s, k):
    s = list(s)
    for i in range(len(s) - k + 1):
        if s[i] == "-":
            return i
    return -1


numberoflip = 0


def flip(s, k):
    global numberoflip
    numberoflip += 1
    s = list(s)
    j = minusfinder(s, k)
    i = minusfinder(s, k)
    while i < (k + j):
        if s[i] == "+":
            s[i] = "-"
        else:
            s[i] == "-"
            s[i] = "+"
        i = i + 1  #:D
    return s


def checklastk(s, k):
    s = list(s)
    i = len(s) - k
    while i < (len(s)):
        if s[i] == "-":
            return "you dieded"
        i += 1
    return "YES There's a solution"


def pankek4Nazism(s, k):
    s = list(s)
    while minusfinder(s, k) != -1:
        s = (flip(s, k))
    if checklastk(s, k) == "you dieded":
        f.write("impossible\n")
    else:
        f.write(str(numberoflip) + "\n")

f = open('output.txt', 'w')
T = int(input())
for i in range(T):
    numberoflip = 0
    line = input()
    a = line.split(" ")
    a[1] = int(a[1])
    pankek4Nazism(a[0], a[1])