#!/usr/bin/env python

def main():
    fin = open('A-large.in', 'r')
    fout = open('out.out', 'w')
    T = int(fin.readline().strip('\n'))
    for casenum in range(1, T+1):
        fout.write('Case #%d:\n' % (casenum))
        N = int(fin.readline().strip('\n'))
        chart = []
        for x in range(N):
            chart.append(list(fin.readline().strip('\n')))
        OWPL = []
        for x in range(N):
            games = N-1
            avg = 0.0
            for y in range(N):
                wins = 0.0
                losses = 0.0
                if y == x:
                    pass
                else:
                    for z in range(N):
                        if chart[y][x] == '.':
                            games -= 1
                            break
                        elif z == x:
                            pass
                        elif chart[y][z] == '0':
                            losses += 1
                        elif chart[y][z] == '1':
                            wins += 1
                    if not wins == losses == 0:
                        avg += wins/(wins+losses)
            avg /= (games)
            OWPL.append(avg)
        
        for x in range(N):
            wins = 0.0
            losses = 0.0
            for game in chart[x]:
                if game == '0':
                    losses += 1
                elif game == '1':
                    wins += 1
            WP = wins/(wins+losses)
            OOWP = 0
            games = N-1
            for y in range(N):
                if y == x:
                    pass
                elif chart[y][x] == '.':
                    games -= 1
                    pass
                else:
                    OOWP += OWPL[y]
            OOWP /= (games)
                        
            RPI = (.25*WP) + (.5*OWPL[x]) + (.25*OOWP)
            RPI = str(RPI).rstrip('0')
            fout.write('%s\n' % (RPI))

    fin.close()
    fout.close()

if __name__ == '__main__':
    main()