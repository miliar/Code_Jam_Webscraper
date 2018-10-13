# def isTidy(num):
#     digits = list(reversed(map(int, str(num))))
#     for i in range(0, len(digits) -1):
#         if digits[i] >= digits[i+1]:
#             continue
#         return False
#     return True

# def ordered(number, prev, n):
#     if n == 0:
#         yield number
#         return

#     for i in range(prev + 1, 11-n ):
#         for x in ordered(number * 10 + i, i, n-1):
#             yield x

def ordered2(number, prev, n):
    #print(number, prev, n)
    if prev >= 9:
        return
    if n == 0:
        yield number
        return

    for i in range(prev + 1, 9 + n ):
        for x in ordered2(number * 10 + i, i -1 , n-1):
            yield x

def main():
    with open('B-small-attempt0.in.txt') as f:
        n = int(f.readline())
        for i in range(0, n):
            c = f.readline().rstrip()
            cLen = len(c)
            res = -1
            while res == -1:
                for x in ordered2(0,0, cLen):
                    #print(x)
                    if x <= int(c):
                        res = x
                cLen = cLen - 1
            print("Case #%s: %s" % (i +1 , res))

main()

#for x in ordered2(0,0,5):
   # print x
