#! /usr/bin/env python
#coding=utf-8

def add(tree, node):
    ns = node.split('/')[1:]
    ct = 0
    crt = tree
    for n in ns:
        if not crt.has_key(n):
            ct += 1
            crt[n] = dict()
        crt = crt[n]
    return ct
            

def solve(icase, case_input):
    case_output = 'Case #%d: '%icase
    
#    print icase, case_input
    N, K = [int(x) for x in case_input[0].split()]
    root = dict()
    for i in xrange(N):
        add(root, case_input[1 + i])
    count = 0
    for i in xrange(K):
        count += add(root, case_input[1 + N + i])
        
    case_output += '%d'%count
    
    return case_output  


def main():
    global use_test_data
    global test_data
    global input_file
    global output_file
    
    if use_test_data:
        data = [x.strip() for x in test_data.split('\n')]
    else:
        data = [x.strip() for x in input_file.readlines()]
    
    T = int(data[0])
    iLine = 1
    caseLineNum = 1
    for icase in range(1, T + 1):
        input = []
        N, K = [int(x) for x in data[iLine].split()]
        caseLineNum = N + K
        input.append(data[iLine])
        iLine += 1
        for i in range(caseLineNum):
            input.append(data[iLine])
            iLine += 1
        rslt = solve(icase, input)
        print rslt
        if not use_test_data:
            print >> output_file, rslt
    
    if not use_test_data:
        input_file.close()
        output_file.close()
    
    
if __name__ == '__main__':
    test_data = """3
0 2
/home/gcj/finals
/home/gcj/quals
2 1
/chicken
/chicken/egg
/chicken
1 3
/a
/a/b
/a/c
/b/b"""
    use_test_data = False
    
    test_file = 'A-large.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()
    