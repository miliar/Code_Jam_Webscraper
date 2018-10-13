#Recycled Numbers


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

from collections import deque

flist = file.readlines()
flist = [temp.strip() for temp in flist]
flist = [temp.split() for temp in flist]


#Do the work here:

flist = [[int(y) for y in temp] for temp in flist]
t = flist[0][0]
final = []
myset = set()
       
for i in range(1,t+1):
    top = flist[i][0]
    bot = flist[i][1]
    count = 0
    myset.clear()

    for j in range(top,bot+1):
        temp = str(j)
        d = deque(temp)
        for m in range(len(temp)-1):
            d.rotate(1)
            temp = "".join(d)
            var = int(temp)
            if (var > j) and (var<=bot):
                 count += 1
                 if (j,var) in myset:
                     count -= 1
                 myset.add((j,var))

    final.append(str(count))  
    


#Writing to Output file:
    
wfile = open("G:\codejam\\" + fname, "w")

for i in range(t):
    wfile.write("Case #" + str(i+1) + ": " + str(final[i]) + "\n")

wfile.close()
             
