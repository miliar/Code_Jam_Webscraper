import sys

root = 'C:\\Users\\davedave\\Downloads'
problemLetter = 'A'
infile = '{}\\{}-{}.in'.format(root, problemLetter, 'large')
#infile = '{}\\test.in'.format(root)
outfile = infile.replace('.in', '.out')

if __name__ == '__main__':
    with open(infile, 'r') as fin, open(outfile, 'w') as fout:
        for case in range(int(fin.readline())):
            pancakeString, flipperSizeString = (s for s in fin.readline().split(' '))
            flipperSize = int(flipperSizeString)
            flipCount = 0
            pancakeChars = list(pancakeString)
            for i in range(len(pancakeChars)):
                if pancakeChars[i] == '-':
                    # need to flip flipperSize pancakes starting here -- if we can't, impossible
                    endIndexForFlip = i + flipperSize - 1
                    if endIndexForFlip >= len(pancakeChars):
                        msg = 'Case #{}: {}'.format(1 + case, "IMPOSSIBLE")
                        print(msg)
                        fout.write(msg + '\n')
                        break

                    # perform flip
                    for j in range(i, endIndexForFlip+1):
                        if pancakeChars[j] == '-':
                            pancakeChars[j] = '+'
                        else:
                            pancakeChars[j] = '-'
                    flipCount+=1

            if '-' not in pancakeChars:
                msg = 'Case #{}: {}'.format(1 + case, flipCount)
                print(msg)
                fout.write(msg + '\n')