f=open('C:\Python33\codejam\A-small-attempt2.in')
g=open('C:\Python33\codejam\codejam1.1output.txt','w')
t=int(f.readline().strip("\n"))

for p in range(0,t):
        flag=0
        li1=[]
        li2=[]
        for i in range(4): li1.append(list(f.readline().strip("\n")))
        
        for i in range(4): li2.append(list(li1[j][i] for j in range(4)))
        li3=[li1[i][i] for i in range(0,4)]
        li4=[li1[i][j] for (i,j) in [[0,3],[1,2],[2,1],[3,0]]]
        if ('T' in li3): li3.remove('T')
        if ('T' in li4): li4.remove('T')
        if (set(li3)=={'X'} or set(li4)=={'X'}) :
                g.write("Case #"+str((p+1))+": X won\n")
                flag=1
        elif (set(li3)=={'O'} or set(li4)=={'O'}) :
                g.write("Case #"+str((p+1))+": O won\n")
                flag=1
        else:
            for k in range(4):
                if ('T' in li1[k]): li1[k].remove('T')
                if ('T' in li2[k]): li2[k].remove('T')
                if (set(li1[k])=={'X'} or set(li2[k])=={'X'}): 
                    g.write("Case #"+str((p+1))+": X won\n")
                    flag=1
                    break
                elif (set(li1[k])=={'O'} or set(li2[k])=={'O'}): 
                    g.write("Case #"+str((p+1))+": O won\n")
                    flag=1
                    break
        if flag==0: 
                    if ('.' not in [li1[i][j] for i in range(0,2) for j in range(0,3)]): g.write("Case #"+str((p+1))+": Draw\n")
                    else : g.write("Case #"+str((p+1))+": Game has not completed\n")
        
        f.readline()
g.close()    
        
