i = open("D-small-attempt3.in", 'r')

f = open('outDD.txt', 'w')



num_case = i.readline()

num_case = int(num_case)



for case in range(1, num_case + 1):

    case = str(case)

    line = i.readline()

    line = line.split()

    area = int(line[1]) * int(line[2])

    omino = int(line[0])

    if omino == 1:

        f.write("Case #" + case + ": " + "GABRIEL" + "\n")

    elif omino == 2:

        if area % omino == 0:

            f.write("Case #" + case + ": " + "GABRIEL" + "\n")

        else:

            f.write("Case #" + case + ": " + "RICHARD" + "\n")

    elif omino == 3:

        if area % omino == 0:

            if area == 3:

                f.write("Case #" + case + ": " + "RICHARD" + "\n")

            else:

                f.write("Case #" + case + ": " + "GABRIEL" + "\n")

        else:

            f.write("Case #" + case + ": " + "RICHARD" + "\n")

    else: #omino == 4

        if area % omino == 0:

            if area == 4 or area == 8:

                f.write("Case #" + case + ": " + "RICHARD" + "\n")

            else:

                f.write("Case #" + case + ": " + "GABRIEL" + "\n")

        else:

            f.write("Case #" + case + ": " + "RICHARD" + "\n")



f.close()
