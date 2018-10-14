'''Welcome to my program'''

fil=open('D:\\temp\\C-small-attempt1.in')

N=int(fil.readline()[:-1])

txt='welcome to code jam'
def calculate(line, ind=0):
    '''To determine how many ways there are'''
    nc=0
    if ind>=len(txt):
        return 1
    for i in xrange(len(line)):
        if line[i]==txt[ind]:
            nc+=calculate(line[i+1:], ind+1)
            nc%=1000
    return nc
    
out=open('D:\\temp\\output.txt', 'w')
for i in xrange(N):
    line=fil.readline()
    res=str(calculate(line))
    if len(res)<4:
        res='0'*(4-len(res))+res
    out.write('Case #%s: %s\n'%(i+1, res))
out.close()

