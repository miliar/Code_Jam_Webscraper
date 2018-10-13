fair_and_square = [1, 4, 9]

def is_fair(n):
    s = str(n)
    head = s[:len(s) / 2]
    tail = s[(1 - len(s)) / 2:]
    return head == tail[::-1]

def prepare():
    i = 1
    while True:
        s = str(i)
        for j in xrange(1, 10):
            n = int((s + str(j) + s[::-1])) ** 2
            if is_fair(n):
                fair_and_square.append(n)
        n = int((s + s[::-1])) ** 2
        if is_fair(n):
            fair_and_square.append(n)
        if n >= 10 ** 14:
            break
        i += 1
    fair_and_square.sort()

def solve():
    A, B = map(int , raw_input().split())
    count = 0
    for i in fair_and_square:
        if A <= i <= B:
            count += 1
    return count

T = int(raw_input())
prepare()
for i in xrange(T):
    print "Case #%d:" % (i + 1), solve()
