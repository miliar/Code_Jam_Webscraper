
def fix(n,infile):
        l=[]
        for x in range(n):
                line=infile.readline()

                l.append([])
                dotcount=0
                for c in line:
                        if c=='.':
                                dotcount+=1
                        else:
                                l[x].append(c)
                l[x]=(['.']*dotcount)+l[x]
                
        return l
                
                        

def test(l,n,k):

        byes=0
        ryes=0
        #columns
        for x in range(n):
                bcount=0
                rcount=0
                for y in range(n):
                        if l[x][y]=='R':
                                rcount+=1
                                bcount=0
                        elif l[x][y]=='B':
                                rcount=0
                                bcount+=1
                        else:
                                rcount=0
                                bcount=0
                        if bcount>=k:
                                byes=1
                        if rcount>=k:
                                ryes=1
                        if ryes and byes:
                                return 'Both'

        #Rows
        for y in range(n):
                bcount=0
                rcount=0
                for x in range(n):
                        if l[x][y]=='R':
                                rcount+=1
                                bcount=0
                        elif l[x][y]=='B':
                                rcount=0
                                bcount+=1
                        else:
                                rcount=0
                                bcount=0
                        if bcount>=k:
                                byes=1
                        if rcount>=k:
                                ryes=1
                        if ryes and byes:
                                return 'Both'


        #diag downward
        for x in range(n):
                xpos=x
                ypos=0
                bcount=0
                rcount=0
                while xpos<n and ypos<n:                
                        
                        if l[xpos][ypos]=='R':
                                rcount+=1
                                bcount=0
                        elif l[xpos][ypos]=='B':
                                rcount=0
                                bcount+=1
                        else:
                                rcount=0
                                bcount=0
                        if bcount>=k:
                                byes=1
                        if rcount>=k:
                                ryes=1
                        if ryes and byes:
                                return 'Both'
                        xpos+=1
                        ypos+=1

                xpos=0
                ypos=x
                bcount=0
                rcount=0
                while xpos<n and ypos<n:                
                        
                        if l[xpos][ypos]=='R':
                                rcount+=1
                                bcount=0
                        elif l[xpos][ypos]=='B':
                                rcount=0
                                bcount+=1
                        else:
                                rcount=0
                                bcount=0
                        if bcount>=k:
                                byes=1
                        if rcount>=k:
                                ryes=1
                        if ryes and byes:
                                return 'Both'
                        xpos+=1
                        ypos+=1
                        


        #diag upward
        for x in range(n):
                xpos=x
                ypos=0
                bcount=0
                rcount=0
                while xpos>=0 and ypos<n:              
                        
                        if l[xpos][ypos]=='R':
                                rcount+=1
                                bcount=0
                        elif l[xpos][ypos]=='B':
                                rcount=0
                                bcount+=1
                        else:
                                rcount=0
                                bcount=0
                        if bcount>=k:
                                byes=1
                        if rcount>=k:
                                ryes=1
                        if ryes and byes:
                                return 'Both'
                        xpos-=1
                        ypos+=1

                xpos=n-1
                ypos=x
                bcount=0
                rcount=0
                while xpos>=0 and ypos<n:              
                        if l[xpos][ypos]=='R':
                                rcount+=1
                                bcount=0
                        elif l[xpos][ypos]=='B':
                                rcount=0
                                bcount+=1
                        else:
                                rcount=0
                                bcount=0
                        if bcount>=k:
                                byes=1
                        if rcount>=k:
                                ryes=1
                        if ryes and byes:
                                return 'Both'
                        xpos-=1
                        ypos+=1




                        
        if ryes:
                return 'Red'
        elif byes:
                return 'Blue'
        else:
                return 'Neither'

                

def go():
        infile=open('in.txt')
        t=int(infile.readline())
        
        for case in range(t):
                n,k=[int(x) for x in infile.readline().split()]
                l=fix(n,infile)
               # for x in l:
               #         print x
                print ('Case #%d: '%(case+1))+test(l,n,k)


        infile.close()
