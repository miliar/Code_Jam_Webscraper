import sys


def parseCase(fin):
    line = next(fin).strip()
    D, N = map(int, line.split(' '))
    horses = []
    for i in range(N):
        line = next(fin).strip()
        Ki, Si = map(int, line.split(' '))
        horses.append( (Ki, Si) )
    return D, horses


def solve(D, horses):
    slowestHorseTime = 0
    for (Ki, Si) in horses:
        if Ki>=D: continue
        horseTime = (D-Ki)/Si
        slowestHorseTime = max(horseTime, slowestHorseTime)
    return D/slowestHorseTime


def main(filenameIn, filenameOut):
    with open(filenameIn, 'rt') as fin, open(filenameOut, 'wt') as fout:
        line = next(fin).strip()
        count = int(line)
        for i in range(count):
            D, horses = parseCase(fin)
            answer = solve(D, horses)
            fout.write("Case #{}: {:.8}\n".format(i+1, answer))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
