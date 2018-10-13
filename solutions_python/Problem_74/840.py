import sys, math
from multiprocessing import Pool

def main(line):
    time = 0
    d = line.split()
    n = int(d[0])
    data = [(d[i], int(d[i+1])) for i in range(1, len(d), 2)]
    pos = {"O":1, "B":1}

    lastbot = None
    movetime = 0
    for bot, button in data:
        if lastbot is None:
            lastbot = bot
            
        if lastbot == bot:
            movetime += math.fabs(button - pos[bot]) + 1
        else:
            time += movetime
            movetime = max(math.fabs(button - pos[bot]) - movetime, 0) + 1
        lastbot = bot
        pos[bot] = button
    time += movetime
    
    return time

if __name__ == "__main__":
    f = open(sys.argv[1])
#    f = open("test.txt")
    T = int(f.readline())
    data = []
    for i in range(T):
        data.append(f.readline().strip())
    
    pool = Pool()
    r = pool.map(main, data)
#    r = map(main, data)
    for i in range(T):
        print "Case #%d: %d" % (i+1, r[i]) 