from sys import stdin, stdout, stderr
from string import rstrip

def nexttask(color, tasks, cur):
    for i in range(len(tasks)):
        if tasks[i][0] == color and i>cur:
            return i
    return -2

def solve(tasks):
    t = 0
    oi = 0
    ol = 1
    od = False
    bi = 0
    bl = 1
    bd = False
    dt = -1
    while dt<len(tasks)-1:
        #stderr.write('### t = '+str(t)+'\n')
        oi = nexttask('O',tasks,dt)
        if oi == -2 and not od:
            od = True
            #stderr.write('## Orange is done\n')
        if not od:
            #stderr.write('## Orange goal: '+str(tasks[oi][1])+'\n')
            if tasks[oi][1] > ol:
                ol += 1
                #stderr.write('## Orange moves forward\n')
            elif tasks[oi][1] < ol:
                ol -= 1
                #stderr.write('## Orange moves backwards\n')
            elif oi==dt+1:
                dt=oi
                #stderr.write('## Orange presses the button at '+str(ol)+'\n')
            else:
                #stderr.write('## Orange waits\n')
                pass
            #stderr.write('## Orange location: '+str(ol)+'\n')
        bi = nexttask('B',tasks,dt)
        if bi == -2 and not bd:
            bd = True
            #stderr.write('## Blue is done\n')
        if not bd:
            #stderr.write('## Blue goal: '+str(tasks[bi][1])+'\n')
            if tasks[bi][1] > bl:
                bl += 1
                #stderr.write('## Blue moves forward\n')
            elif tasks[bi][1] < bl:
                bl -= 1
                #stderr.write('## Blue moves backwards\n')
            elif bi==dt+1 and dt != oi:
                dt=bi
                #stderr.write('## Blue presses the button at '+str(bl)+'\n')
            else:
                #stderr.write('## Blue waits\n')
                pass
            #stderr.write('## Blue location: '+str(bl)+'\n')
        t += 1
        if dt == oi: oi += 1
        if dt == bi: bi += 1
        #stderr.write('## Last task: '+str(dt)+'\n')
    return t

input = []
for line in stdin:
    input.append(rstrip(line,'\n'))

nTestCases = int(input[0])
stderr.write("# %s test cases\n"%nTestCases)

line = 1
while line < len(input):
    tokens = input[line].split(' ')
    N = tokens[0]
    tokens = tokens[1:len(tokens)]
    stderr.write('# Case '+str(line)+'\n')
    stderr.write('# Buttons: '+N+'\n')
    tasks = []
    for i in range(0,int(N)):
        task = tokens[(2*i):(2*i)+2]
        stderr.write('# '+task[0]+' '+task[1]+'\n')
        task[1] = int(task[1])
        tasks.append(task)
    seconds = str(solve(tasks))
    stderr.write('############################\n')
    stdout.write("Case #%s: "%line+str(seconds)+'\n')
    line += 1

