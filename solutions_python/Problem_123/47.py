import fileinput,sys
import math

print_indicator = 0

def myprint(*arg):
    if print_indicator != 0:
        print print_indicator
        print arg

lines = []

for line in fileinput.input():
    lines.append(line)

n= int(lines[0])


case = 0
line_no =1      
myprint("n",n)
for j in xrange(1,n+1):
    case +=1
    print "Case #%d:" % (case),
    nbym = (lines[line_no]).partition(" ")
    line_no +=1
    A = int(nbym[0])
    N = int(nbym[2])
    #slow(r,t)
    #fast(r,t)
    current_line = lines[line_no]
    line_no+=1
    row = []
    for k in xrange(0,N):
        cl_split = current_line.partition(" ")
        row.append(int(cl_split[0]))
        current_line = cl_split[2]
    #row.sort()
    myprint("row", row)
    added = 0
    delete_rest_score = N
    k = 0
    best_score = N
    cur_score = N
    row.sort()
    while (k < len(row)):
        myprint("A", A, "added", added, "best_score", best_score)
        if (A > row[k]):
            A += row[k]
            k +=1
            cur_score -=1
            if (cur_score < best_score):
                best_score = cur_score
        else:
            added += 1
            A += A-1
            cur_score += 1
            if added > best_score:
                break
        myprint("A", A, "added", added, "best_score", best_score)
    print best_score
            
            
            
            


                        
        
    
