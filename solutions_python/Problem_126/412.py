#! /usr/bin/env python3

def isVowel(s):
  return s == 'a' or s == 'e' or s == 'u' or s == 'i' or s == 'o'

def isConsonant(s):
  return not isVowel(s)

def isConsequetiveConsonants(s):
  return all(map(isConsonant, s))

def calculateScore(name, n):
  score = 0
  prev = 0
  for i in range(0, len(name) - n + 1):
    if isConsequetiveConsonants(name[i : i + n]):
      score += (i - prev + 1) * (len(name) - i - n + 1)
      prev = i + 1
  return score

def processCase(i):
  line = input()
  params = line.split()
  name = params[0]
  n = int(params[1])
  result = calculateScore(name, n)
  print("Case #" + str(i) + ": " + str(result))

def main():
  line = input()
  if line:
    number = int(line)
    for i in range(number):
      processCase(i + 1)

main()
