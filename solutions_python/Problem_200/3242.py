def lstToStr(lst):
    #return solve(int("".join(map(str, lst))))
    return int("".join(map(str, lst)))


#def solve(n):
#    lst = map(int, list(str(n)))
#    for i in range(len(lst)):
#        for j in range(i+1, len(lst)):
#            if lst[i] > lst[j]:
#                lst[i] -= 1
#                for k in range(i+1, len(lst)):
#                    lst[k] = 9
#                return lstToStr(lst)
#    return n
#

def maxLeft(lst, i):
    return max(lst[:i])

def maxRight(lst, i):
    return max(lst[i+1:])

def isTidy(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def solve(n):
    lst = map(int, list(str(n)))
    while True:
        if isTidy(lst):
            return lstToStr(lst)
        for i in range(len(lst)-1, 0, -1):
            if lst[i] > maxLeft(lst, i):
                lst [i] -= 1
                for k in range(i+1, len(lst)):
                    lst[k] = 9
                break
        else:
            lst[0] -= 1
            for k in range(1, len(lst)):
                lst[k] = 9


num_cases = input()
for case in range(1, num_cases+1):
    n = input()
    print "Case #%d: %d" % (case, solve(n))
