import sys


#####################

def printMove():
    tmp=raw_input()
    tmp=tmp.split()
    R=int(tmp[0])
    C=int(tmp[1])
    
    tiles=[]
    hcount = 0
    #take R inputs
    for i in xrange(R):
        tiles.append(raw_input())
        for c in xrange(C):
            if tiles[i][c] is "#":
                hcount = hcount + 1
    #tiles[] built
                
    if hcount % 4 is not 0:
        print "Impossible"
        return 0
    #case 1 done

    for i in xrange(R-1):
        for c in xrange(C-1):
            if tiles[i][c] is "#":
                
                rep = ['/','\\','\\','/']
                #print "HHH",tiles[i][c]
                if tiles[i][c+1] is "#" and tiles[i+1][c] is "#" and tiles[i+1][c+1] is "#":
                    s= list(tiles[i])
                    s=s[:c]+rep[0:2]+s[c+2:]
                    tiles[i]="".join(s)
                    s= list(tiles[i+1])
                    s=s[:c]+rep[2:4]+s[c+2:]
                    tiles[i+1]="".join(s)
                
    for i in xrange(R-1):
        for c in xrange(C-1):
            if tiles[i][c] is "#":
                print "Impossible"
                return 0
            
    for i in xrange(R):
            print tiles[i]
        
    return 1

####################
sys.stdin = open("in.txt", "r")

sys.stdout = open("out.txt", "w")
no = input()
for i in xrange(0,no):
    print "Case #{0}:".format(i+1)
    printMove()

sys.stdout.close()
#
