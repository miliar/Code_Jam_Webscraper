_case = 0
def gout(s):
    global _case
    _case += 1
    print "Case #%d: %s" % (_case,s) 

def memoize(f):
    dict = {}
    def func(*n):
        if n in dict:
            return dict[n]
        else:
            dict[n] = f(*n)
            return dict[n]
    return func

for _ in xrange(int(raw_input())):
    time = {'O':0, 'B':0}
    pos = {'O':1, 'B':1}
    
    line = raw_input().split()[1:]
    oldBot = line[0]
    for i in xrange(0,len(line),2):
        curBot, curButton = line[i], int(line[i+1])
        time[curBot] += 1 + abs(curButton - pos[curBot])
        pos[curBot] = curButton
        if curBot!=oldBot:
            if time[oldBot] >= time[curBot]:
                time[curBot] = time[oldBot]+1
        oldBot = curBot
    gout(max(time['O'],time['B']))
