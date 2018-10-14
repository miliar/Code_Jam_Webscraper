import sys

def dancingGooglers(filename):
  f = open(filename, 'rU')
  lines = f.readlines()
  first = int(lines[0])
  f = open("output.txt", 'r+')
  for line in range(1,first + 1):
    nums = lines[line].split()
    noOfGooglers = int(nums[0])
    noOfJudges = 3
    surprise = int(nums[1])
    p = int(nums[2])
    add = 0
    d = 0
    for c in range(3, noOfGooglers + 3):
      if (int(nums[c]) >= (p + 2*(p - 1)) or (int(nums[c]) >= (p*3))):
        add+=1
      elif int(nums[c]) >= (p + 2*(p - 2)) and surprise > 0 and (p-2) >=0: 
        add+=1
        surprise-=1
    s = "Case #" + str(line) + ": " + str(add) + "\n"
    f.write(s)
  f.close()	

def sum_to_n(n, size, limit=None):
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail
	  
def main():
  dancingGooglers(sys.argv[1])

if __name__ == '__main__':
  main()