f = open('asdf', 'w')

t = raw_input()

for counter in range(int(t)):
    ansone = int(raw_input())
    pos = []

    gridone = []
    gridtwo = []

    gridone.append(map(int,raw_input().rsplit()))
    gridone.append(map(int,raw_input().rsplit()))
    gridone.append(map(int,raw_input().rsplit()))
    gridone.append(map(int,raw_input().rsplit()))

    anstwo = int(raw_input())

    gridtwo.append(map(int,raw_input().rsplit()))
    gridtwo.append(map(int,raw_input().rsplit()))
    gridtwo.append(map(int,raw_input().rsplit()))
    gridtwo.append(map(int,raw_input().rsplit()))

    for num in gridone[ansone-1]:
        if num in gridtwo[anstwo-1]:
            pos.append(num)

    if len(pos) == 0:
        f.write("Case #" + str(counter+1) + ": Volunteer cheated!\n")
    elif len(pos) > 1:
        f.write("Case #" + str(counter+1) + ": Bad magician!\n")
    else:
        f.write("Case #" + str(counter+1) + ": " + str(pos[0]) +"\n")





    
