#!/usr/bin/python

def solve(stalls, k):
    occupied = 0
    iteration = 0
    split = {stalls: 1}
    while occupied + 2**iteration < k:
        newSplit = {}
        for num, count in split.items():
            num -= 1
            nextNum = num / 2
            if nextNum not in newSplit:
                newSplit[nextNum] = 0
            if num % 2:
                if nextNum + 1 not in newSplit:
                    newSplit[nextNum + 1] = 0
                newSplit[nextNum] += count
                newSplit[nextNum + 1] += count
            else:
                newSplit[nextNum] += 2 * count
        split = newSplit
        occupied += 2 ** iteration
        iteration += 1
        #print stalls, k, split, occupied
    left = k - occupied
    for k in sorted(split.keys(), reverse=True):
        if left <= split[k]:
            k -= 1
            if k % 2:
                k /= 2
                return (k + 1, k)
            return (k / 2, k / 2)
        else:
            left -= split[k]



def main():
    t = int(raw_input())
    for i in xrange(t):
        n, k = map(int, raw_input().split(" "))
        mx, mn = solve(n, k)
        print "Case #{}: {} {}".format(i+1, mx, mn)

if __name__ == '__main__':
    main()
