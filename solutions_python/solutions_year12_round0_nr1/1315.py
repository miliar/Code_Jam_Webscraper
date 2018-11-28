this = open('this.txt')
that = open('that.txt')
trans = {}

this1 = this.read()
that1 = that.read()

for i in range(0,len(this1)):
    trans[this1[i]] = that1[i]

#trans['q'] = 'q'
#trans['z'] = 'z'

trans['q'] = 'z'
trans['z'] = 'q'

filein = open('small_input.txt')
fileout = open('output1.txt', 'w')

m = filein.readlines()
for n in range(0,len(m)):
    if n == 0:
        continue
    temp = ''
    temp += 'Case #%d: ' %(n)
    #if n == 4 or n == 5:
    #    for i in m[n]:
    #        temp += i
    #    fileout.write(temp)
    #    continue
    for i in m[n]:
        temp += trans[i]
    fileout.write(temp)

this.close()
that.close()
filein.close()
fileout.close()
