'''
    ------------------------------------------------------------------------------------------------------------------------------------------
    ##########################################################################################################################################
    ------------------------------------------------------------------------------------------------------------------------------------------
'''

def A():
    '''
        Google Code Jam
        Year 2015
        Problem A
    '''
    f = open('C:\Python\CodeJam\CodeJam 2015\A-small-attempt1.in', 'r')
    output = open('C:\Python\CodeJam\CodeJam 2015\A-small-practice-result.txt', 'w')
    cases = int(f.readline())
    for case in range(cases):
        result = 'Case #' + str(case + 1) + ': '
        line = f.readline().split()
        N = int(line[0])
        string = line[1]
        persons = 0
        persons_required = 0
        for k in range(N + 1):
            if k > persons and string[k] != '0':
                persons_required += k - persons
                persons += persons_required
            persons += int(string[k])
        result += str(persons_required)
        output.write(result + '\n')
    output.close()
    f.close()
