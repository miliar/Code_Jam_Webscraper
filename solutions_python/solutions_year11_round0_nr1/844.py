import os

if __name__ == "__main__": 
    f = open('A-large.in', 'r')
    fo = open('A-large.out', 'w')
    T = int(f.readline())
    
    for i in range(0, T):
        case = f.readline().split()
        N = case[0]
        robots = case[1::2]
        buttons = map(int, case[2::2])
        
        opos, otime = 1, 0
        bpos, btime = 1, 0
        time = 0
        for r, b in zip(robots, buttons):
            if r == 'O':
                t = max(0, abs(b - opos)- otime) + 1;
                opos = b
                btime += t
                otime = 0
                time += t
            else:
                t = max(0, abs(b - bpos)- btime) + 1;
                bpos = b
                otime += t
                btime = 0
                time += t
                
        fo.write('Case #' + str(i + 1) + ': ' + str(time) + '\n')
    f.close()
    fo.close()
