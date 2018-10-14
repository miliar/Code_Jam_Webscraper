import re

def solve(fout,case,S,C,D):
    temp = ''
    for i in range(len(S)):
        temp += S[i]
        #search for C
        for j in range(len(C)):
            temp = re.sub(C[j][0:2],C[j][2],temp)
            temp = re.sub(C[j][1::-1],C[j][2],temp)
        #search for D
        check = temp
        for j in range(len(D)):
            temp = re.sub(D[j][0]+'.*'+D[j][1],'',temp)
            temp = re.sub(D[j][1]+'.*'+D[j][0],'',temp)
            if check != temp:
                temp = ''
                break

    fout.write("Case #"+str(case)+": [")
    for i in range(len(temp)):
        fout.write(temp[i])
        if i < len(temp)-1:
            fout.write(", ")
    fout.write("]\n")

def main():
    #setting up
    fin = open("input.txt","r")
    fout = open("output.txt","w")
    
    case = 0
    for line in fin:
        case += 1
        line = line.split()
        
        #get C
        C = []
        for i in range(int(line[0])):
            C.append(line[i+1])
            
        #get D
        i = int(line[0])
        D = []
        for j in range(int(line[i+1])):
            D.append(line[i+j+2])
            
        #get string
        S = line[len(line)-1]
        
        solve(fout,case,S,C,D)

    fout.close()
    fin.close()

main()
