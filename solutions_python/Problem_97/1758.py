
def isMirroredNumber(a, b):
    distinctPairs=[]
    if len(a) < 2:
        if a == b:
            return 1
        else:
            return 0
    pos = 1
    count = 0
    while pos < len(a):
        if a[pos:] + a[:pos] == b:
            if not a[pos:]+a[:pos] + ":" + b in distinctPairs:
                distinctPairs.append(a[pos:]+a[:pos] + ":" + b)
                count+=1
        pos+=1
    return count


firstSkipped=False
counter=1
out=open("out.txt","w")
for line in open("C-small-attempt0.in","r").readlines():
    if not firstSkipped:
        firstSkipped=True
        continue
    line=line.replace("\n","")
    numberA, numberB=line.split(" ")
    numberA=int(numberA)
    numberB=int(numberB)
    mirrorCounter=0
    for a in range(numberA, numberB):
        for b in range(a, numberB+1):
            if a < b and len(str(a))==len(str(b)):
                mirrorCounter+=isMirroredNumber(str(a), str(b))
    out.write("Case #" + str(counter)+ ": " + str(mirrorCounter) + "\n")
    counter+=1
    
out.close()