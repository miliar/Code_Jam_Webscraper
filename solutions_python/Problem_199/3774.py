from multiprocessing import Process

def readInput(filename):
    file = open(filename, "r")
    T= int(file.readline())
    print "there are "+str(T)+" tests"
    test_cases=[]
    for line in file:
        state=line.split()[0]
        k = int(line.split()[1])
        #print "state: "+state+" k:"+str(k)
        test_cases.append((state,k))
    return test_cases

def flip(state,k,index):
    new_state = list(state)
    for i in range(k):
        if new_state[index+i]=='+':
            new_state[index+i]='-'
        else:
            new_state[index + i] = '+'
    return ''.join(new_state)

def correct(state):
    for c in state:
        if c == '-':
            return False
    return True

def solve_test_Case(test_case,depth=0,visited=[],processes=[]):
    k = test_case[1]
    state=test_case[0]
    print state
    if correct(state):
        print "solved at depth "+str(depth)
        for p in processes:
            p.terminate()
        return depth
    if state in visited:
        return
    visited.append(state)
    for i in range(len(state)-k):
        new_state=(flip(state,k,i),k)
        #solve_test_Case(new_state, depth + 1, visited)
        p = Process(target=solve_test_Case, args=(new_state, depth + 1, visited,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

def solve_test_Case_2(test_case):
    k = test_case[1]
    state=test_case[0]
    array=list(state)
    count =0
    for i in range(len(state)-k+1):
        if array[i] == '-':
            array =list(flip(''.join(array),k,i))
            #print array
            count+=1
    if correct(''.join(array)):
        return count
    else:
        return -1
def create_output(solution):
    file= open("output.txt", "w")
    problem=1
    for s in solution:
        if not s == -1:
            file.write("Case #"+str(problem)+": "+str(s)+"\n")
        else:
            file.write("Case #" + str(problem) + ": IMPOSSIBLE\n")
        problem +=1
    file.close()

test_cases=readInput("A-large.in")
print test_cases
solution=[]
for t in test_cases:
    count=solve_test_Case_2(t)
    solution.append(count)
    #print "T1: "+str(count)
create_output(solution)