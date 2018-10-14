file = open("A-small-attempt1.in","r")
out = open("out.txt","w")
listA = []
listB = []
listC = []

numCase = int(file.readline())

for x in range(1,numCase+1):
    ans = int(file.readline())
    for y in range(1,5):
        if y == ans:
            listA = map(int,file.readline().split())
        else:
            file.readline()
    ans = int(file.readline())
    for y in range(1,5):
        if y == ans:
            listB = map(int,file.readline().split())
        else:
            file.readline()
    listC = list(set(listA).intersection(set(listB)))
    if len(listC) == 0:
        print >> out, "Case #"+str(x)+": Volunteer cheated!"
    if len(listC) == 1:
        print >> out, "Case #"+str(x)+": "+str(listC[0])
    if len(listC) > 1:
        print >> out, "Case #"+str(x)+": Bad magician!"

out.close()
file.close()
