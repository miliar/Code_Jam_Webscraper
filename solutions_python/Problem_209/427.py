from math import pi

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def area(stack):
    S_h = 0
    r = 0
    for pancake in stack:
        if pancake[1]>r:
            r = pancake[1]
        S_h += 2*pi*pancake[0]*pancake[1]
    return pi*r*r+S_h

def solve(pancakes,k):
    results = []
    for i in range(len(pancakes)):
        remainder = pancakes[:i] + pancakes[i+1:]
        stack = [pancakes[i]] + remainder[:k-1]
        results += [area(stack)]
    return max(results)

def compare(a,b):
    if a[0]*a[1] > b[0]*b[1]:
        return -1
    else:
        return 1

t = int(input())
for i in range(1,t+1):
    n, k  = [int(x) for x in input().split(" ")]
    pancakes = []
    for j in range(n):
        pancakes += [[int(x) for x in input().split(" ")][::-1]]
    pancakes.sort(key=cmp_to_key(compare))
    print("Case #" + str(i) + ": " + str(solve(pancakes,k)))
