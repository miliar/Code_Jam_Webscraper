import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
print len(alphabet)

file = open(sys.argv[1],'r')
lines2 = file.readlines()
file.close() 
       

i = 0
googleToEng = {'a':'y', 'o':'e', 'z' :'q'}
engToGoogle = {'y':'a', 'e':'o', 'q' :'z'}

def translatorGtoE(dictGtoE, dictEtoG, line1, line2):
    i = 0
    for char in line1:
        dictGtoE[char]     = line2[i]
        dictEtoG[line2[i]] = char
        i = i + 1
               
def learn(lines):
    i = 0;
    for line in lines[0:3]:
        print line + lines[i+4]
        translatorGtoE(googleToEng, engToGoogle, line, lines[i+4])
        i = i + 1


        
learn(lines2)

print len(googleToEng)
print len(engToGoogle)

for key in sorted(googleToEng.iterkeys()):
    print "%s : %s" % (key, googleToEng[key])       

for letter in alphabet:
    if letter not in googleToEng:
        print letter + " is not in the dict"
        char = letter
for letter in alphabet:
    if letter not in engToGoogle:
        print letter + " is not in the dict"
        char2 = letter 
               
googleToEng[char] = char2
engToGoogle[char2]= char

def translate(line, number):
    line2 = 'Case #'+ str(number) + ': '
    for char in line:
        line2 = line2 + googleToEng[char]
    return line2

file = open(sys.argv[2],'r')
lines = file.readlines()
file.close() 

lines2 = []
i = 1
for line in lines[1:]:
    lines2.append(translate(line, i))
    i = i + 1
print lines2

file = open(sys.argv[3],'w')
lines = file.writelines(lines2)


       
#file = open(sys.argv[1],'r')
#lines = file.readlines()
#file.close()
#line1 = lines[0]
#T = line1[0]
#print T
#
#
#for line in lines[1:]:
#    i = i + 1
#    for char in line:
        