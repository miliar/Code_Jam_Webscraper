# Google Code Jam 2014 Qualification Round
# Problem A
# Shaotong Wang

fin = open('A_test.in', 'r')
fout = open('A_test.out', 'w')

num_cases = int(fin.readline())

for case in range(1,num_cases+1):
    fst_row_num = int(fin.readline())
    fst_row = 0
    for x in range(1,5):
        if x == fst_row_num:
            fst_row = fin.readline()
        else:
            fin.readline()
    fst_row = fst_row.split()
    fst_row = set(fst_row)

    snd_row_num = int(fin.readline())
    snd_row = 0
    for x in range(1,5):
        if x == snd_row_num:
            snd_row = fin.readline()
        else:
            fin.readline()
    snd_row = snd_row.split()
    snd_row = set(snd_row)

    fout.write("Case #" + str(case) + ": ")
    if len(fst_row & snd_row) == 1:
        fout.write((fst_row & snd_row).pop())
    elif len(fst_row & snd_row) == 0:
        fout.write("Volunteer cheated!")
    else:
        fout.write("Bad magician!")
    fout.write("\n")

fin.close()
fout.close()

