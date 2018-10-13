
#now how to write a function deciding if possible to win in 1 click on R*C board
#with M mines or not
def ispossible(Rt,Ct,M):
    #returns str w Impossible or a legit mine configuration
    done=False
    #deal with NO MINES case
    if M==0:
        #in this case it's possible but have to write a fnctn creating an
        #appropriate output
        done=True
        st="c"
        for i in range(Ct-1):
            st=st+'.'
        st=st+'\n'
        for j in range(Rt-1):
            for i in range(Ct):
                st=st+'.'
            st=st+'\n'
        #at this pt st is a valid mine configuration w 1 click no mines
        return st
    #now, dealt with no mines case, can now assume M>0
    
    #deal with ALL COVERED WITH MINES
    if M==(Rt*Ct):
        done=True
        return "Impossible\n"
    #now can assume 0<M<R*C so there's at least one free space
    
    #now can deal with only one free space:
    if M==(Rt*Ct-1):
        done=True
        st="c"
        for i in range(Ct-1):
            st=st+'*'
        st=st+'\n'
        for j in range(Rt-1):
            for i in range(Ct):
                st=st+'*'
            st=st+'\n'
        #at this pt st is a valid mine configuration w 1 click all else mines
        return st

    #now can assume M>0 but also that there are at least two free spots
    
    #first want to reassign so that can assume R<C
    R=min(Rt,Ct)
    C=max(Rt,Ct)
    if Rt>Ct:
        swapped=True
    else:
        swapped=False
    #now R<=C possibly swapped row-column numbers, and swapped variable
    #keeps track of whether we had to do the swap or not so that we can
    #give a non-swapped output at the end

    #now wanna deal with various degenerate cases, like R=1 or 2
    #R=1 first: R=1 and as we can assume exist mines and at least two free spots
    #so all such configurations are POSSIBLE, now just have to generate
    #the outputs

    #for convenience: define F to be a number of free spots
    F=R*C-M
    
    if R==1:
        done=True
        if not swapped:
            #nonswapped one row case
            st=""
            for i in range(M):
                st=st+'*'
            for i in range(F-1):
                st=st+'.'
            st=st+"c\n"
            return st
        else:
            #swapped R=1 case - ie actually one column
            st=""
            for i in range(M):
                st=st+'*\n'
            for i in range(F-1):
                st=st+'.\n'
            st=st+"c\n"
            return st
    #ok, dealt with R=1 case, now can assume R>=2
        
    #as R>=2 and F>=2 only can win in 1 click if that's click on zero
    #but having a zero in R>=2 case even corner one forces at least 4
    #free spots so in our assumption F=2,3 are impossible
    if F==2:
        done=True
        return "Impossible\n"
    if F==3:
        done=True
        return "Impossible\n"
    #so now can assume R>=2 F>=4
    
    #now let's deal with R=2 case which is still kinda degenerate
    #and remember have at least 4 free spots and some mines so in particular
    #C>=3 is implied by that
    if R==2:
        done=True
        #impossible to have 1 click win w odd number of mines coz
        #zeros come in whole columns in this case
        if ((M%2)!=0):
            return "Impossible\n"
        #now M is divisible by 2
        M2=M/2
        if not swapped:
            #in non-swapped case
            #winning configuration if M2 columns of mines then C-M2 empty columns
            l1=""
            l2=""
            for i in range(M2):
                l1=l1+'*'
                l2=l2+'*'
            for i in range(C-M2-1):
                l1=l1+'.'
                l2=l2+'.'
            l1=l1+'.\n'
            l2=l2+'c\n'
            return (l1+l2)
        else:
            #now actly have 2 columns and C rows
            #M2 rows of mines C-M2 empty rows, click in last spot
            st=""
            for i in range(M2):
                st=st+"**\n"
            for i in range(C-M2-1):
                st=st+"..\n"
            st=st+".c\n"
            return st
            

    #now can assume M>=1 F>=4 R>=3
    if F==4:
        done=True
        #4 free spots+assumptions above always possible w empty square in
        #the corner
        if not swapped:
            st="c."
            for i in range(C-2):
                st=st+'*'
            st=st+'\n..'
            for i in range(C-2):
                st=st+'*'
            st=st+'\n'
            for j in range(R-2):
                for i in range(C):
                    st=st+'*'
                st=st+'\n'
            return st
        else:
            st="c."
            for i in range(R-2):
                st=st+'*'
            st=st+'\n..'
            for i in range(R-2):
                st=st+'*'
            st=st+'\n'
            for j in range(C-2):
                for i in range(R):
                    st=st+'*'
                st=st+'\n'
            return st
    #now can assume M>=1 R>=3 F>=5
        
    #also F=5 impossible as zero must be either in the corner then 4 free spots
    #or if not then at least 6 free spaces if the zero is in the middle of
    #a side
    if F==5:
        done=True
        return "Impossible\n"
    
    #now F>=6
    #F=6 can do analogously to F=4, by putting a 2*3 box in the corner
    #with a zero (and click) in a second cell from top-left
    if F==6:
        done=True
        if not swapped:
            st=".c."
            for i in range(C-3):
                st=st+'*'
            st=st+'\n...'
            for i in range(C-3):
                st=st+'*'
            st=st+'\n'
            for j in range(R-2):
                for i in range(C):
                    st=st+'*'
                st=st+'\n'
            return st
        else:
            st=".c."
            for i in range(R-3):
                st=st+'*'
            st=st+'\n...'
            for i in range(R-3):
                st=st+'*'
            st=st+'\n'
            for j in range(C-2):
                for i in range(R):
                    st=st+'*'
                st=st+'\n'
            return st
    #now R>=3, F>=7. is F=7 possible? it's kinda related to that R=3
    #degenerate case so maybe let's do that first
    if R==3:
        done=True
        #now R=3, and still M>=1 F>=7
        #turns out F=7 doesn't work in this case
        if F==7:
            return "Impossible\n"
        #now R=3 F>=8
        M3=M/3
        MR=M%3
        #M3 - number of columns of mines, MR - non-full column remaining mines
        #MR=0,1,2 so let's do these cases separately
        if MR==0:
            if not swapped:
                #need M3 columns of mines, then C-M3 empty columns,
                #click in bottom-right-most spot
                l1=""
                l2=""
                l3=""
                for i in range(M3):
                    l1=l1+"*"
                    l2=l2+"*"
                    l3=l3+"*"
                for i in range(C-M3-1):
                    l1=l1+"."
                    l2=l2+"."
                    l3=l3+"."
                l1=l1+'.\n'
                l2=l2+'.\n'
                l3=l3+'c\n'
                return (l1+l2+l3)
            else:
                #now swapped case - M3 rows of mines in this case total of
                #C rows
                l=""
                for i in range(M3):
                    l=l+"***\n"
                for i in range(C-M3-1):
                    l=l+"...\n"
                l=l+"..c\n"
                return l
        #now we've dealt with M being divisible by 3 case
        if MR==1:
            if not swapped:
                #need M3 columns of mines then '*..'^t column then empty columns
                #click in bottomrightmost as usual
                l1=""
                l2=""
                l3=""
                for i in range(M3):
                    l1=l1+"*"
                    l2=l2+"*"
                    l3=l3+"*"
                l1=l1+"*"
                l2=l2+"."
                l3=l3+"."
                for i in range(C-M3-2):
                    l1=l1+'.'
                    l2=l2+'.'
                    l3=l3+'.'
                l1=l1+'.\n'
                l2=l2+'.\n'
                l3=l3+'c\n'
                return (l1+l2+l3)
            else:
                l=""
                #now need M3 rows of mines then '*..'
                for i in range(M3):
                    l=l+'***\n'
                l=l+'*..\n'
                for i in range(C-M3-2):
                    l=l+'...\n'
                l=l+'..c\n'
                return l
        #dealt with MR==0 and MR==1 cases. what happens with MR==2 case?
        if MR==2:
            #3*3 board with 2 mines 7 free spots is impossible
            if C==3:
                return "Impossible\n"
            #now MR=2 and C>=4: which means we can fit an appropriate
            #3*4 box to realize this configuration
            if not swapped:
                l1=""
                l2=""
                l3=""
                for i in range(M3):
                    l1=l1+"*"
                    l2=l2+"*"
                    l3=l3+"*"
                l1=l1+"**"
                l2=l2+".."
                l3=l3+".."
                for i in range(C-M3-3):
                    l1=l1+"."
                    l2=l2+"."
                    l3=l3+"."
                l1=l1+".\n"
                l2=l2+".\n"
                l3=l3+"c\n"
                return (l1+l2+l3)
            else:
                #swapped case
                l=""
                for i in range(M3):
                    l=l+"***\n"
                l=l+"*..\n*..\n"
                for i in range(C-M3-3):
                    l=l+"...\n"
                l=l+"..c\n"
                return l
    #back to our general function level
    #now have R>=4 F>=7.
    #a bit unsure but seems like F=7 impossible
    #???check if not works in the end
    if F==7:
        done=True
        return "Impossible\n"
    #so now R>=4 F>=8
    #2R+2,2R+3,...3R,3R+2,3R+3,...4R etc are all possible in a kinda
    #uniform manner so let's code that first
    Fk=F/R
    Fr=F%R
    l=[[0 for i in range(C)] for i in range(R)]
    #empty R*C list
    if ((Fk>=2) & (Fr!=1)):      
        #gonna save our mine distribution as r*c list of symbols
        #each of which is '.', '*' or 'c' - it's gonna be easier
        #to convert that to required form later, swapping should become
        #simpler
        l[0][0]='c'
        for i in range(1,R):
            l[i][0]='.'
        #filled the first column
        for j in range(1,Fk):
            for i in range(R):
                l[i][j]='.'
        #filled first Fk columns
        if Fk<C:
            #filling the tricky Fk+1-th column
            for i in range(Fr):
                l[i][Fk]='.'
            for i in range(Fr,R):
                l[i][Fk]='*'
        #now filled first Fk+1 columns
        if Fk+1<C:
            for j in range(Fk+1,C):
                for i in range(R):
                    l[i][j]="*"
        done=True
        #now filled the whole l: it's left to print it out appropriately:
    #actly, can leave the printing till the very end if we use that same l
    #to store the proper board pictures in all the other cases as well
                    
    #now, have M>=1 R>=4 F>=8 and dealt with the generic case where
    #dealt: Fk>=2 & Fr!=1
                    
    #let's deal with Fk>=2 Fr=1 case
    #Fr=1 Fk=2 is tricky so let's leave that for now;
    #in Fr=1 Fk>=3 case it's clear what to do
    if ((Fr==1) &(Fk>=3) & (not done)):
        #first Fk-1 cols empty, click top-left corner, then 2 spcl colums
        # then C-(Fk+1) mine columns
        l[0][0]='c'
        for i in range(1,R):
            l[i][0]='.'
        for j in range(1,Fk-1):
            for i in range(R):
                l[i][j]='.'
        for i in range(R-1):
            l[i][Fk-1]='.'
        l[R-1][Fk-1]='*'
        l[0][Fk]='.'
        l[1][Fk]='.'
        for i in range(2,R):
            l[i][Fk]='*'
        #now tricky columns are filled, the rest is all mines
        for j in range(Fk+1,C):
            for i in range(R):
                l[i][j]='*'
        #now l filled in this case
        done=True
    #now dealt with a lot of free space Fk>=2 cases except for
    #Fk=2 Fr=1
    #let's deal with some of the 'little free space' cases
    #note F=R*Fk+Fr and still have F>=8 bound
    #not Fk>=2 case means 8<=F<2R
    #if F even it's clear how to fill out
    if ((Fk<=1) & (F%2==0) & (not done)):
        n=F/2
        #fill as follows: columns starting third one all mines
        #in first two columns first n rows are empty rest is mines again
        for j in range(2,C):
            for i in range(R):
                l[i][j]='*'
        #filled all the columns except the first one
        l[0][0]='c'
        l[0][1]='.'
        for j in range(2):
            for i in range(1,n):
                l[i][j]='.'
            for i in range(n,R):
                l[i][j]='*'
    
        #l all done in this even case
        done=True
    #now, what about the small & odd case? ie still F<2R Fk<=1
    #btw, I think F=8 is now dealt with automatically, so can assume F>=9    
    #figured out how to do F=9+2k case, for F from 9 up to 2R+3, which
    #settles small and odd case
    if ((Fk<=1) & (F%2==1) & (not done)):
        k=(F-9)/2 #the k in my notes
        #can assume R,C>=4
        #first three columns are tricky, starting fourth is all mines
        l[0][0]='c'
        l[0][1]='.'
        l[0][2]='.'
        l[1][0]='.'
        l[1][1]='.'
        l[1][2]='.'
        l[2][0]='.'
        l[2][1]='.'
        l[2][2]='.'
        for j in range(3,C):
            for i in range(R):
                l[i][j]='*'
        for i in range(3,R):
            l[i][2]='*'
        for j in range(2):
            for i in range(k):
                l[i+3][j]='.'
            for i in range(k+3,R):
                l[i][j]='*'
        #now l all filled in this case
        done=True
    #now Fk<=1 case is all settled! hooray!
    #the only thing which was left is Fk=2 Fr=1 ie F=2R+1 case
    #but this is basically the previous case with k=R-1
    if ((not done) & (Fk==2) & (Fr==1)):
        k=R-4
        l[0][0]='c'
        l[0][1]='.'
        l[0][2]='.'
        l[1][0]='.'
        l[1][1]='.'
        l[1][2]='.'
        l[2][0]='.'
        l[2][1]='.'
        l[2][2]='.'
        for j in range(3,C):
            for i in range(R):
                l[i][j]='*'
        for i in range(3,R):
            l[i][2]='*'
        for j in range(2):
            for i in range(k):
                l[i+3][j]='.'
            for i in range(k+3,R):
                l[i][j]='*'
        #now l all filled in this case
        done=True
    #now it seems like all is done: left to convert to string form and return
    if done:
        if not swapped:
            #R - # of actual rows in non-swapped case
            st=""
            for i in range(R):
                for j in range(C):
                    st=st+str(l[i][j])
                st=st+'\n'
            return st
        else:
            #swapped case wanna output R columns C rows
            st=""
            for i in range(C):
                for j in range(R):
                    st=st+str(l[j][i])
                st=st+'\n'
            return st
    #seems like this is it for our function, left only to do
    #some input-output
                
inn=open("C:/downloads/in.in",'r')
rst=open("C:/downloads/rs.rs",'w')
T=int(inn.readline())
for i in range(T):
    l=inn.readline()
    ls=l.split()
    Rt=int(ls[0])
    Ct=int(ls[1])
    M=int(ls[2])
    rst.write("Case #"+str(i+1)+":\n"+ispossible(Rt,Ct,M))
inn.close()
rst.close()
