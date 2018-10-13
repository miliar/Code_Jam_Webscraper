
def read_file(filepath):
    try:
        lines = file(filepath, 'rU').readlines()
    except IOError, e:
        print '*** file open failed:', filepath
        raise e
    else:
        return lines

def get_longest_sequence(start):
    longest_id = None
    longest_length = 0
    for id in range(len(servers)):
        j = start
        length = 0
        while(j<Q and seq[id][j]==False):
            length += 1
            j += 1
        print servers[id], length
        if length>longest_length:
            longest_length = length
            longest_id = id
    return longest_id, longest_length

# main
lines = read_file('./data/A-large.in')
for i in range(len(lines)):
    lines[i] = lines[i].rstrip('\r\n')
print lines

N = int(lines[0])
answers = []
i = 1
for n in range(N):
    # read a case
    print 'case #'+str(n+1)+':'
    S = int(lines[i])
    i += 1
    servers = []
    for j in range(S):
        servers.append(lines[i])
        i += 1
    print 'servers:', servers
    Q = int(lines[i])
    i += 1
    if Q==0:
        answers.append(0)
        continue
    queries = []
    for _ in range(Q):
        queries.append(lines[i])
        i += 1
    print 'queries:', queries
    
    # check for 0
    zero = False
    for s in servers:
        if not s in queries:
            zero = True
            break
    if zero==True:
        answers.append(0)
        continue
    
    # create on/off sequences
    seq = []
    for s in servers:
        tmp = []
        for q in queries:
            if q==s:
                tmp.append(True)
            else:
                tmp.append(False)
        seq.append(tmp[:])
    for j in range(len(servers)):
        print servers[j], seq[j]
        
    #
    k = 0
    switches = -1
    while(k<Q):
        id, length = get_longest_sequence(k)
        print 'longest:', servers[id], length
        k += length
        switches += 1
    answers.append(switches)
        
# answers
for n in range(N):
    print 'Case #'+str(n+1)+':', answers[n]

