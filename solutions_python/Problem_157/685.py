__author__ = 'Xapheus'

#New to python

qTable = (("1", "i", "j", "k"),
          ("i", "-1", "k", "-j"),
          ("j", "-k", "-1", "i"),
          ("k", "j", "-i", "-1"))
qOperands = ("1", "i", "j", "k")


def mult_quarternion(a, b):
    negative = False
    if a[0] == '-':
        negative = True
        a = a[1]
    if b[0] == '-':
        negative = not negative
        b = b[1]
    ret_string = qTable[qOperands.index(a)][qOperands.index(b)]
    if negative:
        if ret_string[0] == '-':
            return ret_string[1]
        else:
            return "-" + ret_string
    else:
        return ret_string

f = open("C-small-attempt5.in", 'r')
o = open("output.txt", 'w')
num_cases = int(f.readline())

for i in range(num_cases):
    stringProperties = list(map(int, f.readline().split(' ')))
    inputStringLength = stringProperties[0]
    repeats = stringProperties[1]
    string = f.readline()

    i_flag, j_flag = False, False

    #find product of "string"
    #multiply substring "repeats" times
    a = string[0]
    for j in range(1, inputStringLength*repeats):
        if a=="i": #encountered "i"
            i_flag = True
        elif a == "k" and i_flag: #encountered "ij"
            j_flag = True
        a = mult_quarternion(a, string[j%inputStringLength])

    if i_flag and j_flag and a == "-1": # encountered "ijk"
        print("Case #" + str(i + 1) + ": YES\n")
        o.write("Case #" + str(i + 1) + ": YES\n")
    else:
        o.write("Case #" + str(i + 1) + ": NO\n")
        print("Case #" + str(i + 1) + ": NO\n")

f.close()
o.close()