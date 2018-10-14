# Sample
sample_inp = '''4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21'''
sample_outp = '''Case #1: 3
Case #2: 2
Case #3: 1
Case #4: 3'''

# get input file
inp_name = raw_input("What's the input file name?\n")
inp = open(inp_name)

# initialize output file
outp = open('output.out','w')

# get N
N_str = inp.readline().replace('\n','')
N = int(N_str)

# helping procedures
def triplet(total):
    avg = total/3
    r = total%3
    if r==0:
        return (avg,avg,avg)
    elif r==1:
        return (avg+1,avg,avg)
    else:
        return (avg+1,avg+1,avg)

def improvable((a,b,c)):
    if(b>0 and a<10 and a==b):
        return True
    else:
        return False
    
def best(triplet, s=False):
    if(s and improvable(triplet)):
        return max(triplet)+1
    else:
        return max(triplet)
    
# line by line
for i in xrange(1,N+1):
    line_lst = inp.readline().replace('\n','').split(' ')
    n = int(line_lst[0])
    s = int(line_lst[1])
    p = int(line_lst[2])
##    print '\tn=' + str(n)
##    print '\ts=' + str(s)
##    print '\tp=' + str(p)
    totals = map(int, line_lst[3:])
##    print '\n\ttotals=' + str(totals)
    if(len(totals) != n):
        print "ACHTUNG FEHLER"
        exit
    triplets = map(triplet, totals)
##    print '\n\tregular_bests=' + str(regular_bests)
    y = 0
    for trip in triplets:
        if best(trip)>= p:
            y += 1
        elif s>0 and best(trip, True)>=p:
            y += 1
            s -= 1
            
    result = 'Case #' + str(i) + ': ' + str(y)
    print result
    outp.write(result)
    outp.write('\n')

# close input/output files    
inp.close()
outp.close()
