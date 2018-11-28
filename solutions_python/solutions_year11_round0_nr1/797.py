#!/usr/bin/python


def test():
    print "Hello"
    return




out = open('output.dat','w')
f = open('o.test','r')

O = dict()
B = dict()
l = f.readline()

for i in range(0,int(l)):
    case = f.readline()
    case = case.split();
    n = case[0]
    O['loc'] = 1
    B['loc'] = 1
    O['time'] = 0
    B['time'] = 0
    for k in range(0,int(n)):
        if case[2*(k)+1]== 'O':
            target = int(case[2*k+2])
            wait = B['time']
            dist = abs(target - O['loc'])
            if dist+O['time'] >= wait:
                O['loc'] = target
                O['time'] = O['time'] + dist + 1
            else:
                O['loc'] = target
                O['time'] = wait + 1
        if case[2*(k)+1]== 'B':
            target = int(case[2*k+2])
            wait = O['time']
            dist = abs(target - B['loc'])
            if dist+B['time'] >= wait:
                B['loc'] = target
                B['time'] = B['time'] + dist + 1
            else:
                B['loc'] = target
                B['time'] = wait + 1
        
    if B['time']>O['time']:
        out.write('Case #' + str(i+1) + ': '+str(B['time'])+'\n')
    else:
        out.write('Case #' + str(i+1) + ': '+str(O['time'])+'\n')
    

f.closed






