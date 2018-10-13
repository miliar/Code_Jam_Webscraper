def main():
    file1 = open('A-large.in')
    lines = file1.read().split('\n')[1:-1]
    file1.close()
    file1 = open('A-large.out', 'w')
    for case in range(len(lines)):
        inpt = lines[case].split(' ')[1]
        lst = [int(inpt[i]) for i in range(len(inpt))]
        numExtra = 0
        for i in range(len(lst) - 1, 0, -1):
            toLeft = sum(lst[:i]) + numExtra
            if toLeft > (i - 1):
                continue
            numExtra += i - toLeft
        file1.write('Case #%d: %d\n'%(case + 1, numExtra))
    file1.close()

main()