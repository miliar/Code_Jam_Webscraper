'''
Created on 14-04-2012

@author: Hokanos
'''
import sys
def shifts(S,i):
    return S[i:] + S[:i]
    
def calcNums(A,B):
    dt = {}
    t = []
    sdt = {}
    sa = str(A)
    sb = str(B)
    ai = int(sa[0])
    bi = int(sb[0])
    counter = 0
    for i in range(A,B+1,1):
        dt[i] = 0
        t.append(str(i))
        sdt[str(i)] = 0
        
    print(sdt)
#    for i in range(len(t)-1,-1,-1):
#        tmp = t[i]
#        itmp = int(tmp)
#        dict = {}
#        for j in range(len(tmp)-1,0,-1):
#            num = int(shifts(tmp,j))
#            if (num in dt) and ((itmp > num) and (itmp != num)):
#                if num in dict:
#                    continue
#                else:
#                    dict[num] = 0
#                    counter+=1

    
    for x in t:
        tmp = int(x)
        i = 1
        used = {}
        while(i<len(x)):
            newt = shifts(x,i)
            num = int(newt)
            #if ((num <= B) and (num > A) and (num in dt) and (num != tmp)):
            #    if ~(num in used):
            #        used[num] = 0
            #        counter+=1
            if tmp < num:
                if newt[0] != "0":
                    if (newt in sdt) and (newt != x):
                        if ((newt in used) == False):
                            counter+=1
                            used[newt] = 0
                            print(newt)
                
            i+=1
            
    return counter
def main():
    f = open(sys.argv[1],"r")
    fw = open("out.out","w")
    
    lines = int(f.readline())
    for i in range(lines):
        n = f.readline().rstrip().split(" ")
        print(n)
        fw.write("Case #"+str(i+1)+": "+str(calcNums(int(n[0]),int(n[1])))+"\n")
    
    fw.close()
    f.close()

    
main()
#print(calcNums(1111,2222))