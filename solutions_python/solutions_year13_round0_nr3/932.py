# small and first large

def is_palindrome(num):
    a = str(num)
    return a == a[::-1]

all = set()

for front in xrange(1, 100000):
    rev = str(front)[::-1]
    for st in xrange(2):
        back = int(rev[st:] or 0)
        num = front * (10 ** (len(rev) - st)) + back
        
        if is_palindrome(num * num):
            all.add(num * num)

# for a in sorted(all):
#     b = str(int(a ** 0.5))
#     print a, int(a ** 0.5), '22' in b
# print 'max', max(all)
# print len(all)


t = int(raw_input())
for cc in xrange(t):
    a, b = map(int, raw_input().split())
    cnt = 0
    for c in all:
        if a <= c <= b:
            cnt += 1
    print 'Case #%d: %d' % (cc + 1, cnt)
    



