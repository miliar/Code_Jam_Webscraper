alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
google =   ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']


#b h z

input = open('input.in', 'r')
output = open('output.txt', 'w')
cases = int(input.readline())

for x in range(cases):
  inword = input.readline().replace('\n','')
  print inword
  outword = []
  for y in range(len(inword)):
    if inword[y] == ' ':
      outword.append(' ')
    else:
      outword.append(alphabet[google.index(inword[y])])
  out = ''.join(outword)
  print out
  
  output.write('Case #' + str(x+1) + ': ' + out + '\n')