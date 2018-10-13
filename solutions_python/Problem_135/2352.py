stuff = []


with open("a.in", "r") as txt:
    for line in txt:
        lis = line.strip('\n')
        stuff += [lis]

T = int(stuff[0])
stuff.remove(stuff[0])
i = 0
while(i < T) :
    R1 = int(stuff[0])
    ans = stuff[R1].split()
    stuff.remove(stuff[0])
    stuff.remove(stuff[0])
    stuff.remove(stuff[0])
    stuff.remove(stuff[0])
    stuff.remove(stuff[0])
    R2 = int(stuff[0])
    ans2 = stuff[R2].split()
    stuff.remove(stuff[0])
    stuff.remove(stuff[0])
    stuff.remove(stuff[0])
    stuff.remove(stuff[0])
    stuff.remove(stuff[0])
    #print(ans)
    #print(ans2)
    magic = list(set(ans) & set(ans2))
    #print(magic)
    if(len(magic) == 0):
        print("Case #" + str(i+1) + ": Volunteer cheated!")
    elif (len(magic) == 1):
        print("Case #" + str(i+1) + ": " + str(magic[0]))
    else :
        print("Case #" + str(i+1) + ": Bad magician!")
    i += 1
    #print()
