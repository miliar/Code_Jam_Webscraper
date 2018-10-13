fin = open('A-large.in','r')
fout = open('ovationLarge.out','w')

cases = int(fin.readline().strip())

a = 1

while a <= cases:
    currStanding = 0
    numFriends = 0

    data = fin.readline().strip().split(" ")

    maxShyness = int(data[0])
    audience = data[1]

    for i in range(0,maxShyness+1):
        people = int(audience[i])
        if people != 0:
            if currStanding >= i:
                currStanding += people
            else:
                numFriends += (i - currStanding)
                currStanding += (i - currStanding)
                currStanding += people
    
    fout.write('Case #'+str(a)+': '+str(numFriends)+"\n")

    a+=1
fin.close()
fout.close()
