def main ():
  decoder = {'a':'y',
             'b':'h',
             'c':'e',
             'd':'s',
             'e':'o',
             'f':'c',
             'g':'v',
             'h':'x',
             'i':'d',
             'j':'u',
             'k':'i',
             'l':'g',
             'm':'l',
             'n':'b',
             'o':'k',
             'p':'r',
             'q':'z',
             'r':'t',
             's':'n',
             't':'w',
             'u':'j',
             'v':'p',
             'w':'f',
             'x':'m',
             'y':'a',
             'z':'q'}
  result = ''
  input = open('A-small-attempt0.in', 'r')
  data = input.read().split('\n')
  num_cases = int(data.pop(0))
  for position,line in enumerate(data):
    if position < len(data) - 1:
      result += 'Case #' + str(position+1) + ': '
    words = line.split(' ')
    for count,word in enumerate(words):
      for index, char in enumerate(word):
        result += decoder[char]
      if count < len(words) - 1:
        result += ' '
    if position < len(data) - 1:
      result +='\n'
  output = open('output.txt', 'w')
  output.write(result)

        
  
if __name__ == '__main__':
  main()