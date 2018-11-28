'''
Created on May 6, 2011

@author: mk
'''

def solve(fin, fout):
    cases = int(fin.readline())
    for index in range(cases):
        _ignore = fin.readline()
        numbers = map(int, fin.readline().strip().split())
        fout.write(solveCase(index+1, numbers))


def solveCase(index, numbers):
    numbers_out_of_place = 0
    for number_index, number in enumerate(numbers):
        if number != number_index+1:
            numbers_out_of_place += 1
    return "Case #{0}: {1}.000000\n".format(index, numbers_out_of_place)
    

def testSolve():
    from StringIO import StringIO
    input = StringIO("""3
2
2 1
3
1 3 2
4
2 1 4 3""")
    solve(input, sys.stdout)

if __name__ == '__main__':
    import sys
    #testSolve()
    solve(sys.stdin, sys.stdout)
