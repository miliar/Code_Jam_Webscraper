from string import maketrans

def replaceString( inStr) :
    intab = "abcdefghijklmnopqrstuvwxyz"
    outtab = "yhesocvxduiglbkrztnwjpfmaq"
    transtable = maketrans(intab,outtab)
    return inStr.translate(transtable)


f=open('E:\\Dropbox\\2012-project\\GoogleJam\\A-small-attempt1.in')
fw = open('E:\\Dropbox\\2012-project\\GoogleJam\\A-small-attempt1.out','w')

numberLines = int(f.readline())
for x in range(numberLines):
    output = "Case #" +str(x+1)+": " +replaceString(f.readline())
    fw.write(output)

f.close()
fw.close()

