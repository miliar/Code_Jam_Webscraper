'''
Created on 21/03/2013
Tic-Tac-Toe-Tomek

@author: Ferran Negre

'''

with open("A-large.in","r") as fp:
    with open("ouput.out","w") as out:
        cases = fp.readline()
        
        for k in range(0,int(cases)):
            X=0
            O=0
            point=0
            T=False
            done=0
            
            if(k==0):
                lines = [[]*4 for x in range(4)]
                for i in range(0,4):
                    lines[i] = fp.readline();
            else:
                lines = [[]*5 for x in range(5)]
                for i in range(0,5):
                    lines[i] = fp.readline();
                
            lines=[name for name in lines if name.strip()]
                        
            for i in range(0,4):
                if(done==0):
                    for j in range(0,4):
                        if (lines[i][j]=='X'): 
                            X+=1
                        elif(lines[i][j]=='O'):
                            O+=1
                        elif(lines[i][j]=='.'):
                            point+=1
                        elif(lines[i][j]=='T'):
                            T=True
                    if(X==4 or (X==3 and T)):
                        out.write("Case #" + str(k+1) + ": X won\n")
                        done=1
                    elif(O==4 or (O==3 and T)):
                        out.write("Case #" + str(k+1) + ": O won\n")
                        done=1
                    else:
                        X=0
                        O=0
                        T=False
            if(done==0):
                X=0
                O=0
                T=False                   
                for i in range(0,4):
                    if(done==0):
                        for j in range(0,4):
                            if (lines[j][i]=='X'): 
                                X+=1
                            elif(lines[j][i]=='O'):
                                O+=1
                            elif(lines[j][i]=='.'):
                                point+=1
                            elif(lines[j][i]=='T'):
                                T=True
                        if(X==4 or (X==3 and T)):
                            out.write("Case #" + str(k+1) + ": X won\n")
                            done=1
                        elif(O==4 or (O==3 and T)):
                            out.write("Case #" + str(k+1) + ": O won\n")
                            done=1;
                        else:
                            X=0
                            O=0
                            T=False 
                if(done==0):
                    X=0
                    O=0
                    T=False          
                    for i in range(0,4):         
                        if (lines[i][i]=='X'): 
                            X+=1
                        elif(lines[i][i]=='O'):
                            O+=1
                        elif(lines[i][i]=='.'):
                            point+=1
                        elif(lines[i][i]=='T'):
                            T=True
                    if(X==4 or (X==3 and T==True)):
                        out.write("Case #" + str(k+1) + ": X won\n")
                        done=1
                    elif(O==4 or (O==3 and T==True)):
                        out.write("Case #" + str(k+1) + ": O won\n")
                        done=1
                    elif(done==0):
                        X=0
                        O=0
                        T=False          
                        for i in range(0,4):         
                            if (lines[i][3-i]=='X'): 
                                X+=1
                            elif(lines[i][3-i]=='O'):
                                O+=1
                            elif(lines[i][3-i]=='.'):
                                point+=1
                            elif(lines[i][3-i]=='T'):
                                T=True
                        if(X==4 or (X==3 and T==True)):
                            out.write("Case #" + str(k+1) + ": X won\n")
                        elif(O==4 or (O==3 and T==True)):
                            out.write("Case #" + str(k+1) + ": O won\n")
                        elif(point>0):
                            out.write("Case #" + str(k+1) + ": Game has not completed\n")
                        else:
                            out.write("Case #" + str(k+1) + ": Draw\n")