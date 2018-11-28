import sys

def solve(infd,outfd,case):
    indata = infd.readline()
    solution = [int(ch) for ch in indata if ch != '\n']
    size = len(solution)
    index = 0
    while index<size-1:
        if solution[index]<=solution[index+1]:
            index += 1
        else:
            while index>0 and solution[index] == 0:
                index -=1
            number = solution[index]
            number -= 1
            solution[index]=number
            for i in range(len(solution[index+1:])):
                solution[index+i+1] = 9
            if index > 0:
                index -= 1
    ret = "%i" * len(solution)
    ret = ret % tuple(solution)
    ret =str(int(ret))
    output = 'Case #%i: ' % (case)
    print (output+ret,file=outfd)
        

if __name__=="__main__":
    program, filename, stdout = sys.argv
    inf = open(filename,'r')

    N = int(inf.readline())

    outf = sys.stdout
    if stdout == 'final':
        outputfilename = filename.replace('in','out')
        outf = open(outputfilename,'w')
    
    for case in range(N):
        solve(inf,outf,case+1)
