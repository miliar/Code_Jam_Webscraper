'''
Created on May 6, 2011

@author: mk
'''


def solve(fin, fout):
    cases = int(fin.readline())
    for index in range(cases):
        tokens = fin.readline().strip().split()
        fout.write(solveCase(index+1, tokens))

def solveCase(index, tokens):
    c = int(tokens.pop(0))
    combiners = dict()
    for _ in range(c):
        token = tokens.pop(0)
        combiners[token[0] + token[1]] = token[2]
        combiners[token[1] + token[0]] = token[2]
    
    d = int(tokens.pop(0))
    opposed = set()
    for _ in range(d):
        token = tokens.pop(0)
        opposed.add(token[0] + token[1])
        opposed.add(token[1] + token[0])
    
    n = int(tokens.pop(0))
    input = tokens.pop(0)
    
    stack = []
    for ch in input:
        should_add = True
        if stack:
            replaced_by = combiners.get(stack[-1] + ch)
            if replaced_by:
                stack[-1] = replaced_by
                should_add = False
                ch = replaced_by
        for item in stack:
            if item + ch in opposed:
                stack = []
                should_add = False
                break
        if should_add:
            stack += [ch]
        
    return "Case #{0}: [{1}]\n".format(index, ', '.join(stack))


def testSolve():
    from StringIO import StringIO
    input = StringIO("""5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW""")
    solve(input, sys.stdout)

if __name__ == '__main__':
    import sys
    #testSolve()
    solve(sys.stdin, sys.stdout)
    