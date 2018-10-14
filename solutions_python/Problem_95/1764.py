input = open("A-small-attempt0.in")
output = open("A-small-attempt0.out", "w")

EngToGooglerese = {
'a' : 'y',
'b' : 'n',
'c' : 'f',
'd' : 'i',
'e' : 'c',
'f' : 'w',
'g' : 'l',
'h' : 'b',
'i' : 'k',
'j' : 'u',
'k' : 'o',
'l' : 'm',
'm' : 'x',
'n' : 's',
'o' : 'e',
'p' : 'v',
'q' : 'z',
'r' : 'p',
's' : 'd',
't' : 'r',
'u' : 'j',
'v' : 'g',
'w' : 't',
'x' : 'h',
'y' : 'a',
'z' : 'q'}

GooglereseToEng = dict([[v,k] for k,v in EngToGooglerese.items()])

input.next() #Skip the number of cases
i=1
for line in input:
  output.write("Case #" + str(i) + ": ")
  for char in line:
    try:
      output.write(GooglereseToEng[char])
    except KeyError:
      output.write(char)
  i=i+1
