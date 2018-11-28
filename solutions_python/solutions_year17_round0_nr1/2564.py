'''
Created on 2017-04-08

@author: qiuyx
'''

def flip(row, start, end):
    if row is None:
        return None
    for i in xrange(start, end):
        if row[i] == '+':
            row[i] = '-'
        elif row[i] == '-':
            row[i] = '+'
        else:
            print 'Invalid Character!'

def solve(s, k, cno):
    row = list(s)
    counts = 0
    result = 'Case #' + str(cno) +': '
    for i in range(len(row)-k+1):
        if row[i] == '-':
            flip(row, i, i+k)
            counts += 1

    if '-' not in row:
        result += str(counts)
    else:
        result +='IMPOSSIBLE'
    return result 

if __name__ == '__main__':
    # read file:
    file_in = open('H:/A-small-attempt1.in')
    file_out = open('H:/small_output.out', 'w')
    T = int(file_in.readline()[:-1])
    for i in xrange(T):
        line = (file_in.readline())[:-1]
        case = (line).split(' ')
        s = case[0]
        k = int(case[1])
        res = solve(s, k, i+1)
        file_out.write(res+'\n')
        print res

    file_out.close()
    file_in.close()
