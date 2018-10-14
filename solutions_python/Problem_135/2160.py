fh = open("a.in",'r')
fhw = open("b.txt",'w')
f = fh.readlines()
cases = int(f[0].strip())
Casedir = {}
count = 1
for i in range(0,cases):
    Casedir["Case #" + str(i+1)] = []
    for j in range(0,10):
        Casedir["Case #" + str(i+1)].append(f[count].strip())
        count += 1
Keys = list(Casedir.keys())
Keys.sort()
for k in Keys:
    l1 = (Casedir[k][int(Casedir[k][0])]).split(" ")
    l2 = (Casedir[k][5 + int(Casedir[k][5])]).split(" ")
    print(l1)
    print(l2)
    Decision = [value for value in l1 if value in l2]
    length = len(Decision)
    if length == 0:
        fhw.write(k + ": Volunteer cheated!\n")
    elif length == 1:
        fhw.write(k + ": " + Decision[0] + "\n")
    else:
        fhw.write(k + ": Bad magician!\n")
fh.close()
fhw.close()
