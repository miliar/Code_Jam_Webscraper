fin2 = open('cansnew1.txt', 'r')
fin = open('C-large-2.in', 'r')
fout = open('numbersAnswer.txt', 'w')


def binary_searchSmaller(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    if a[mid+1] <= x:
        return mid+1
    elif a[mid] <= x:
        return mid
    else:
        return mid-1

def binary_searchBigger(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    if a[mid - 1 if mid > 0 else 0] > x:
        return mid-1
    elif a[mid] > x:
        return mid
    else:
        return mid+1    


T = fin.readline()
squares = fin2.readlines()
squares = map(int, squares)
for i in range(int(T)):
    A, B = map(int, fin.readline().split())
    a = binary_searchBigger(squares, A)
    b = binary_searchSmaller(squares, B)
    ans = b - a +1
    fout.write('Case #' + str(i+1) + ': ' + str(ans) + '\n')
fout.close()
fin2.close()
fin.close()
