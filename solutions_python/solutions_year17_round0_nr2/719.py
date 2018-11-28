def readint(): return int(raw_input())
def readarray(x): return map(x, raw_input().split())

def toInt(nums):
    y = []
    for x in nums:
        x = int(x)
        y.append(x)
    return y

cases = readint()
for case in range(cases):

    num = list(raw_input())
    for j in range(20):
        for i, digit in enumerate(num):
            if i != len(num)-1:
                cur = int(num[i])
                next = int(num[i+1])
                if cur > next:
                    num[i] = cur - 1
                    num[i+1:] = [9 for x in range(len(num[i+1:]))]

    #remove extra 0s
    while num[0] == 0:
        del num[0]

    print 'Case #%i:'%(case+1), "".join(str(x) for x in num)
