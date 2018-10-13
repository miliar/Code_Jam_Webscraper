def run(dancers, nrSup, score):
    nrOver = 0

    for d in dancers:
        if d >= max(score*3 - 2, score):
            nrOver = nrOver + 1
        elif nrSup > 0 and d >= max(score*3 - 4, score):
            nrSup = nrSup - 1
            nrOver = nrOver + 1

    return nrOver

def main():
    fin = open('B-large.in', 'r')
    fout = open('B-large.out','w')
    numOfCases = int(fin.readline())

    for case in range(numOfCases):      
        values = fin.readline().split(' ')
        nrOver = run([int(n) for n in values[3:]], int(values[1]), int(values[2]))
        result = "Case #" + repr(case+1) + ": " + repr(nrOver) + "\n"
        fout.write(result)

    fin.close()
    fout.close()

main()
