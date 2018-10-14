import math

def demo():
    a=open("D-large.in")
    b=a.readlines()
    outf=open("out.txt","w")
    
    for i in range(int(b[0])):
        res=check(b[i*3+2].split(),b[i*3+3].split())        
        print "Case #"+str(i+1)+": "+str(res)
        outf.write("Case #"+str(i+1)+": "+str(res)+"\n")
    outf.close()

def kenChoice(i):
    global kenW
    if max(kenW)<i:
        return kenW.pop(kenW.index(min(kenW)))
    return kenW.pop([x>i for x in kenW].index(True))

def check(r1,r2):
    global naoW
    global kenW
    naoW=[]
    kenW=[]
    for i in range(len(r1)):
        naoW.append(float(r1[i]))
        kenW.append(float(r2[i]))
    kenW.sort()
    naoW.sort()
    
    naoScore=0
    for i in naoW:
        kenChosen = kenChoice(i)
        if kenChosen < i:
            naoScore+=1

    for i in range(len(r1)):
        kenW.append(float(r2[i]))
    kenW.sort()
    
    naoScoreDW=0
    while len(kenW)>0:
        res = sum([naoW[i]>kenW[i] for i in range(len(naoW))])
        if res>naoScoreDW:
            naoScoreDW=res
        kenW.pop()
        naoW.pop(0)
    
    return str(naoScoreDW)+" "+str(naoScore)
    
    
raw_input("Got data?")
demo()

