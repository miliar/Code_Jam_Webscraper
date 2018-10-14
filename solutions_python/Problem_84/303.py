
f=open("A-large.in.txt","r")
lines=f.readlines()
f.close()


T=eval(lines[0])

f=open('o.in','w')

line=0

for i in range(T):
    print(str(i+1))
    line+=1

    temp=lines[line].split()

    l=eval(temp[0])
    c=eval(temp[1])

    
    grid=[]
    for j in range(l):
        grid.append(list(range(c)))

    for j in range(l):
        line+=1

        temp=lines[line]
        

        for k in range(c):
            grid[j][k]=temp[k]


    # Fin de l'input

    for j in range(l):
        for k in range(c):
            if j+1<l and k+1<c:
                droite=grid[j][k+1]
                depart=grid[j][k]
                bas=grid[j+1][k]
                basdroite=grid[j+1][k+1]

                if droite=='#' and depart=='#' and bas=='#' and basdroite=='#':
                    grid[j][k]='/'
                    grid[j][k+1]='\\'
                    grid[j+1][k]='\\'
                    grid[j+1][k+1]='/'

    diese=False

    for j in range(l):
        for k in range(c):
            if grid[j][k]=='#':
                diese=True

    f.write("Case #"+str(i+1)+":\n")

    if diese==True:
        f.write("Impossible\n")
    else:
        for j in range(l):
            for k in range(c):
                f.write(grid[j][k])
            f.write("\n")
                

f.close()
    
    
