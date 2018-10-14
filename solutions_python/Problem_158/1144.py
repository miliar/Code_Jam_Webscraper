'''
    ------------------------------------------------------------------------------------------------------------------------------------------
    ##########################################################################################################################################
    ------------------------------------------------------------------------------------------------------------------------------------------
'''

def D():
    '''
        Google Code Jam
        Year 2015
        Problem D
    '''
    f = open('C:\Python\CodeJam\CodeJam 2015\D-small-attempt1.in', 'r')
    output = open('C:\Python\CodeJam\CodeJam 2015\D-small-result.txt', 'w')
    cases = int(f.readline())
    for case in range(cases):
        result = 'Case #' + str(case + 1) + ': '
        X, R, C = map(int, f.readline().split())
        grid = R * C
        if X > grid:
            result += 'RICHARD'
        elif X == grid:
            if X > 2:
                result += 'RICHARD'
            else:
                result += 'GABRIEL'
        else:
            if X > 3 and X in (R, C) and 2 in (R, C):
                result += 'RICHARD'
            elif grid % X == 0:
                result += 'GABRIEL'
            else:
                result += 'RICHARD'
        output.write(result + '\n')
    output.close()
    f.close()
