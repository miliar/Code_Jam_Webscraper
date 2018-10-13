N=0

def cpp(stage,r,c) -> bool: #Can place plus
    tr=r+1
    tc=c+1
    while(tr<N and tc<N):
        if(stage[tr][tc]=='+' or stage[tr][tc]=='o'):
            return False
        else:
            tr+=1
            tc+=1
    tr=r-1
    tc=c+1
    while(tr>=0 and tc<N):
        if(stage[tr][tc]=='+' or stage[tr][tc]=='o'):
            return False
        else:
            tr-=1
            tc+=1
    tr=r+1
    tc=c-1
    while(tr<N and tc>=0):
        if(stage[tr][tc]=='+' or stage[tr][tc]=='o'):
            return False
        else:
            tr+=1
            tc-=1
    tr=r-1
    tc=c-1
    while(tr>=0 and tc>=0):
        if(stage[tr][tc]=='+' or stage[tr][tc]=='o'):
            return False
        else:
            tr-=1
            tc-=1
    return True

def cpx(stage,r,c): #Can place x
    tr=r+1
    while(tr<N):
        if(stage[tr][c]=='x' or stage[tr][c]=='o'):
            return False
        else:
            tr+=1
    tr=r-1
    while(tr>=0):
        if(stage[tr][c]=='x' or stage[tr][c]=='o'):
            return False
        else:
            tr-=1
    tc=c-1
    while(tc>=0):
        if(stage[r][tc]=='x' or stage[r][tc]=='o'):
            return False
        else:
            tc-=1
    tc=c+1
    while(tc<N):
        if(stage[r][tc]=='x' or stage[r][tc]=='o'):
            return False
        else:
            tc+=1
    return True
            
with open("D-small-attempt9.in") as file:
    arr=file.readlines()
cases=int(arr[0])
index=1
wfile=open("outfile.txt",'w')
for case in range(cases):
    line=arr[index].split()
    index+=1
    N=int(line[0])
    M=int(line[1])
    stage=[['.' for x in range(N)] for y in range(N)]
    for i in range(M):
        line2=arr[index].split()
        row=int(line2[1])
        col=int(line2[2])
        stage[row-1][col-1]=line2[0]
        index+=1
    changelist=[]
    for i in range(N):
        for j in range(2):
            if(stage[i][j*(N-1)]=='.'):
                if(cpp(stage,i,j*(N-1))):
                    if(cpx(stage,i,j*(N-1))):
                        stage[i][j*(N-1)]='o'
                        changelist.append(['o',i+1,j*(N-1)+1])
                    else:
                        stage[i][j*(N-1)]='+'
                        changelist.append(['+',i+1,j*(N-1)+1])
            elif(stage[i][j*(N-1)]=='+'):
                if(cpx(stage,i,j*(N-1))):
                    stage[i][j*(N-1)]='o'
                    changelist.append(['o',i+1,j*(N-1)+1])
            elif(stage[i][j*(N-1)]=='x'):
                if(cpp(stage,i,j*(N-1))):
                    stage[i][j*(N-1)]='o'
                    changelist.append(['o',i+1,j*(N-1)+1])
    for i in range(2):
        for j in range(1,N-1):
            if(stage[i*(N-1)][j]=='.'):
                if(cpp(stage,i*(N-1),j)):
                    if(cpx(stage,i*(N-1),j)):
                        stage[i*(N-1)][j]='o'
                        changelist.append(['o',i*(N-1)+1,j+1])
                    else:
                        stage[i*(N-1)][j]='+'
                        changelist.append(['+',i*(N-1)+1,j+1])
            elif(stage[i*(N-1)][j]=='+'):
                if(cpx(stage,i*(N-1),j)):
                    stage[i*(N-1)][j]='o'
                    changelist.append(['o',i*(N-1)+1,j+1])
            elif(stage[i*(N-1)][j]=='x'):
                if(cpp(stage,i*(N-1),j)):
                    stage[i*(N-1)][j]='o'
                    changelist.append(['o',i*(N-1)+1,j+1])
    for i in range(1,N-1):
        for j in range(1,N-1):
            if(stage[i][j]=='.'):
                if(cpp(stage,i,j)):
                    if(cpx(stage,i,j)):
                        stage[i][j]='o'
                        changelist.append(['o',i+1,j+1])
                    else:
                        stage[i][j]='+'
                        changelist.append(['+',i+1,j+1])
            elif(stage[i][j]=='+'):
                if(cpx(stage,i,j)):
                    stage[i][j]='o'
                    changelist.append(['o',i+1,j+1])
            elif(stage[i][j]=='x'):
                if(cpp(stage,i,j)):
                    stage[i][j]='o'
                    changelist.append(['o',i+1,j+1])
    for i in range(N):
        for j in range(N):
            if(stage[i][j]=='.'):
                if(cpx(stage,i,j)):
                    if(cpp(stage,i,j)):
                        stage[i][j]='o'
                        changelist.append(['o',i+1,j+1])
                    else:
                        stage[i][j]='x'
                        changelist.append(['x',i+1,j+1])
            
    score=0
    for i in range(N):
        for j in range(N):
            if(stage[i][j]=='+' or stage[i][j]=='x'):
                score+=1
            elif(stage[i][j]=='o'):
                score+=2
    wfile.write("Case #{}: {} {}\n".format(case+1,score,len(changelist)))
    for el in changelist:
        wfile.write("{} {} {}\n".format(el[0],el[1],el[2]))
print('done')
wfile.close()
                
    
    
