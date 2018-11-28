import sys

T = int(sys.stdin.readline()[:-1])

for i in range(1, T+1):
    r = int(sys.stdin.readline()[:-1])
    for _ in range(r-1): sys.stdin.readline()
    s1 = set(map(int, sys.stdin.readline()[:-1].split()))
    for _ in range(r+1, 5): sys.stdin.readline()
    r = int(sys.stdin.readline()[:-1])
    for _ in range(r-1): sys.stdin.readline()
    s2 = set(map(int, sys.stdin.readline()[:-1].split()))
    for _ in range(r+1, 5): sys.stdin.readline()
    s = s1.intersection(s2)
    print 'Case #{}:'.format(i),
    if len(s) > 1:
        print 'Bad magician!'
    elif len(s) < 1:
        print 'Volunteer cheated!'
    else:
        print s.pop()
