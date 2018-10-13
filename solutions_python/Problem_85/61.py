
t = 0
fp = open("large.txt")  #input filename
fout = open("large_out.txt", "w") #output filename

    
def get_input():
    global t

    t = int(fp.readline())
    
    for i in xrange(t):
        line = fp.readline().split()
        l = int(line[0])
        t = int(line [1])
        n = int(line[2])
        c = int(line[3])
        c_list = map(int, line[4:])
        yield l,n,t,c,c_list

def process(l,n,t,c,c_list):
    c_dict = {}
    time_taken = 0
    crossed = False
    for i in xrange(n):
        time_taken += (c_list[i%c] *2)
        if time_taken >= t and crossed == False:
            #print "time", time_taken, t, time_taken%t
            c_dict[(time_taken - t)/2] = c_dict.get(time_taken,0) + 1
            crossed = True
            continue;

        if crossed:
            c_dict[c_list[i%c] ] = c_dict.get(c_list[i%c],0 ) +1

    #optimize
    ckeys = c_dict.keys()
    ckeys.sort(reverse=True)
    
    while(l >0):

        mx = ckeys[0]
        #print mx,l, ckeys, c_dict
        if c_dict[mx] >= l :
            time_taken -= min(l,c_dict[mx]) * mx
            break;

        tmp = c_dict[mx]
        time_taken -= mx * tmp
        l-=tmp
        ckeys.pop(0)
        
            
        
    return time_taken
    
for i,j in enumerate(get_input(), 1):
    l,n,t,c,c_list = j
    r = process(l,n,t,c,c_list)
    print "Case #%s: %s" % (i,r)
    print >> fout, "Case #%s: %s" % (i,r)
    
fout.close()
