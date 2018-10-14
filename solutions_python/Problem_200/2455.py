def NumbersSorted(n):
    lst = sorted(map(int, str(n)))
    ns = ''.join(str(e) for e in lst)
    return (n == int(ns))

def TidyNumbers(n):
    
    if(n < 10 or NumbersSorted(n)):
        return n

    while not NumbersSorted(n):
        lst = list(map(int, str(n)))
        mi = lst.index(max(lst), 0)

        if(mi+1 == len(lst)):
            lst[mi] = 0
        flag = False
        for i in range(mi + 1, len(lst)):
            if(lst[i] == 9):
                flag = True
            else:
                flag = False
                break
        if flag:
            mi = lst.index(max(lst[:mi]), 0)
        
        for i in range(mi + 1, len(lst)):
            lst[i] = 0
      
        n = int(''.join(str(e) for e in lst))

        if n % 10 == 0:
            n -= 1
        
        
    return n

T = int(input())
for t in range(1, T+ 1):
    n = int(input())
    print('Case #' + str(t) + ': ' + str(TidyNumbers(n)))
