#!/usr/bin/python

fname = "A-small-attempt0.in"
with open(fname) as f:
    content = f.readlines()

m1 = []
m2 = []

n_case = 1

out_file = open("A-small-attempt0.out","w+")

def elabora(scelta1, m1, scelta2, m2):
    riga1 = m1[scelta1-1].rstrip("\n").split(" ")
    riga2 = m2[scelta2-1].rstrip("\n").split(" ")

    carta_scelta = -1

    numero_scelte = 0
    for r in riga1:
        if r in riga2:
            numero_scelte += 1
            carta_scelta = r

    global n_case

    if numero_scelte == 0:
        out =  "Case #%d: Volunteer cheated!" % n_case
    elif numero_scelte == 1:
        out =  "Case #%d: %s" % (n_case, str(carta_scelta))
    else:
        out = "Case #%d: Bad magician!" % n_case

    out_file.write(out + "\n")
    n_case += 1


for i, line in enumerate(content):
    if i == 0:
        tests = line[0]

    if (i-1) % 10 == 0:
        scelta1 = int(line[0])

    elif (i-1) % 10 == 1:
        m1.append(line)
    elif (i-1) % 10 == 2:
        m1.append(line)
    elif (i-1) % 10 == 3:
        m1.append(line)
    elif (i-1) % 10 == 4:
        m1.append(line)
    elif (i-1) % 10 == 5:
        scelta2 = int(line[0])
    elif (i-1) % 10 == 6:
        m2.append(line)
    elif (i-1) % 10 == 7:
        m2.append(line)
    elif (i-1) % 10 == 8:
        m2.append(line)
    elif (i-1) % 10 == 9:
        m2.append(line)


        if i != 0:
            '''
            print
            print
            print "test: %s" % tests
            print "m1: "
            print m1
            print
            print "m2: "
            print m2
            '''
            elabora(scelta1, m1, scelta2, m2)

        m1 = []
        m2 = []



out_file.close()
