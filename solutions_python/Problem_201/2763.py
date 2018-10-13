
def stalls2(n, k):
    n+=2
    file1 = open('test', 'w')
    if n-k < 2:
        return [0,0]

    D = [0]*n
    D[0]=1
    D[n-1]=1
    f1=-1
    f2=-1

    while k >= 1:
        count = 0
        max = 0
        maxi = 0
        pos = 0
        for i in range(0,n):
            if D[i] == 0:
                count+=1
            elif D[i]==1:
              if count >max:
                  max=count
                  pos = int(((count-1) / 2)) + maxi
                  if pos == 0:
                      pos += 1
                  f1 = pos- maxi
                  f2 = count - f1 -1

              maxi=i+1
              count=0

        if count > max:
            max = count
            pos = int(((count - 1) / 2)) + maxi
            if pos == 0:
                pos += 1
            f1 = pos-maxi
            f2 = count-f1-1

        D[pos] = 1

        if pos ==1:
            D[0]=1
        k-=1
       # print(k,D)
       # file1.write(';'.join(map(str, D)))
       # file1.write('\n');

    file1.close()
    return [f1,f2]

def readFile():
    f1 = open('C-small-1-attempt1.in', 'r')

    n = int(f1.readline())
    #w = temp.rstrip('\n')
    l = []

    for i in range(1,n+1):
        t = f1.readline().split()
        l.append(t)

    return l

#print(stalls2(5,2))


l = readFile()

for i in range(1, len(l)+1):
     t = l[i-1]
     res =  stalls2(int(t[0]), int(t[1]))
     f1 = max(res[0], res[1])
     f2 = min(res[0], res[1])
     print('Case #'+ str(i)+ ':',f1, f2)


