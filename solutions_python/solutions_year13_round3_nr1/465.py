def solve(**kwargs):
  
  name = kwargs['name']
  n = kwargs['n']
  
  
  
  n_value = 0
  
  for i in range(n,len(name) + 1):
    for o in range(len(name) - i + 1):
	n_value += hasConsecutiveConsonants(name[o:o + i],n)
	
  
  return str(n_value)

def hasConsecutiveConsonants(word,n):
  
  vocals = ['a','e','i','o','u']
  
  for i in range(len(word) - n + 1):
    subString = word[i:i + n]
    if 'a' not in subString and 'e' not in subString and  'i' not in subString and  'o' not in subString and  'u' not in subString:
      return True
  
  return False

if __name__ == "__main__":
  
  f_in = open('file.in','r')
  f_out = open('file.out','w')

  N = int(f_in.readline())

  for i in range(N):
    problem = {}
    [problem['name'],problem['n']] = f_in.readline().replace('\n','').split(' ')
    problem['n'] = int(problem['n'])
  
    f_out.write('Case #' + str(i + 1) + ': ' + solve(**problem) + '\n')

  f_in.close()
  f_out.close