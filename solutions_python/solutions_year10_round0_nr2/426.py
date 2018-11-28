from fractions  import gcd

fin = open("B-large.in", "r")
fout = open("B-large.out", "w")

C = int(fin.readline())

#print( C)

for i in range(0, C, 1):
    tempList = str.split(fin.readline()," ")
    tempIntList = []

    
    for j in tempList:
        tempIntList.append(int(j))

    N = tempIntList[0]
    T = tempIntList[1:]

    T.sort()

    first = T[0]
    for j in range( len(T) ):
        T[j] -= first

    boris = T[1]

    for j in range(2, len(T)):
        boris = gcd(boris, T[j]);

    poo=((-first)%boris)
    fout.write("Case #" + str(i+1) + ": " + str(poo)+"\n")

fin.close()
fout.close()
