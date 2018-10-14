#a is less significant than b
def satisfy_pair(a,b):
    return a>=b


#if the integer array is not tidy, return the less significant index
#not satisfying tidyness.
def get_index_not_satisfiable(ar, checkpoint):
    for i in range(checkpoint,0,-1):
        if not satisfy_pair(ar[i],ar[i-1]):
            return i
    return None

#N is string
def get_last_tidy(N):
    arintN = [int(i) for i in N]
    tidy = list(arintN)
    checkpointer = len(tidy)

    for time in range(len(tidy)-1,0,-1):
        index_not_satisfy = get_index_not_satisfiable(tidy, checkpointer-1)
        if index_not_satisfy is not None:
            tidy[index_not_satisfy-1]-=1
            checkpointer= index_not_satisfy
    
    if checkpointer is len(tidy):
         return N
    #apply 9-ers to the non-satisfiable subarray
    tidy[checkpointer:]=[9]*(len(tidy)-checkpointer)
    return int(''.join(map(str,tidy)))



def readFile(fileName):
    with open(fileName) as f:
        lines = f.readlines()
    num_tests = int(lines[0])
    print('Num tests:{0}'.format(num_tests))
    tests={}
    for i in range(1,num_tests+1):
        tests[str(i)] = {'input':lines[i].rstrip('\n'), 'output': None}
    return tests


def write_outputs(tests):
    with open('B-large.txt','w') as fw:
        for i in range(1,len(tests)+1):
            si = str(i)
            fw.write('Case #{0}: {1}\n'.format(si, tests[si]['output']))
            


def main():
    tests = readFile('B-large.in')
    for i, test in tests.items():
        tests[i]['output']=get_last_tidy(tests[i]['input'])
        #print('N:{0} ->tidy: {1}'.format(tests[i]['input'], tests[i]['output']))
    write_outputs(tests)
    


if __name__ == "__main__": main()


