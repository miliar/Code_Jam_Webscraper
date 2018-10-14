letters = 'abcdefghijklmnopqrstuvwxyz '
change = 'yhesocvxduiglbkrztnwjpfmaq '

filename = open("A-small-attempt1.in",'r')
s = filename.readlines()
for i in range(len(s)):
    s[i] = s[i].replace("\n","")
cases  = int(s[0])

filename.close()
caseNumber = 1


newFile = open("output.in","w")

for i in s[1:]:
    newFile.writelines("Case #%s: "%(caseNumber),)
    for letter in i:
        indexLetter = letters.index(letter)
        newFile.writelines(change[indexLetter])
    newFile.writelines("\n")
    caseNumber+=1

newFile.close()
    
    
