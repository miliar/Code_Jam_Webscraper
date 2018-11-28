
__author__="reszegtivadar"
__date__ ="$Apr 14, 2012 1:31:15 PM$"

if __name__ == "__main__":
    print "Hello";

#a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
#our language is impossible to understand

transformArrayOriginal = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
transformArrayKey      = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","z","-","-","-","-","-","-","-","-","q"]

#
## building list from example
#
exampleCoded1  = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
exampleSolved1 = "our language is impossible to understand"
for i in range(len(exampleCoded1)):
    if (exampleCoded1[i] in transformArrayOriginal):
        transformArrayKey[transformArrayOriginal.index(exampleCoded1[i])] = exampleSolved1[i]
exampleCoded1  = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
exampleSolved1 = "there are twenty six factorial possibilities"
for i in range(len(exampleCoded1)):
    if (exampleCoded1[i] in transformArrayOriginal):
        transformArrayKey[transformArrayOriginal.index(exampleCoded1[i])] = exampleSolved1[i]
exampleCoded1  = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
exampleSolved1 = "so it is okay if you want to just give up"
for i in range(len(exampleCoded1)):
    if (exampleCoded1[i] in transformArrayOriginal):
        transformArrayKey[transformArrayOriginal.index(exampleCoded1[i])] = exampleSolved1[i]
#
## building list from example
#


print  transformArrayOriginal
print  transformArrayKey



from textFile import TextFile

#input = TextFile('2012_A_input_test')
#output = TextFile('2012_A_output_test')
input = TextFile('A-small-attempt0.in')
output = TextFile('A-small-attempt0.out')

lines = input.readLinesFromFile()

numberOfLines = int (lines[0])
print numberOfLines
for i in range(numberOfLines):
    decodedRow = "Case #"+str(i+1)+": "
    for j in range(len(lines[i+1])):
        if (lines[i+1][j] in transformArrayOriginal):
            decodedRow += transformArrayKey[transformArrayOriginal.index(lines[i+1][j])]
        else:
            decodedRow += lines[i+1][j]

    print decodedRow
    if (i == 0):
        output.writeToFile(decodedRow)
    else:
        output.appendToFile(decodedRow)