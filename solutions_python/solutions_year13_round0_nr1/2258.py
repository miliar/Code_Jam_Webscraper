#################################################################
### https://code.google.com/codejam/contest/2270488/dashboard ###
#################################################################
cases = int(raw_input())
for z in xrange(cases):
    sol    = []
    #adding rows to solution set
    for y in xrange(4):
        sol.append(raw_input())
    #adding cols to solution set
    for y in xrange(4):
        col = ""
        for x in xrange(4):
            col= col+sol[x][y]
        sol.append(col)
    #adding diagonals to solution set
    sol.append(sol[0][0]+sol[1][1]+sol[2][2]+sol[3][3])
    sol.append(sol[0][3]+sol[1][2]+sol[2][1]+sol[3][0])
    #processing solution set
    ans=0               #draw
    for y in xrange(len(sol)):
        if (sol[y].count('X') == 4 or (sol[y].count('X') == 3 and sol[y].count('T') == 1)):
            ans = 2         # x won the game
        if (sol[y].count('O') == 4 or (sol[y].count('O') == 3 and sol[y].count('T') == 1)):
            if ans ==2:
                ans =0      # both x and o won, essentially a draw
            else:
                ans =3      # o won the game
        if ans == 0 and sol[y].count('.') !=0:
            ans = 1         # not completed
        #print sol[y].count('X'), sol[y].count('O'), sol[y].count('T'), sol[y].count('.')
    if ans ==0:
        print "Case #"+str(z+1)+": Draw"
    elif ans ==1:
        print "Case #"+str(z+1)+": Game has not completed"
    elif ans ==2:
        print "Case #"+str(z+1)+": X won"
    elif ans ==3:
        print "Case #"+str(z+1)+": O won"    
    #print sol
    #handling the empty file at the end of each test case
    if z != cases-1:
        empty   = raw_input()