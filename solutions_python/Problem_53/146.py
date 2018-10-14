on = 'ON'
off = 'OFF'
f = open("A-large.in")
case = int(f.readline())
string = ''
for k in range(case):
    item = f.readline().rstrip("\n")
    i = item.split()
    snap = int(i[1])
    switch = int(i[0])
    link = 2**switch
    if (snap % link) == (link - 1):
        string += "Case #" + str(k+1) + ": ON\n"
    else:
        string += "Case #" + str(k+1) + ": OFF\n"
o = open('A-large-out.in', 'w')
o.write(string)
o.close()
