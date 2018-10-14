n = int(raw_input().strip())

def findNum(num):
    if num == 1:
        return 1
    while(num > 1):
        num_str = str(num)
        temp = "".join(sorted(num_str))
        if num_str == temp:
            return num
        num -= 1

for i in xrange(n):
    t = int(raw_input().strip())
    print "Case #{}: {}".format(i + 1, findNum(t))

# t = int(raw_input())
# mTable = {}
# for i in xrange(t):
#     n, m = [int(s) for s in raw_input().split(" ")]
#     print "Case #{}: {}".format(i + 1, calSquareNum(n, m))
