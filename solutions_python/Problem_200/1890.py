import bisect
def isTidy(n):
    m = str(n)
    for i in range(0,len(str(n))-1):
        if m[i] > m[i+1]:
            return False
    return True
def lastTidy(x):
    # find leftmost index
    dl = list(map(int,str(x)))
    rightindices = list(filter(lambda i: dl[i] > dl[i+1],range(0,len(dl)-1)))
    xn = 0
    if len(rightindices) != 0:
        xn = (min(rightindices))
    while dl[xn] < dl[xn-1] and xn != 0:
        xn-= 1
        if xn == 0:
            break
    dl[xn] -= 1
    for i in range(xn+1,len(dl)):
        dl[i] = 9
    neu = int(''.join(map(str,dl)))
    return neu
def lastTidyt(x):
    for i in range(0,len(str(x))):
        m = 10**i
        if isTidy(x):
            return x
        for j in range(10):
            if(str(x)[-(i+1)]) != '9':
                x -= m
        #print("%d %d %s"%(m,x,str(x)[-(i+1)]))
    return x



def genNext(list):
    liste = sorted(list,key=lambda x:str(x)[-1])
    neueliste = list[:]
    lprinted = 0
    for i in range(0,len(list)):
        if int(i/len(list)*100) != lprinted:
            print(i/len(list)*100)
            lprinted += 1
        l = list[i]
        for j in range(0,len(list)):
            if isTidy(str(list[i])+str(list[j])):
                neueliste.append(int(str(list[i])+str(list[j])))
    return list(set(neueliste))
"""
liste = []
for n in range(10**0,10**7):
    if isTidy(n):
        print(n)
        liste.append(n)

print(isTidy(14376))
print("Doing it")
for i in range(10**0,10**7):
    if not isTidy(i):
       if liste[bisect.bisect_left(liste, i) - 1] != lastTidyt(i):
        print(i)
        print(">> "+str(liste[bisect.bisect_left(liste, i) - 1]))
"""
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())  # read a list of integers, 2 in this case
  print("Case #{}: {}".format(i, lastTidyt(n)))