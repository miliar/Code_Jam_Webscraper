pancake_rows = []
pancake_ints=[]
k= []
output=open('output.in', 'w+')
dataFile = open("A-large.in", 'r')
rows = dataFile.readline()
for line in dataFile:
    pancake_rows.append(line.split(" ")[0])
    k.append(int(line.split(" ")[1]))


for i in range(len(pancake_rows)):
    print i
    row=pancake_rows[i]
    pancake_ints.append([])
    for j in range(len(row)):
        pancake = row[j]
        if pancake == '-':
            pancake_ints[i].append(-1)
        else:
            pancake_ints[i].append(1)

print pancake_ints

for i in range(len(pancake_ints)):
    row = pancake_ints[i]
    total=0
    for j in range(len(row)):
        pancake = row[j]
        if pancake == -1:
            if j+k[i] > len(row):
                total=-1
            else:
                total=total+1
                for m in range(k[i]):
                    row[j+m]=row[j+m]*(-1)
    output.write('Case #'+str(i+1)+': ')
    if total == -1:
        output.write('IMPOSSIBLE')
    else:
        output.write(str(total))
    output.write('\n')
    print total

# for i in range(len(pancake_rows)):
#     row = pancake_rows[i]
#     total = 0;
#     for pancake in row:
#         if pancake== -1:
#             total=total+1
#             for j in range(k[i]):
#                 if i+j-1 > len(row):
#                     total=-1
#                 else:
#                     row[i+j-1]=row[i+j-1]*(-1)
#     print total


print pancake_rows
print k
