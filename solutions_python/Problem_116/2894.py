def play(f, f1):
    t = int(f1.readline())
    c=1
    while(c<=t):
        arr=[]
        arr.append(f1.readline())
        arr.append(f1.readline())
        arr.append(f1.readline())
        arr.append(f1.readline())
        #conditions for winning the game
        check =0       
        for i in (range(0,4)):
            X=0
            O=0
            #for checking row
            for j in range(0,4):
                if arr[i][j]=='T':
                    X+=1
                    O+=1
                elif arr[i][j] == 'X':
                    X+=1
                elif arr[i][j] == 'O':
                    O+=1
                
            if X==4:
                f.write("Case #%d: X won" % (c,))
                c+=1
                check = 1
            elif O==4:
                f.write("Case #%d: O won" % (c,))
                c+=1
                check = 1
                
            #for checking column
            if check == 0:
                X=0
                O=0
                for j in range(0,4):
                     if arr[j][i]=='T':
                        X+=1
                        O+=1
                     elif arr[j][i] == 'X':
                        X+=1
                     elif arr[j][i] == 'O':
                        O+=1
                
                if X==4:
                    f.write("Case #%d: X won" % (c,))
                    c+=1
                    check = 1
                elif O==4:
                    f.write("Case #%d: O won" % (c,))
                    c+=1
                    check =1
            
        #for checking forward diagonals
        if check == 0:
            X=0
            O=0
            for j in range(4):
                if arr[j][j]=='T':
                    X+=1
                    O+=1
                elif arr[j][j] == 'X':
                    X+=1
                elif arr[j][j] == 'O':
                    O+=1
            if X==4:
                f.write("Case #%d: X won" % (c,))
                c+=1
                check = 1
            elif O==4:
                f.write("Case #%d: O won" % (c,))
                c+=1
                check = 1          
        
        #for checking backward diagonal
        if check == 0:
            X=0
            O=0
            k=0
            for j in range(3,-1,-1):
                if arr[k][j]=='T':
                    X+=1
                    O+=1
                elif arr[k][j] == 'X':
                    X+=1
                elif arr[k][j] == 'O':
                    O+=1
                k+=1
            if X==4:
                f.write("Case #%d: X won" % (c,))
                c+=1
                check = 1
            elif O==4:
                f.write("Case #%d: O won" % (c,))
                c+=1
                check =1
                
        
           
        
        
        
        #if game is not completed
        if check ==0:
        	for i in range(4):
        	    for j in range(4):
        	        if arr[i][j] == '.':
        	            check =1
        	if check == 1:
        		f.write("Case #%d: Game has not completed" % (c,))
        		c+=1
        		
        		          
        #game is draw
        if check ==0:
        	f.write("Case #%d: Draw" % (c,))
        	c+=1
        f.write("\n")
        f1.readline()
    
 
 
f1= open('A-small-attempt1.in')
f = open('output.txt', 'w')
play(f, f1)
