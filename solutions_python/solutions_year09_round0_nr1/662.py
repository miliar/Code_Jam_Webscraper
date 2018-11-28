import re

file_in = open("entrada2.in")
file_out = open("salida2.out",'w')

options = file_in.readline().split()
print options
data = []

for i in range(int(options[1])):
    data.append(file_in.readline().strip())

for index in range(int(options[2])):
    total = 0
    regla = file_in.readline().strip()
    regla = re.sub("\(","[",regla)
    regla = re.sub("\)","]",regla)
    for item in data:
        # print "regla: %s, data: %s" % (regla, data)
        if re.match(regla,item):
            total += 1
    file_out.write("Case #%s: %s\n" % (index+1,total))

file_out.close()
