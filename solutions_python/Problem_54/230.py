def gcd(a, b):
    if (b==0):
        return a;
    else:
        return gcd(b, a%b)

fin= open("in.txt", "r")
fout= open("out.txt", "w")
t= int(fin.readline())

for i in range(1, t+1):
    data= fin.readline().split(' ')
    mas= list()
    for j in range(1, len(data)):
        mas.append(int(data[j]))
    mas.sort()
    mas.reverse()
    nod= mas[1]-mas[0]
    for j in range(0, len(mas)):
        for k in range(j+1, len(mas)):
            nod= gcd(nod, mas[j]-mas[k])
    res= (nod-mas[0]%nod)%nod;
    fout.write("Case #{0}: {1}\n".format(i, res))
fin.close()
fout.close()
