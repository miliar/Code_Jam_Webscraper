import sys

def digit(n):
    d = 0
    while n > 0:
        n /= 10
        d += 1
    return d

def is_recycled(snum, bnum):
    d = digit(bnum) - 1
    for x in range(d):
        mod = bnum % 10
        bnum = mod * (10 ** d) + bnum / 10
        if bnum == snum:
            return True
    return False

limit = int(sys.stdin.readline())

"""
for i in range(limit):
    lst = sys.stdin.readline().split(" ")
    A = int(lst[0])
    B = int(lst[1])

    count = 0
    for snum in range(A, B):
        for bnum in range(snum + 1, B + 1):
            if is_recycled(snum, bnum):
                #print snum, bnum
                count += 1
    
    print "Case #" + str(i + 1) + ": " + str(count)
"""

def get_recycle_pair(num, A, B):
    self_num = num
    lst = []
    for d in range(digit(num) - 1, digit(B)):
        for x in range(d):
            mod = num % 10
            num = mod * (10 ** d) + num / 10
            if (not num in lst) and (A <= num <= B) and (self_num != num):
                #print num
                lst.append(num)
    if len(lst) > 0:
        lst.append(self_num)
    return lst
                
for i in range(limit):
    lst = sys.stdin.readline().split(" ")
    A = int(lst[0])
    B = int(lst[1])
    
    count = 0
    check_lst = [True for j in range(A, B + 1)]
    for num in range(A, B + 1):
        if check_lst[num - A]:
            recycle_lst = get_recycle_pair(num, A, B)
            for j in recycle_lst:
                check_lst[j - A] = False
            length = len(recycle_lst)
            count += length * (length - 1) / 2
            
    print "Case #" + str(i + 1) + ": " + str(count)
    

    
