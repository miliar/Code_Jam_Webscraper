def ex1(st):
  zero = []
  one = []
  two = []
  three = []
  four = []
  five = []
  six = []
  seven = []
  eight = []
  nine = []
  zero.append('Z')
  zero.append('E')
  zero.append('R')
  zero.append('O')
  one.append('O')
  one.append('N')
  one.append('E')
  two.append('T')
  two.append('W')
  two.append('O')
  three.append('T')
  three.append('H')
  three.append('R')
  three.append('E')
  three.append('E')
  four.append('F')
  four.append('O')
  four.append('U')
  four.append('R')
  five.append('F')
  five.append('I')
  five.append('V')
  five.append('E')
  six.append('S')
  six.append('I')
  six.append('X')
  seven.append('S')
  seven.append('E')
  seven.append('V')
  seven.append('E')
  seven.append('N')
  eight.append('E')
  eight.append('I')
  eight.append('G')
  eight.append('H')
  eight.append('T')
  nine.append('N')
  nine.append('I')
  nine.append('N')
  nine.append('E')
  numbers = []
  numbers.append(zero)
  numbers.append(one)
  numbers.append(two)
  numbers.append(three)
  numbers.append(four)
  numbers.append(five)
  numbers.append(six)
  numbers.append(seven)
  numbers.append(eight)
  numbers.append(nine)
  res = []
  k = 0
  s = str(st)
  while s:
    del res[:]
    res_str = ""
    s = str(st)
    for i in range (len(numbers)):
      while verifyNumber(s, numbers[(i + k) % 10]):
        res.append((i + k) % 10)
        for n in numbers[(i + k) % 10]:
          for j in range(len(s)):
            if s[j] == n:
              s = s[:j] + s[(j+1):]
              break;
    res.sort()
    res_str = ""
    for n in res:
      res_str += str(n)
    k = k + 1
  return res_str

def verifyNumber(s, num):
  num_copy = list(num)
  for c in s: 
    if c in num_copy:
      num_copy.remove(c)
  return not num_copy
    

def main():
  n = input()
  for i in range(1, n + 1):
    s = raw_input()
    s = str(s)
    print("Case #" + str(i) + ": " + ex1(s))

main()
