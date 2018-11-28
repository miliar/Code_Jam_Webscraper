#!/bin/env python3

T=0
test_case_no = 1
counter=0
a=""
b=[]

f = open("result_large.txt", "w")

for line in open("A-large.in"):
    if T == 0:
        T = int(line)

    else:
        if line[0] != "\n":
            a += line.rstrip("\n")
            #print(a)

            counter += 1

            if counter == 4:
                b.append((a[0], a[1], a[2], a[3]))
                b.append((a[4], a[5], a[6], a[7]))
                b.append((a[8], a[9], a[10], a[11]))
                b.append((a[12], a[13], a[14], a[15]))
                b.append((a[0], a[4], a[8], a[12]))
                b.append((a[1], a[5], a[9], a[13]))
                b.append((a[2], a[6], a[10], a[14]))
                b.append((a[3], a[7], a[11], a[15]))
                b.append((a[0], a[5], a[10], a[15]))
                b.append((a[3], a[6], a[9], a[12]))
                #print(b)

                x_win = 0
                o_win = 0
                not_complited = 0
                for c in b:
                    #print(c)
                    if c.count("X") == 4 or (c.count("X") == 3 and "T" in c):
                        x_win = 1
                        break
                    elif c.count("O") == 4 or (c.count("O") == 3 and "T" in c):
                        o_win = 1
                        break
                    elif "." in c:
                        not_complited = 1

                if x_win == 1:
                    f.write("Case #{0}: X won\n".format(test_case_no))
                elif o_win == 1:
                    f.write("Case #{0}: O won\n".format(test_case_no))
                elif not_complited == 1:
                    f.write("Case #{0}: Game has not completed\n".format(test_case_no))
                else:
                    f.write("Case #{0}: Draw\n".format(test_case_no))


        else:
            test_case_no += 1
            counter=0
            a=""
            b=[]

f.close()

