# Speaking in Tongues

reverseGooglerese = {
  'a' : 'y',
  'b' : 'h',
  'c' : 'e',
  'd' : 's',
  'e' : 'o',
  'f' : 'c',
  'g' : 'v',
  'h' : 'x',
  'i' : 'd',
  'j' : 'u',
  'k' : 'i',
  'l' : 'g',
  'm' : 'l',
  'n' : 'b',
  'o' : 'k',
  'p' : 'r',
  'q' : 'z',
  'r' : 't',
  's' : 'n',
  't' : 'w',
  'u' : 'j',
  'v' : 'p',
  'w' : 'f',
  'x' : 'm',
  'y' : 'a',
  'z' : 'q',
  ' ' : ' ',
}


# main code

fr = open('A-small-attempt0.in', 'r')
fw = open('A-small-attempt0.out', 'w')

numOfTestCase = int(fr.readline())

for x in range(0,numOfTestCase):
  result = ""

  line = fr.readline()
  for y in range(0,len(line)-1):
    result = result + reverseGooglerese[line[y]]
  
  fw.write("Case #" + str(x+1) + ": " + result + "\n")

fr.close()
fw.close()
