def check_sort(n):
    n = str(n)
    first = int(n[0])
    for i in n:
        if first > int(i):
            return False
        first = int(i)
    return True

for i in xrange(int(input())):
    n = input()
    int_n = int(n)
    c = 0
    for j in xrange(int_n, 0, -1):
        if(check_sort(j)):
            print("Case #"+str(i+1)+": "+str(j))
            break
