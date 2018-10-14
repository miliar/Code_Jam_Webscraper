import sys

T = int(sys.stdin.readline())

vowels = ['a', 'i', 'u', 'e', 'o']

def all_not_vowels(sub):
    for c in sub:
        if c in vowels:
            return False
    return True

def check_startpoints(word, n):
    points = []
    for i1 in xrange(len(word)):
        sub = word[i1:i1+n]
        if len(sub) == n and all_not_vowels(sub):
            points.append(i1)
    return points
        
def solver(word, n):
    points = check_startpoints(word, n)
    count = 0
    passed = list()
    for point in points:
        start, end = point, point + n
        queue = list()
        queue.append((start, end))
        while queue:
            item = queue.pop(0)
            if item in passed:
                pass
            else:
                passed.append(item)
                start, end = item
                count += 1
                if start - 1 >= 0:
                    queue.append((start - 1, end))
                if end + 1 <= len(word):
                    queue.append((start, end + 1))
    return count

for i in xrange(T):
    word, n = sys.stdin.readline().split()
    n = int(n)
    print "Case #{0:d}: {1:d}".format(i+1, solver(word, n))

