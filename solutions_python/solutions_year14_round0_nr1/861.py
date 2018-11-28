#from Sets import set

ifile = open("A-small-attempt0.in","r")
T = ifile.next().rstrip("\n")

for i in range (int(T)):
    listA=[]
    listB=[]
    row = int(ifile.next().rstrip("\n"))
    for j in range(4):
       nextRow = ifile.next().rstrip("\n")
       if j+1 == row:
           listA=nextRow.split(" ")
    row2 = int(ifile.next().rstrip("\n"))
    for j in range(4):
        nextRow = ifile.next().rstrip("\n")
        if j+1 == row2:
            listB=nextRow.split(" ")

    setA, setB = set(listA), set(listB)
    common = setA.intersection(setB)
    if len(common) == 1:
        print "Case #"+str(i+1)+": " + str(next(iter(common)))
    if len(common) > 1:
        print "Case #"+str(i+1)+": Bad magician!"
    if len(common) < 1:
        print "Case #"+str(i+1)+": Volunteer cheated!"
    
    
