

def readFile(fname):
    """
    The first line of the input gives the number of test cases, T. 
        T test cases follow. 
    Each consists of one line with a string S and an integer K. 
        S represents the row of pancakes: 
            each of its characters is either 
                + (which represents a pancake that is initially happy side up) or 
                - (which represents a pancake that is initially blank side up).
    :param fname: string file path to the input file.
    :return: list of problems, [(S_0,K_0,),(S_1,K_1,),...(S_T,K_T,)]
    """
    f = open(fname)
    T = int(f.readline().strip())
    problems = [line.strip().split() for line in f]
    f.close()
    assert T == len(problems), "Didn't load the right amount of problems."
    return problems

def writeOutput(outputs, n=1):
    f = open(r'./Outputs/C-small-1-attempt0.out','w')
    #f = open(r'\Outputs\Output00%s.txt' % n,'w')
    for i in range(len(outputs)):
        f.write('Case #%d: %d %d\n' % (i+1, outputs[i][0], outputs[i][1]))
    f.close()

def solve(problem):
    N, K = problem
    N = int(N)
    K = int(K)
    stalls = '0' + '.'*N + '0'
    for i in range(K-1):
        stalls = update(stalls)
    values = calculateLR(stalls)
    m = findMaxMin(values)
    return max(values[m]), min(values[m])

def calculateLR(stalls):
    values = []
    for i in range(len(stalls)):
        if stalls[i] == '0':
            values.append((None,None,))
        else:
            L = len(stalls[:i].rsplit('0',1)[-1])
            R = len(stalls[i+1:].split('0',1)[0])
            values.append((L,R,))
    return values

def update(stalls):
    values = calculateLR(stalls)
    m = findMaxMin(values)
    if isinstance(m,tuple):
        print(m)
    s = list(stalls)
    s[m] = '0'
    return ''.join(s)

def findMaxMin(values):
    m = 0
    maxes = []
    for i in range(len(values)):
        if values[i][0] is not None and m < min(values[i]):
            m = min(values[i])
            maxes = [i]
        elif values[i][0] is not None and m == min(values[i]):
            maxes.append(i)
    m = 0
    best = []
    for i in range(len(maxes)):
        current = values[maxes[i]]
        if max(current) > m:
            m = max(current)
            best = [maxes[i]]
        elif max(current) == m:
            best.append(maxes[i])
    return best[0]

if __name__ == '__main__':
    inputName = r'./Inputs/C-small-1-attempt0.in'
    problems = readFile(inputName)
    outputs = []
    for problem in problems:
        outputs.append(solve(problem))
    writeOutput(outputs)
    print("Finished.")