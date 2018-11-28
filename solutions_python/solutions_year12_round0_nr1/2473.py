__author__ = 'Mantas'

dictstr = "ynficwlbkuomxsevzpdrjgthaq"

f = open("C:/Users/Mantas/Desktop/A-small.in", "r")
f_out = open("C:/Users/Mantas/Desktop/A-small.out", "w")
num = int(f.readline())

for i in range(0, num):
    string = f.readline()
    outstr = ""
    for j in range(0, len(string)):
        if string[j] == " ":
            outstr += " "
            continue
        outstr += chr(ord('a') + dictstr.find(string[j]))
    f_out.write("Case #" + str(i + 1) + ": " + outstr + "\n")
f_out.close()
