#Google Code Jam - Magic Trick
solve=open ('/Users/thedopestethiopian/Desktop/solve.in')
loop=0
case=1
rowf=[]
rows=[]
here=False
finito=False
output=open("/Users/thedopestethiopian/Desktop/output.txt","w")
for numbers in solve:
    tries=0
    if loop==0:
        first=int(numbers)
    elif loop==first:
        for x in numbers.split():
            rowf.append(int(x))
    elif loop==5:
        second=int(numbers)
        added=loop
        here=True
    elif here==True and loop==second+added:
        for x in numbers.split():
            rows.append(int(x))
        finito=True
    if finito==True and loop==9:
        loop=-1
        for num1 in rowf:
            for num2 in rows:
                if num1==num2:
                    theone=num1
                    tries+=1
        if tries==1:
            line="Case #"+str(case)+": "+ str(theone)+"\n"
            output.write (str(line))
        elif tries>1:
            line="Case #"+str(case)+": Bad magician!\n"
            output.write(str(line))
        elif tries==0:
            line="Case #"+str(case)+": Volunteer cheated!\n"
            output.write (str(line))
        rowf=[]
        rows=[]
        case+=1
    loop+=1
output.close()
