if __name__ == '__main__':
    f = file('D-small-attempt0.in')
    g=file('output.txt','w')
    line=f.readline()
    T=int(line)
    for k in range(T):
        line=f.readline()
        temp=line.split(" ")
        x=int(temp[0])
        r=int(temp[1])
        c=int(temp[2])
        winner=""
        if x==1:
            winner='GABRIEL'
        elif x==2:
            if r%2==0 or c%2==0:
                winner='GABRIEL'
            else:
                winner='RICHARD'
        elif x==3:
            if (r%2==0 and c%3==0) or (r%3==0 and c%2==0):
                winner='GABRIEL'
            else:
                winner='RICHARD'
        elif x==4:
            if r%4==0 and c%4==0:
                winner='GABRIEL'
            else:
                winner='RICHARD'
        elif x==5:
            if (r%5==0 and c%4==0) or (r%4==0 and c%5==0):
                winner='GABRIEL'
            else:
                winner='RICHARD'
        elif x==6:
            if (r%6==0 and c%4==0) or (r%4==0 and c%6==0):
                winner='GABRIEL'
            else:
                winner='RICHARD'
        ans="Case #"+str(k+1)+': '+winner+'\n'
        g.write(ans)
    f.close()
    g.close()