'''
Google Code Jam 2017 Qualification Round
Problem B. Tidy Numbers
Solution by Liu Yue <euyuil@gmail.com>
Created at 2017-04-08T23:15:00+0800
'''

def calc(numstr):
    '''
    Calculate the largest tidy number le numstr.
    '''
    w = 0
    for i in range(0, len(numstr)-1):
        if numstr[w] < numstr[i]:
            w = i
        if numstr[i] > numstr[i+1]:
            left = None
            if numstr[w] == '1':
                left = ''
            else:
                left = numstr[:w] + chr(ord(numstr[w]) - 1)
            right = '9' * (len(numstr) - w - 1)
            return left + right
    return numstr

def main():
    '''
    The main method for the program.
    '''
    with open('B-large.in') as fin, open('B-large.out', 'w') as fout:
        fin.readline()
        curr = 1
        for line in fin:
            res = calc(line.rstrip())
            fout.write('Case #%d: %s\n' % (curr, res))
            curr = curr + 1

if __name__ == '__main__':
    main()
