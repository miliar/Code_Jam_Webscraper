

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
    problems = [line.strip() for line in f]
    f.close()
    assert T == len(problems), "Didn't load the right amount of problems."
    return problems

def writeOutput(outputs, n=1):
    f = open(r'./Outputs/B-small-attempt0.out','w')
    #f = open(r'\Outputs\Output00%s.txt' % n,'w')
    for i in range(len(outputs)):
        f.write('Case #%d: %s\n' % (i+1,outputs[i]))
    f.close()

def solve(n):
    if isTidy(n):
        return n
    elif isJump(n):
        return solve(jump(n))
    return solve(n-1)

def isJump(n):
    l = len(str(n))
    return int('1'+'0'*(l-1)) < n < int('1'*(l-1)+'0')

def jump(n):
    l = len(str(n))
    return int('1'+'0'*(l-1))

def isTidy(n):
    p = 0
    for i in str(n):
        if int(i) >= p:
            p = int(i)
        else:
            return False
    return True

if __name__ == '__main__':
    inputName = r'./Inputs/B-small-attempt0.in'
    problems = readFile(inputName)
    outputs = []
    for problem in problems:
        outputs.append(solve(int(problem)))
    writeOutput(outputs)
    print("Finished.")