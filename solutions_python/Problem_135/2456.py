info = open("C:\Users\Feynman\Downloads\A-small-attempt0.in","r")
magiclist =[]
for line in info:
    line=line.strip()
    magiclist.append(line)

info.close()

testcase = int(magiclist.pop(0))

def choose(magiclist):
 k = int(magiclist.pop(0))

 row = magiclist[k-1].split(" ")
 
 return row

def solution(row1,row2):
 solution = []
 for i in range(len(row1)):
    for j in range(len(row2)):
        
        if row1[i] == row2[j]:
            solution.append(row1[i])
            
 if len(solution) == 1:
    return solution[0]
 if len(solution) >= 2:
    return "Bad magician!"
 if solution ==[]:
    return "Volunteer cheated!"

for i in range(testcase):
       
 row1 = choose(magiclist)
 magiclist = magiclist[4:]
 row2 = choose(magiclist)
 magiclist = magiclist[4:]

 print "Case #" +str(i+1)+": ", solution(row1,row2)

