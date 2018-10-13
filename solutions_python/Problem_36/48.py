'''
Created on Sep 3, 2009
@author: namnx
'''

INFILE = 'welcome-large.in'
OUTFILE = 'welcome-large.out'

def countSubStr(message, s):
    a = []
    for i in range(len(s)):
        a.append([])
        for j in range(len(message)):
            a[i].append(0)
    
    if message[0] == s[0]: a[0][0] = 1
    for i in range(1, len(message)):
        a[0][i] = a[0][i-1]
        if message[i] == s[0]:
            a[0][i] += 1
    
    for i in range(1, len(s)):
        for j in range(1, len(message)):
            a[i][j] = a[i][j-1]
            if s[i] == message[j]:
                a[i][j] += a[i-1][j-1]
    return a[len(s)-1][len(message)-1]       


def main():
    fin = file(INFILE,'r')
    fout = file(OUTFILE, 'w')
    n = int(fin.readline().strip())
    for i in range(n):
        line = fin.readline()
        count = countSubStr(line, 'welcome to code jam')
        count = count % 10000
        strCount = str(count)
        for j in range(4 - len(strCount)):
            strCount = '0' + strCount
        fout.write('Case #' + str(i+1) +': ' + strCount + '\n')
    fin.close()
    fout.close()
    return


if __name__ == '__main__':
    main()
