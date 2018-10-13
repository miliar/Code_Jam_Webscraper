__author__ = 'muhammadkhadafi'


def who_won(omino, gridx, gridy):

    longer_axis = gridx
    shorter_axis = gridy
    if gridy > gridx:
        longer_axis = gridy
        shorter_axis = gridx

    if (gridx * gridy) % omino != 0:
            return "RICHARD"
    else:
        if omino == 1 or omino == 2:
            return "GABRIEL"
        elif omino == 3:
            if longer_axis == 3 and shorter_axis == 1:
                return "RICHARD"
            else:
                return "GABRIEL"
        else:
            if longer_axis == 4 and shorter_axis == 3:
                return "GABRIEL"
            elif longer_axis == 4 and shorter_axis == 4:
                return "GABRIEL"
            else:
                return "RICHARD"


f_in = open('D-small-attempt1.in', 'r')
f_out = open('output4small.txt', 'w')
cases = int(f_in.readline().rsplit()[0])
for i in range(1, cases+1):
    ominos = f_in.readline().rsplit()
    f_out.write("case #" + str(i) + ": " + str(who_won(int(ominos[0]), int(ominos[1]), int(ominos[2]))))
    if i < cases:
        f_out.write('\n')
f_in.close()
f_out.close()