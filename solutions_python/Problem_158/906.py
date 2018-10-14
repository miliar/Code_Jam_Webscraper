with open("D-small-attempt8.in") as f:
    input_Arr = f.readlines()
with open("output.txt","w") as g:
    for q in range(int(input_Arr[0])):
        inp=input_Arr[q+1].split(' ')
        winner=''
        if (int(inp[1])*int(inp[2]))%(int(inp[0]))==0:
            if((int(inp[0]))>(int(inp[1])))and((int(inp[0]))>(int(inp[2]))):
                winner='RICHARD'
            else:
                if ((int(inp[1])*int(inp[2]))<=((int(inp[0]))*2))and(int(inp[0]))>3:
                    winner='RICHARD'
                if (((int(inp[0]))/2>=(int(inp[1]))or(int(inp[0]))/2>=(int(inp[2]))))and(int(inp[0]))>2:
                    winner='RICHARD'
                else:
                    winner='GABRIEL'
        else:
            winner='RICHARD'
        outp='Case #'+str(q+1)+': '+str(winner)+'\n'
        g.write(outp)
