import sys

# Pre calculation
# ---------------
fair = []

for i in range(1, 10000000):
    if str(i) != str(i)[::-1]: continue
    sq = i * i
    if str(sq) == str(sq)[::-1]:
        fair.append(sq)
        print sq, i

print len(fair)

# fair.append(9)
# for x in xrange(1, 10001):
#     i = 0
#     while x > 0:
#         i = i * 10 + x % 3
#         x /= 3
#
#     if str(i) != str(i)[::-1]: continue
#
#     sq = i * i
#     if str(sq) == str(sq)[::-1]:
#         if sq <= 10**14:
#             fair.append(sq)
#
# fair = sorted(list(set(fair)))
# for i in fair:
#     print i
#
# print len(fair)

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w+')
T = input()
for t_case in range(T):
    A, B = raw_input().split()
    A, B = int(A), int(B)
    ans = 0
    for f in fair:
        if A <= f <= B:
            ans += 1
    print "Case #%s: %s" % (t_case+1, ans)
