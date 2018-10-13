def win(line):
    s=""
    s=s.join(line)
    if s in ["XXXT","TXXX","XXXX"]:
        return "X"
    elif s in ["OOOT","TOOO","OOOO"]:
        return "O"
    else:
        return "False"

        
def row(block):
    l1=[]
    for row in block:
        l1.append(win(row))
    return l1
        


def column(block):
    l2=[]
    for num in range(0,4):
        column=[]
        for row in block:
            column.append(row[num])    
        l2.append(win(column))
    return l2

def diagonal(block):
    l3=[]
    diag1=[]
    diag2=[]
    for n in range(0,4):
        diag1.append(block[n][n])
    for n in range(0,4):
        diag2.append(block[n][3-n])
    l3.append(win (diag1))
    l3.append(win (diag2))
    return l3
        
    

l=[]
m=[]
case=1
file=open("small.in","r")
n=int(file.readline())
del n
for line in file:
    line=line.rstrip("\n")
    if line!="":
        m.append(list(line))
    if len(m)%4==0 and len(m)!=0:
        l.append(m)
        m=[]
file.close()
text=open("output.txt","a")
for block in l:
    if "X" in column(block) or "X" in row(block) or "X" in diagonal(block):
        text.write("Case #%d: X won\n" % case)
        case+=1
    elif "O" in column(block) or "O" in row(block) or "O" in diagonal(block):
        text.write("Case #%d: O won\n" % case)
        case+=1
    else:
        if "." in block[0] or "." in block[1] or "." in block[2] or "." in block[3]:
            text.write("Case #%d: Game has not completed\n" % case)
            case+=1
        else:
            text.write("Case #%d: Draw\n" % case)
            case+=1
text.close()
