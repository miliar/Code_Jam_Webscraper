from itertools import combinations
import sys

def partition(lst):
    combs = []
    upper = None
    upper_lst = []
    lst = sorted(lst)
    for i in range(len(lst)-1):
        for j in combinations(lst, i+1):
            combs.append(list(j))
    for c in combs:
        diff = lst[:]
        for i in c:
            diff.remove(i)
        s1 = reduce(lambda x, y: x^y, c, 0)
        s2 = reduce(lambda x, y: x^y, diff,0)
        if s1 == s2:
            if sum(c) > upper:
                upper = sum(c)
                upper_lst = list(c)
            if sum(diff) > upper:
                upper = sum(diff)
                upper_lst = list(diff)
        if upper:
            return str(upper)
        else:
            return "NO"


if __name__ == "__main__":
    items = sys.stdin.read().split("\n")
    items = filter(lambda x: x, items)
    t = int(items[0])
    items = items[1:]
    for i in range(t):
        line = items[2*i].split()
        n = int(line[0])
        line = items[2*i+1].split()
        lst = []
        for j in range(n):
            lst.append(int(line[j]))
        
        print "Case #%d: %s" % (i+1, partition(lst))
