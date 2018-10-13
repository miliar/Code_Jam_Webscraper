#!/usr/bin/python

def process_input(shyness):
  total_people = shyness[0]
  additional_people = 0

  Si = 1
  while Si < len(shyness):
    if Si > total_people + additional_people:
      additional_people += Si - total_people - additional_people
    total_people += shyness[Si]
    Si += 1

  return additional_people

def main():
  T = int(raw_input())
  for i in range(T):
    line = raw_input()
    shyness_string = line.split()[1]
    shyness = [int(digit) for digit in shyness_string]

    print "Case #%i: %i" % ( i+1, process_input(shyness) )

if __name__ == '__main__':
  main()