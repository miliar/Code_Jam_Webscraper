import sys
sys.stdin = open('in')
sys.stdout = open('out', 'w')


for case in xrange(int(raw_input())):
    a, b, k = map(int, raw_input().strip().split())
    count = 0
    for i in xrange(a):
        for j in xrange(b):
            if i & j < k:
                count += 1
    print('Case #{}: {}'.format(case + 1, count))
