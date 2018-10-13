'''
Created on 2017-04-08

@author: qiuyx
'''


def gettidy(numstr):
    length = len(numstr)
    for i in xrange(length-1):
        if int(numstr[i]) >= int(numstr[i+1]):
            return int(numstr[:i] + str(int(numstr[i])-1) + '9'*(length-i-1))
    return numstr


if __name__ == '__main__':
    # read file:
    
    file_in = open('H:/B-small-attempt0.in')
    file_out = open('H:/small_output.out', 'w')
    T = int(file_in.readline()[:-1])
    for i in xrange(T):
        N = (file_in.readline())[:-1]
        res = 'Case #' + str(i) + ': ' + str(gettidy(N))
        file_out.write(str(res)+'\n')
        print res

    file_out.close()
    file_in.close()
    '''
    s = '7'
    s = gettidy(s)
    print s
    '''