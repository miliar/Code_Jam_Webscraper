#####ggj3


A = 0
B = 0
value = 0
string = ""
def changeorder (k):
    val=0
    leng = len(string)
    

    for i in range (1,leng):
        string2 = string[i:]+ string[:i]
##        if k==1234:
##            print string2
        if string2[0]=="0":
            continue
        
        if k < int (string2) and int(string2) <= B:
            val = val+1
            
    return val
fin = open ("small.in","r")
fout = open ("small.out","w")
T=0

abc = fin.readline()
T = int (abc[:-1])
j=0

while j < T:
    value =0
    j = j+1
    sting = fin.readline()
    A = int (sting[:sting.find(" ")])
    if not j==T:
        B = int (sting[sting.find(" "): -1])    
    else:
        B = int (sting[sting.find(" "):])
##    print T,A,B
    
    for k in range (A,B+1):
    ##    print k
        string = str(k)
        value = value + changeorder(k)
    sting2 = "Case #%s: %s\n"%(j,value)
    fout.writelines(sting2)
    fout.writelines('\n')
