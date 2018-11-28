from string import maketrans

intab = "abcdefghijklmnopqrstuvwxyz"
outtab ="yhesocvxduiglbkrztnwjpfmaq"
trantab = maketrans(intab, outtab)

inf = file('C:\\temp\\in.txt', 'r')
outf = file('C:\\temp\\out.txt', 'w')
c = int(inf.readline().replace('\n',''))
for i in range(c):
    outf.write("Case #" + str(i+1) + ": " + inf.readline().translate(trantab))

inf.close()
outf.close()
    
