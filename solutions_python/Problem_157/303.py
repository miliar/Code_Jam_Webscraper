def multiply(x, y):
  if x == '1':
    return y
  elif x[0] == '-':
    temp = multiply(x[1], y)
    if temp[0] == '-':
      return temp[1]
    else:
      return '-' + temp
  elif x == 'i':
    if y == 'i':
      return '-1'
    elif y == 'j':
      return 'k'
    elif y == 'k':
      return '-j'
  elif x == 'j':
    if y == 'i':
      return '-k'
    elif y == 'j':
      return '-1'
    elif y == 'k':
      return 'i'
  elif x == 'k':
    if y == 'i':
      return 'j'
    elif y == 'j':
      return '-i'
    elif y == 'k':
      return '-1'

def solve(s, target):
  letter = s[0]
  if len(s) == 0:
    return ""
  for j in range(1, len(s)):
    if letter == target:
      return s[j:]
    else:
      letter = multiply(letter, s[j])
  if letter == target:
    return ""
  else:
    return "-1" 

def print_solution(ans):
  f = open('output_small.txt', 'w')
  for i in range(len(ans)):
    f.write("Case #" + str(i+1) + ": " + str(ans[i]) +"\n")

if __name__ == '__main__':
  f = open('C-small-attempt2.in')
  T = int(f.readline())
  answers = [0]*T
  for i in range(T):
    line = f.readline().split(' ')
    L = int(line[0])
    X = int(line[1])
    s = f.readline().strip()

    pattern = s*X

    if len(pattern) < 3:
      answers[i] = "NO"
    else:
      letter = pattern[0]
      observedI = False
      moreThanTwo = False
      for j in range(1,len(pattern)):
        if letter == "i":
          observedI = True
          if len(pattern) - j >= 2:
            moreThanTwo = True
        letter = multiply(letter, pattern[j])
      if letter == '-1' and observedI and moreThanTwo:
        answers[i] = 'YES'
      else:
        answers[i] = 'NO'

    """
    target = ['i', 'j', 'k']
    target_ind = 0
    if len(pattern) < 3:
      pattern = "-1" 
    while len(pattern) >= 3:
      pattern = solve(pattern, target[target_ind])
      target_ind += 1 
      if target_ind == 3:
        while len(pattern) > 0 and pattern != '-1':
          pattern = solve(pattern, '1')
          
    if pattern == "-1":
      answers[i] = "NO"
    else:
      answers[i] = "YES"
    """

  print_solution(answers)
  print answers

