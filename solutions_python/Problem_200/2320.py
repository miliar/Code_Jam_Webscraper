t = int(input())
a = []

for i in range(0,t):
    s = input()
    l = list(s)
    a += [1]

    if(sorted(l) == l):
        a[i] = str(s)
    else:
        pos = 0
        for j in range(len(l)-1):
            if(l[j] < l[j+1]):
                pos = j+1
            elif(l[j] > l[j+1]):
                for k in range(len(l)-1, pos,-1):
                    l[k] = '9'
                x = int(l[pos]) - 1
                l[pos] = str(x)
                a[i] = "".join(l)
                break

for i in range(0,t):
    print("Case #" + str(i+1) + ": " + str(int(a[i])))
