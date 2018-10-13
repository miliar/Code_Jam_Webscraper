input_file = 'A-small-attempt0.in'
output_file = 'outputtongue.txt'

entry_lines = open(input_file,'r')
procthis = []
for line in entry_lines:
  procthis.append(line)
entry_lines.close()

googlerese = {'a':'y','b':'h','c':'e','d':'s',
              'e':'o','f':'c','g':'v','h':'x',
              'i':'d','j':'u','k':'i','l':'g',
              'm':'l','n':'b','o':'k','p':'r',
              'q':'z','r':'t','s':'n','t':'w',
              'u':'j','v':'p','w':'f','x':'m',
              'y':'a','z':'q'
             }

output = open(output_file,'a')

total_set = int(procthis[0])
counter = 0
while counter < total_set:
  rawinput = procthis[counter+1]
  inputline = rawinput.replace('\n','')
  results = ""
  indexing = 0
  for letter in inputline:
    if letter == ' ':
      results = results + ' '
    else:
      results = results + googlerese[letter]
  case_count = counter + 1
  counter+=1
  outputmsg = "Case #" + str(case_count) + ": " + results + "\n"
  output.write(outputmsg)

output.close()

