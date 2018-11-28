#Dancing


#Opening input file:

while True:
    choice = input("Large or Small set: ")
    if choice == "s":
        file = open("G:\Downloads\chrome download\B-small-practice.in")
        fname = "B-small-practice.in"
        break
    elif choice == "l":
        file = open("G:\Downloads\chrome download\B-large-practice.in")
        fname = "B-large-practice.in"
        break
    elif choice == "t":
        file = open("G:\\Downloads\\chrome download\\test.txt")
        fname = "test.txt"
        break
    elif choice == "c":
        fname = input('Enter file name: ')
        floc = "G:\Downloads\chrome download\\" + fname
        file = open(floc)
        break
    else:
        print("Wrong Choice")

flist = file.readlines()
flist = [temp.strip() for temp in flist]
flist = [temp.split() for temp in flist]


#Do the work here:

flist = [[int(y) for y in temp] for temp in flist]
t = flist[0][0]
global surp
final = []

#function definition

def setfind(ntotal):
    

    if ntotal >=3:
        temp = ntotal//3
        score = range(temp - 2,temp + 2)
        for i in score:
            for j in range(i,i+2):
                for k in range(i, i+2):
                    if i+j+k == ntotal:
                      return [i,j,k]
    else:
        temp = ntotal
        score = range(0,temp+1)
        for i in score:
            for j in range(i,i+2):
                for k in range(i, i+2):
                    if i+j+k == ntotal:
                      return [i,j,k]

    return 0

def optmark(ntotal,p):
    global surp
    marks = setfind(ntotal)
    if marks[2]+1 == p:
        if (surp != 0) and (marks[0]>0):
            if marks[2] == marks[0]:
                surp -= 1
                marks[2] += 1
                marks[0] -= 1
            elif marks[2] == marks[1]:
                surp -= 1
                marks[2] += 1
                marks[1] -= 1
    return [marks[0],marks[1],marks[2]]






for i in range(1,t+1):
    n = flist[i][0]
    surp = flist[i][1]
    p = flist[i][2]
    finalmarks = []
    count = 0
    
    for googler in range(n):
        total = flist[i][googler + 3]
        finalmarks.append(optmark(total,p))
        if finalmarks[googler][2] >= p:
            count += 1
    final.append(count)
    
    
  



#Writing to Output file:
    
wfile = open("G:\codejam\\" + fname, "w")

for i in range(t):
    wfile.write("Case #" + str(i+1) + ": " + str(final[i]) + "\n")

wfile.close()
             
