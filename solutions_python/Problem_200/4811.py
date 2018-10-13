#!/usr/bin/python

out = open('soluion.txt', 'w')

def tidy(number):
    digits = [digit for digit in str(number)]
    if len(digits) == 1:
        return True
    if digits[0] > digits[1]:
        return False
    checked = []
    for x,y in enumerate(digits):
        if x == 0:
            checked.append(y)
        if all([n <= y for n in checked]):
            checked.append(y)
            if x == len(digits)-1:
                return True
        else:
            return False

def lastTidy(number):
    isTidy = tidy(number)

    while not isTidy:
        number = int(number) - 1
        isTidy = tidy(number)
    return number

with open('a.txt', 'r') as f:
    problems = f.readline()
    case = 1
    for line in f.readlines():
      number = lastTidy(line.strip())
      out.write("Case #%d: %s\n" % (case, str(number)))
      case += 1

out.close()
        
