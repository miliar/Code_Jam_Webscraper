

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
    f = open(r'./Outputs/A-small-attempt0.out','w')
    #f = open(r'\Outputs\Output00%s.txt' % n,'w')
    for i in range(len(outputs)):
        f.write('Case #%d: %s\n' % (i+1,outputs[i] if outputs[i] is not None else 'IMPOSSIBLE'))
    f.close()


def flip(S,K,i):
    ans = S[:i]
    for each in S[i:i+K]:
        if each == '+': ans += '-'
        else: ans += '+'
    ans += S[i+K:]
    return (ans, K,)

def solve(problem, n=0):
    S, K = problem
    K = int(K)
    if S.count('-') == 0:
        return n

    i = S.index('-')
    if i + K > len(S):
        return None
    return solve(flip(S,K,i),n+1)


if __name__ == '__main__':
    inputName = r'./Inputs/A-small-attempt0.in'
    problems = readFile(inputName)
    outputs = []
    for problem in problems:
        outputs.append(solve(problem))
    writeOutput(outputs)
    print("Finished.")