#!python
#shyness.py
import sys

def main(argv):
  file = open("A-large.in", 'r')
  out = open("ouputshyness.txt", 'w')
  
  cases = int(file.readline())
  on_case = 1
  
  for line in file:
    case = line.split(' ')
    max = int(case[0])
    standing = 0
    friends = 0
    for i in range(0, max + 1):
      if standing < i:
        friends += i - standing
        standing = i
      standing += int(case[1][i])
      
    out.write('Case #' + str(on_case) + ': ' + str(friends) + '\n')
    on_case += 1

if __name__ == "__main__":
  main(sys.argv)