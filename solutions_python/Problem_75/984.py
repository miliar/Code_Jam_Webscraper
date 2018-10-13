import sys


def addtostack(stack, combine, opposed, element):
    stack.append(element)
    if len(stack) > 1:
        e1 = stack[-1]
        e2 = stack[-2] 
        
        for a,b,c in combine:
            if (a == e1 and b == e2) or (b == e1 and a == e2):
                stack = stack[:-2]
                addtostack(stack, combine, opposed, c)
                break
                
    if len(stack) > 1:
        e1 = stack[-1]
        e2 = stack[-2]
        for a, b in opposed:
            if (a in stack) and (b in stack):
                stack = []
                break  
    return stack
    
def dotest(combine, opposed, invoke):
    stack = []
    for e in invoke:
        stack = addtostack(stack, combine, opposed, e)
        print stack
    
    return '[' + ', '.join(stack)[:] + ']'

def main(tests):
    results = []
    tests = tests.split('\n')
    tests = tests[1:]
    case = 0
    for test in tests:
        test = test.split(' ')
        print test
        cnum = int(test.pop(0))
        combine = test[:cnum]
        test = test[cnum:]
        dnum = int(test.pop(0))
        opposed = test[:dnum]
        test = test[dnum:]
        nnum = int(test.pop(0))
        invoke = test.pop(0)
        
        
        print combine
        print opposed
        print invoke
        print '----------------------'
        case = case + 1
        results.append('Case #' + str(case) +': ' + dotest(combine, opposed, invoke) + '\n')
        print '######################'
              
    return ''.join(results)

if __name__ == '__main__':
    inpath = sys.argv[1]
    fin = open(inpath, 'r')
    tests = fin.read()
    fin.close()
    results = main(tests)
    fout = open('outputfile.txt' ,'w')
    fout.write(results)
    fout.close()
        