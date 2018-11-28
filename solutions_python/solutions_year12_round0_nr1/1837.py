translation = {
   'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 
   'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u',
   'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k',
   'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w',
   'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a',
   'z':'q'
}

input_file = open("A-small-attempt0.in","r")
lines = input_file.readlines()
test_cases_count = int(lines[0].strip())

i = 1
for test_case in lines[1:]:
   test_case = test_case.strip()
   output = []
   for character in test_case:
      if character in translation.keys():
         output.append(translation[character])
      else:
         output.append(character)
      
   print "Case #%d: %s" % (i, ''.join(output))
   i += 1
