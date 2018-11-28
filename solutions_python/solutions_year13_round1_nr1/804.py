import math

def paint_cost(r):
    return (r+1)**2 - r**2

def answer(r, t):
    rings = 0
    running = True
    while running:
        t = t - paint_cost(r)
        if t >= 0:
            rings += 1
        else:
            running = False
        r += 2
    return rings




def codejam_read(filen):
    f = open(filen,'r')
    fout = open(filen[:-2] + "out", 'w')
    case_num = 0
    test_size = f.readline()

    for line in f:
        case_num += 1
        radius, paint = line.split(" ")
        # fout.write("Case #{0}: {1}\n".format(case_num,answer(line)))
        # print("Case #{0}: {1}\n".format(case_num,answer(int(radius), int(paint))))
        fout.write("Case #{0}: {1}\n".format(case_num,answer(int(radius), int(paint))))

    fout.close()
    f.close()



codejam_read('A-small-attempt0.in')