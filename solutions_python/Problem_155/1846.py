# Import the file
with open('A-large.in','r') as f:
    data = f.readlines()

# Format the data
T = int(data[0])
del data[0]

def Check(Dist):
    Clapping = Dist[0]
    for i in range(1,len(Dist)):
        if Clapping >= i:
            Clapping += Dist[i]
        else:
            return(False)
    return(True)

NumberAdded = []
for i in range(T):
    MS,Dist = data[i][:-1].split(' ')
    MS = int(MS)
    Dist = [int(el) for el in Dist]
    Num = 0
    while not Check(Dist):
        Dist[0] += 1
        Num += 1
    NumberAdded.append(Num)

print(NumberAdded)

with open('A.out','w') as f:
    for i in range(T):
        f.write('Case #{0}: {1}\n'.format(i+1,NumberAdded[i]))
