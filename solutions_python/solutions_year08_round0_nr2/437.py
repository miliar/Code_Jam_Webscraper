
import datetime


def turnaroundLater(timestr, turnaround):
    return (datetime.datetime.strptime(timestr,'%H:%M') +
        datetime.timedelta(minutes=turnaround)).strftime('%H:%M')

if True:
    filebase = 'B-small-attempt5'
    input = file(filebase + '.in').read().split('\n')
    N = int(input[0])
    
    index = 1
    for i in range(N):
        T = int(input[index]); index += 1
        NA, NB = tuple(map(int, input[index].split(' '))); index += 1
        print T,NA,NB
        
        schedA = map(str.split, input[index:index+NA]); index += NA
        schedB = map(str.split, input[index:index+NB]); index += NB
        
        leaveA = map(lambda s: s[0], schedA); leaveA.sort()
        leaveB = map(lambda s: s[0], schedB); leaveB.sort()
        arrivalA = map(lambda s: s[1], schedB); arrivalA.sort()
        arrivalB = map(lambda s: s[1], schedA); arrivalB.sort()
        
        connectsA, connectsB = [], []
        
        for la in leaveA:
            ci = 0
            for aa in arrivalA:
                if sum(map(lambda (i,l): i == ci, connectsA)) > 0:
                    ci += 1
                    continue
                if la >= turnaroundLater(aa, T):
                    connectsA += [(ci, la)]
                    break   
                ci += 1
        for lb in leaveB:
            ci = 0
            for ab in arrivalB:
                if sum(map(lambda (i,l): i == ci, connectsB)) > 0:
                    ci += 1
                    continue
                if lb >= turnaroundLater(ab, T):
                    connectsB += [(ci, lb)]
                    break
                ci += 1
        print connectsA, connectsB
        
        
        output = 'Case #%d: %d %d' % (i+1, len(schedA) - len(connectsA), len(schedB) - len(connectsB))
        file(filebase + '.out','a').write(output + '\n')
        print output
        
        
