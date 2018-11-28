f = open('A-sample.in', 'r')
T = int(f.readline())
cT = 1

o1 = "our language is impossible to understand"
o2 = "there are twenty six factorial possibilities"
o3 = "so it is okay if you want to just give up"
line_num = 1

conversion = {} # Format is Google letter : real letter

while cT <= T:
    l = f.readline()[:-1]
    for letter_pos in range(len(l)):
        if line_num == 1:
            conversion[l[letter_pos]] = o1[letter_pos]
        elif line_num == 2:
            conversion[l[letter_pos]] = o2[letter_pos]
        elif line_num == 3:
            conversion[l[letter_pos]] = o3[letter_pos]
    line_num += 1
    cT += 1

conversion['z'] = 'q'
conversion['q'] = 'z'

f.close()
f = open('A-small-attempt0.in', 'r')
output = open('Qual-A-Output1.txt', 'w')
T = int(f.readline())

cT = 1
while cT <= T:
   # if cT == T:
        #l = f.readline()
    #else:
    l = f.readline()[:-1]
    result = []
    for letter in l:
        result.append(conversion[letter])
    print("Case #"+str(cT)+": "+"".join(result))
    output.write("Case #"+str(cT)+": "+"".join(result)+"\n")
    cT += 1

f.close()
output.close()
