
#stall_info indices
LOCCUP = 0
ROCCUP = 1

MINMAX = 2

MINS = 0
MAXS = 1 

#[[]]
stall_info = None

#[(Ls,Rs)]
LR = None


def initCont(N):
    global stall_info, LR
    #build guard stalls too
    stall_info=[[0,0,(-1,-1)]] #left guard stall
    LR = [(-1,-1)]
    for i in range(1,N+1):
        stall_info.append([0,N+1, (min(i-1, N-i),max(i-1,N-i)) ])
        LR.append((i-1,N-i))
    stall_info.append([N+1,N+1,(-1,-1)]) #right guard stall
    LR.append((-1,-1))



def prepareStalls(selectedS, N):
    global stall_info, LR
    info = stall_info[selectedS]
    #change left stall info
    for i in range(info[LOCCUP]+1,selectedS):
        LR[i] = (LR[i][LOCCUP], selectedS-i-1)
        stall_info[i][ROCCUP]= selectedS
        stall_info[i][MINMAX] = (min(LR[i]), max(LR[i]))
        
    #change right stall info
    for i in range(selectedS+1, info[ROCCUP]):
        LR[i] = (i-1-selectedS, LR[i][ROCCUP])
        stall_info[i][LOCCUP]= selectedS
        stall_info[i][MINMAX] = (min(LR[i]), max(LR[i]))
        
    #make selectedS occupied    
    LR[selectedS] = (-1,-1)
    stall_info[selectedS] = [selectedS, selectedS, (-1, -1)]


def new_decision(N):
    global stall_info, LR
    
    maxminVal = 0
    maxminSet = []
    for i in range(1, N+1):
        stall_min = stall_info[i][MINMAX][MINS]
        if stall_min > maxminVal:
            maxminVal = stall_min
            maxminSet = [i]
        elif stall_min == maxminVal:
            maxminSet.append(i)
    if len(maxminSet) ==1:
        return maxminSet[0]

    #choose from maxmax
    maxmaxVal = 0
    maxmaxSet = []
    for stall in maxminSet:
        stall_max = stall_info[stall][MINMAX][MAXS]
        if stall_max > maxmaxVal:
            maxmaxVal = stall_max
            maxmaxSet = [stall]
        elif stall_max == maxmaxVal:
            maxmaxSet.append(stall)
    #left-most max
    return maxmaxSet[0]



def put_people_to_stalls(N, K):
    global stall_info, LR
    for k in range(1,K):
        selectedS = new_decision(N)
        prepareStalls(selectedS, N)
    #last visitor
    selectedS = new_decision(N)
    (z,y) = stall_info[selectedS][MINMAX]

    return (y,z)

def readFile(fileName):
    with open(fileName) as f:
        lines = f.readlines()
    num_tests = int(lines[0])
    tests={}
    for i in range(1,num_tests+1):
        NK = lines[i].rstrip('\n')
        N,K=NK.split(' ')
        tests[str(i)] = {'N':N, 'K':K, 'output': None}
    return tests


def write_outputs(tests):
    with open('smallInput1_Res.txt','w') as fw:
        for i in range(1,len(tests)+1):
            si = str(i)
            output = tests[si]['output']
            print('N:{0}, K:{1}, output:{2}'.format(tests[si]['N'], tests[si]['K'], output))
            fw.write('Case #{0}: {1} {2}\n'.format(si, output[0],output[1]))
            
def runTest(N,K):
    initCont(int(N))
    return put_people_to_stalls(int(N), int(K))


def main():
    tests = readFile('C-small-1-attempt0.in')
    for i, test in tests.items():
        tests[i]['output']=runTest(tests[i]['N'], tests[i]['K'])
    write_outputs(tests)
    


if __name__ == "__main__": main()