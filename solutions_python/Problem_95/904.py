# Internal CodeJam 2012
# Speaking in Tongues

def main():
  with open('small_input', 'rB') as f:
    info = f.readlines()

  # Determine # of cases
  cases = info[0].strip()
  data = [line.strip() for line in info[1:]]

  # Dict derived from examples (read through the 'input' string
  # and assigned the value of each character to the corresponding
  # 'output' string at that position. 
  main_dict = {
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q',
    ' ': ' '
  }
 
  # For each input, iterate through the characters, find the correspdoning
  # character in main_dict and append to [newstring] 
  for index, line in enumerate(data):
    newstring = []
    for character in line:
      newstring.append(main_dict[character])
    newstring = ''.join(newstring)

    print 'Case #%s: %s' % (index+1, newstring)
    
if __name__ == '__main__':
  main()
