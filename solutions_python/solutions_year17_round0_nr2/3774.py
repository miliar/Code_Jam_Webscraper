from sys import argv

INPUT_FILE = argv[1]
OUTPUT_FILE = argv[2]

with open(INPUT_FILE) as f1:
  with open(OUTPUT_FILE,'w') as f2:
    current = f1.readline()
    current = f1.readline()[:-1]
    case = 1
    while current!='':
      number = int(current)
      digits = [int(d) for d in str(current)]
      answer = ''
      if all([a<=b for a,b in zip(digits,digits[1:])]):
        answer = str(number)
      else:
        while not all([a<=b for a,b in zip(digits,digits[1:])]):
          index = 0
          while digits[index]<=digits[index+1]:
            index += 1
          for n in range(index+1,len(digits)):
            digits[n] = 9
          if index>0:
            new_d = [int(c) for c in str(int(''.join([str(k) for k in digits[:index+1]]))-1).zfill(index)]
            digits[:index+1] = new_d
          else:
            if digits[0]==0:
              digits = digits[1:]
            else:
              digits[0] -= 1
          if digits[0]==0:
            digits = digits[1:]
        answer = ''.join([str(b) for b in digits])
      f2.write('Case #%d: %s\n'%(case,answer))
      case += 1
      current = f1.readline()[:-1]
