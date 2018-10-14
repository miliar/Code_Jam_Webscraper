'''
@author: Peratham
'''

INPUTFILE = 'C-small-attempt0.in'
OUTPUTFILE = 'C-small-attempt0.out'
#INPUTFILE = 'C-toy.in'
#OUTPUTFILE = 'C-toy.out'

def readFile():
    file = open(INPUTFILE, 'r')
    text = file.readline()
    tmp = text.split()
    P = tmp[0]
    
    param = {}
    param['T'] = int(P)
    input = []
    
    text = file.readlines()
    for line in text:
        tmp = line.split()
        input.append(tmp)
    
    file.close()
    del file
    return [param, input]

def shiftNum(num,start,end):
    count = 0
    snum = str(num)
    n = len(snum)
    for i in xrange(1,n):
        newnum = snum[i:] + snum[:i]
        newnumm = int(newnum)
        if newnumm > num and newnumm >= start and newnumm <= end and len(str(newnumm)) == n:
            count += 1
#            print num, newnum
    return count

def solve(param, input):
    ans = []
    
    for i in xrange(param['T']):
        start = int(input[i][0])
        end = int(input[i][1])
        count = 0
        for j in xrange(start,end):
            count += shiftNum(j,start,end)
        ans.append(count)
    return ans

def writeFile(ans):
    file = open(OUTPUTFILE, 'w')
    file.write("Case #1: %d\n" % ans[0])
    file.close()
    
    file = open(OUTPUTFILE, 'a')
    for i in xrange(len(ans) - 1):
        file.write("Case #%d: %d\n" % ((i + 2), ans[(i + 1)]))
        
    file.close()

def main():
    [param, input] = readFile()
    ans = solve(param, input)
    writeFile(ans)

if __name__ == '__main__':
    main()
