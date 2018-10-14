import sys


#readline = sys.stdin.readline() 

T = int(raw_input())
#print T

for t in range(1,T+1) :
    #print "\n\n\nFor casia %d"%(t,)
    grid = []
    
    incomplete = False 
    game_won = True 
    for l in range(4) :
        line = raw_input().rstrip('\n')
        if '.' in line :
            incomplete = True
        grid.append(line)

    horizontal = False
    for l in range(4) :


        sorted_s = ''.join(sorted(grid[l]))
        #print sorted_s

        if sorted_s in ['TXXX','XXXX'] :
            print "Case #%d: X won"%(t,)
            horizontal = True
            break

        elif sorted_s in ['OOOO','OOOT'] :
            print "Case #%d: O won"%(t,)
            horizontal = True

    vertical = False
    if not horizontal :
        #print 'not horizontal'
        for i in range(4) :
            s = ''
            s = grid[0][i]+grid[1][(4+i)%4]+grid[2][(8+i)%4]+grid[3][(12+i)%4]
            sorted_s = ''.join(sorted(s))
            if sorted_s in ['TXXX','XXXX'] :
	            print "Case #%d: X won"%(t,)
	            vertical = True
	            break

            elif sorted_s in ['OOOO','OOOT'] :
                 print "Case #%d: O won"%(t,)
                 vertical = True


    left_u_right_d = False
    left_d_right_u = False
    if not vertical and not horizontal :
        #print 'not v nor h t :',t 
        lu_rd = grid[0][0]+grid[1][1]+grid[2][2]+grid[3][3]
        sorted_s = ''.join(sorted(lu_rd))

        if sorted_s in ['TXXX','XXXX'] :
            print "Case #%d: X won"%(t,)
            left_u_right_d = True
            break

        elif sorted_s in ['OOOO','OOOT'] :
             print "Case #%d: O won"%(t,)
             left_u_right_d = True

        #print 'not left_u_right_d'
        if not left_u_right_d :
	        ld_ru = grid[0][3]+grid[1][2]+grid[2][1]+grid[3][0]
	        sorted_s = ''.join(sorted(ld_ru))
	
	        if sorted_s in ['TXXX','XXXX'] :
	            print "Case #%d: X won"%(t,)
	            left_d_right_u = True
	            #break
	
	        elif sorted_s in ['OOOO','OOOT'] :
	            print "Case #%d: O won"%(t,)
	            left_d_right_u = True
	        else :
	            game_won = False
	
    #print 'game_won is :',game_won
    #print 'game not complete is :',incomplete
    if not game_won and incomplete :
        print "Case #%d: Game has not completed"%(t,)
    elif not game_won and not incomplete :
        print "Case #%d: Draw"%(t,)
    raw_input()