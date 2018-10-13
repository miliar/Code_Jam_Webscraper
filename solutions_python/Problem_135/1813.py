#!/usr/bin/python2.7

def process_testcase(cn, f, fout):
    answer1 = int(f.readline())

    rows1 = []
    rows1.append(f.readline().strip().split(" "))
    rows1.append(f.readline().strip().split(" "))
    rows1.append(f.readline().strip().split(" "))
    rows1.append(f.readline().strip().split(" "))

    answer2 = int(f.readline())

    rows2 = []
    rows2.append(f.readline().strip().split(" "))
    rows2.append(f.readline().strip().split(" "))
    rows2.append(f.readline().strip().split(" "))
    rows2.append(f.readline().strip().split(" "))

    #print answer1, answer2

    v = set.intersection(set(rows1[answer1-1]), set(rows2[answer2-1]))

    if len(v) == 1:
        fout.write("Case #"+str(cn)+": " + str(v.pop()) + "\n")
    elif len(v) == 0:
        fout.write("Case #"+str(cn)+": Volunteer cheated!" + "\n")
    elif len(v) > 1:
        fout.write("Case #"+str(cn)+": Bad magician!" + "\n")


f = open("QualProblemA.in")
fout = open("QualProblemA.out", "w")

amountTestcases = int(f.readline())

for i in range(0, amountTestcases):
    process_testcase(i+1, f, fout)