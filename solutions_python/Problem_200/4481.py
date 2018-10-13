#!/usr/bin/env python

def is_tidy(s):
  last = s[0]
  i=0
  for i in range(len(s)-1):
    # print i, s[i]
    if int(s[i]) > int(s[i+1]):
      return False
  return True

def biggest_tidy(s):
  for i in range(int(s),0,-1):
    # print i
    if is_tidy(str(i)):
      # print i
      return i

def main():
  biglist = readInput("B-small-attempt0.in")
  output=[]
  for s in biglist:
    print s,"------------"
    n = biggest_tidy(s)
    print n
    output.append(n)
  writeOutput(output,"answer.out")



def readInput(filename):
	biglist=[]
 	with open(filename) as file:
 		next(file)
 		for line in file:
 			biglist.append(line.strip())
 	return biglist

def writeOutput(output, filename):
	file = open(filename, "w")
	for i in range(0,len(output)):
			file.write("Case #%d: %s\n" % (i+1, output[i]))
	file.close()

if __name__ == "__main__":
    main()