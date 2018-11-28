T = int(raw_input())

for i in range(T):
        line = raw_input().split()
        N = int(line[0])
        movements = line[1:]
        mv = []
        for j in range(0, len(movements), 2):
                if movements[j] == 'O':
                        mv.append([int(movements[j+1]), None])
                else:
                        mv.append([None, int(movements[j+1])])
        opos = 1
        bpos = 1
        ot = 0
        bt = 0
        t = 0
        for j in range(len(mv)):
                if mv[j][0]:
                        dt = max(abs(mv[j][0] - opos) + 1 - ot, 1)
                        opos = mv[j][0]
                        ot = 0
                        bt += dt
                        t += dt
                else:
                        dt = max(abs(mv[j][1] - bpos) + 1 - bt, 1)
                        bpos = mv[j][1]
                        bt = 0
                        ot += dt
                        t += dt
        output = "Case #" + str(i+1) + ": " + str(t)
        print output



        
