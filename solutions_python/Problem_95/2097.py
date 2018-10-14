import math

plaintext= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cypher =['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']



def translateLetter(letter):
    if letter == " ": return letter
    index = 0
    while (cypher[index] != letter):index+=1
    return plaintext[index]

def translate(phrase):
    plain = ""
    for i in range(len(phrase)):
        plain+=translateLetter(phrase[i])
    return plain

directory = "/home/se/Downloads/"

inFile=directory+"A-small-attempt0.in"
outfile = directory+"test.out"

input = open(inFile)
output = open(outfile, "w")

line = input.readline().strip()
cases = int(line)

for case in range(0,cases):
        data = input.readline().strip()
        phrase = translate(data)
        outputStr =  "Case #"+str(case+1)+": "+phrase
        print >> output, outputStr
        print outputStr
