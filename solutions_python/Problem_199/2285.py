def lastDown(a):
    i = len(a) - 1
    while i >= 0:
        if a[i] == '-':
            return i
        i = i - 1
    return -1

def flip(a, k, i):
    j = i - k + 1
    while i >= j:
        if a[i] == '-':
            a[i] = '+'
        else:
            a[i] = '-'
        i = i-1

def checkEnd(a, k):
    if (len(a) < k):
        ce = checkEnd(a, len(a))
        if ce == 0:
            return 0
        else:
            return -1

    i = k-1
    cont = 0
    while i >=0:
        if a[i] == '+':
            cont = cont + 1
        i = i - 1

    if cont == k:
        return 0 # its done
    elif cont == 0:
        return 1 # flip one more and its done
    else:
        return -1 # its impossible

def jam(a, k):
    flips = 0
    last = lastDown(a)
    while (last >= k):
        flips = flips + 1
        flip(a, k, last)
        last = lastDown(a)
    end = checkEnd(a, k)
    if end == -1:
        return "IMPOSSIBLE"
    flips = flips + end
    return(flips)

cases = int(input())
for i in range(1, cases+1):
    entrada = input().split()
    arr = entrada[0]
    k = entrada[1]
    print("Case #" + str(i) + ": " + str(jam(list(arr), int(k))))
