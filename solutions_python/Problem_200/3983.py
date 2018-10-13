import queue

inputfile = 'input.txt'
outputfile = 'output.txt'

global caseId
caseId = 1

q = queue.Queue()

with open(inputfile) as inf:
    lines = [x.strip() for x in inf.readlines()]

for line in lines:
    q.put(int(line))
    
T = q.get()

def sort(l):
    for i in range(0, len(l)-1):
        if l[i] > l[i+1]:
            l[i] -= 1 
            l[i+1:] = [9 for x in l[i+1:]]
    return l



def write_case(D):
    global caseId
    D = ''.join([str(x) for x in D])
    output = 'Case #{}: {}\n'.format(caseId, int(D))
    with open(outputfile, 'a') as ouf:
        ouf.write(output)
    caseId += 1
    
    
    
while not q.empty():
    N = q.get()
    
    if N < 10:
        D = N
        write_case([D])
    else:
        arr = [int(x) for x in str(N)]
        for i in range(0, len(arr)-1):
            D = sort(arr)
        write_case(D)
        
    

    
    
    
    
    