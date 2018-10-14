import sys

def is_palin(x):
    s = str(x)
    for i in range(len(s) / 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


all_nums = []

# for i in xrange(1, 10 ** 7 + 1):
#     if is_palin(i) and is_palin(i ** 2):
#         print i ** 2
#         all_nums.append(i ** 2)

# print all_nums
all_nums = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

T = int(sys.stdin.readline())
for ca in range(T):
    A, B = map(int, sys.stdin.readline().strip().split(' '))
    ret = 0
    for x in all_nums:
        if A <= x <= B:
            ret += 1
    print 'Case #%d: %d' % (ca + 1, ret)
