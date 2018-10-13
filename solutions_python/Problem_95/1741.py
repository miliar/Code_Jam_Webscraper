# mrtwiddletoes
def mappings(x):
  mappings = {'a' : 'y',
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
              '\n' : ''}
  return mappings[x]
f = open('/home/thinkbot/src/random/codejam/A-small-attempt2.in')
output = open('/home/thinkbot/src/random/codejam/output.out', 'w')
num_trials = f.readline()
for a in range(int(num_trials)):
  sentence = f.readline()
  changed_sentence = ""
  for word in sentence:
    for letter in word:
      changed_sentence = changed_sentence + mappings(letter)
  changed_sentence = changed_sentence + " "
  output.write("Case #{0}: ".format(a+1) + changed_sentence + "\n")
