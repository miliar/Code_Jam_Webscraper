fin = open('D-small-attempt0.in','r')
fout = open('ominoSmall.out','w')

cases = int(fin.readline().strip())

a = 1

while a <= cases:
    data = fin.readline().strip().split(' ')

    ominoSize = int(data[0])
    rows = int(data[1])
    cols = int(data[2])

    if ominoSize < 7 and (rows * cols) % ominoSize == 0 and rows > ominoSize - 2 and cols > ominoSize - 2 :
        fout.write("Case #" + str(a) + ": GABRIEL\n")
    else:
        fout.write("Case #" + str(a) + ": RICHARD\n")
    a+=1
fin.close()
fout.close()
