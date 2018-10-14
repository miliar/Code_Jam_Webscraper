f = open("A-large.in",'r')
out = open("out.txt",'w')
        
def func(n, L):
    min1 = 0
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            min1 += L[i]-L[i+1]

    min2 = 0
    min_pace = 0
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            if min_pace < L[i]-L[i+1]:
                min_pace = L[i]-L[i+1]
    print min_pace
    for i in range(len(L)-1):
        min2 += min_pace
        if L[i] - min_pace < 0:
            min2 += L[i] - min_pace
    return str(min1) + " " + str(min2)

for it in range(int(f.readline().strip('\n'))):
    n = int(f.readline().strip('\n'))
    L = map(int,f.readline().strip('\n').split(' '))

    out.write("Case #%d: %s\n" % (it+1,func(n,L)))
