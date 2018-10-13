# programing language python3
# problem: Speaking in Tongues

# for the language
Key = {
       'a':'y',
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
       'z':'q'
        }

def main():
  file_input = open('input.txt')        # reading input from this file
  file_output = open('output.txt', 'w') # this is the output file
  N = file_input.readline()
  N = int(N[:-1])
  for X in range(1,N+1):
    G = file_input.readline()
    G = G[:-1] if G[-1] == '\n' else G  # removing \n from the end of the string;
    S = ''                              # the output string for each G
    for each in G:
      if each in Key.keys():
        S = S + Key[each]
      else:
        S = S + each
    file_output.write('Case #'+str(X)+": "+S+'\n')
  file_input.close()
  file_output.close()
if __name__ == '__main__':
  main()
