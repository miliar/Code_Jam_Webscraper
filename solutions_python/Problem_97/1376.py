# from sets import Set

# allset = Set([])

def rotations(n, a, b):
    nums = []
    total = 0
    s = str(n)
    l = len(s)
    for i in xrange(l):
        r = int(s[i:l] + s[0:i], 10)
        if n < r <= b and r not in nums:
            # allset.add(Set([n, r]))
            nums.append(r)
            total += 1
    return total

def count(a, b):
    # allset.clear()
    total = 0
    for i in xrange(a, b):
        total += rotations(i, a, b)
    # return len(allset), total
    return total

def main():
    cases = int(raw_input())
    for i in xrange(1, cases+1):
        n = [int(x) for x in raw_input().split(' ')]
        print 'Case #%s: %s' % (i, count(n[0], n[1]))

main()
