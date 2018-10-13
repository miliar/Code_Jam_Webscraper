numbers = []
pancake_ints=[]
k= []
output=open('output.in', 'w+')
dataFile = open("B-large.in", 'r')
rows = dataFile.readline()
for line in dataFile:
    numbers.append(line.split("\n")[0])


for i in range(len(numbers)):
    print i
    digits=list(numbers[i])
    done=0
    while done == 0:
        done=1
        for j in range(1,len(digits)):
            if(int(digits[j])<int(digits[j-1])):
                done=0
                digits[j-1]=str(int(digits[j-1])-1)
                for k in range(j,len(digits)):
                    digits[k]='9'
    print digits
    output.write('Case #'+str(i+1)+': ')
    leading_zeros=1
    for digit in digits:
        if not(leading_zeros==1 and digit=='0'):
            leading_zeros=0
            output.write(digit)
    output.write('\n')
#     if total == -1:
#         output.write('IMPOSSIBLE')
#     else:
#         output.write(str(total))
#     output.write('\n')
#     print total

# for i in range(len(pancake_ints)):
#     row = pancake_ints[i]
#     total=0
#     for j in range(len(row)):
#         pancake = row[j]
#         if pancake == -1:
#             if j+k[i] > len(row):
#                 total=-1
#             else:
#                 total=total+1
#                 for m in range(k[i]):
#                     row[j+m]=row[j+m]*(-1)
#     output.write('Case #'+str(i+1)+': ')
#     if total == -1:
#         output.write('IMPOSSIBLE')
#     else:
#         output.write(str(total))
#     output.write('\n')
#     print total

