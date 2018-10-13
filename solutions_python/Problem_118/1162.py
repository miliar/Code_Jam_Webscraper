from math import sqrt
from itertools import combinations_with_replacement

def gen_new_fair(seed):
    length = len(seed)
    if length % 2:
        blank = (length - 1)/2
        new = list(seed[:blank+1])
    else :
        blank = length/2
        new = list(seed[:blank])

    n = 1
    while True:
        gened = combinations_with_replacement(range(blank), n)
        while True:
            copy = list(new)
            try:
                comb = gened.next()
            except:
                n += 1
                break
            else:
                for con in comb:
                    copy[con] += "0"
                copy = list("".join(copy))
                if len(copy)%1:
                    copycopy = list(copy)
                    copycopy.reverse()
                    copy = copy[:-1] + copycopy
                else:
                    copycopy = list(copy)
                    copycopy.reverse()
                    copy = copy + copycopy
                yield "".join(copy)

def search(a,b):
    count = 0
    if a <= 1 <= b:
        count += 1
    if a <= 2 <= b:
        count += 1
    if a <= 3 <= b:
        count += 1

    search_for = ["11","22","101","111","121","202","212","1111","11011", "11111", "11211", "111111", "1110111", "1111111","11111111","111101111", "111111111"]
    for i in search_for:
        gened = gen_new_fair(i)
        p = i
        while a <= int(p) <= b:
            count += 1
            p = gened.next()
    return count

def main():
    t = int(raw_input())

    for x in range(t):
        a,b = [int(i) for i in raw_input().split(" ")]
        a = sqrt(a)
        b = sqrt(b)
        print "Case #%d: %d" % (x+1,search(a,b))

main()
