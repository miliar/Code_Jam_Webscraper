import sys

def recycledNumbers(filename):
  f = open(filename, 'rU')
  lines = f.readlines()
  first = int(lines[0])
  f = open("output.txt", 'r+')
  for line in range(1,first + 1):
    nums = lines[line].split() 
    a = int(nums[0])
    b = int(nums[1])
    ranges = range(a,b+1)
    result = 0
    if len(nums[0]) == 1 and len(nums[1]) == 1:
      s = "Case #" + str(line) + ": " + str(0) +"\n"
      f.write(s)
    else:
      for i in range(0,len(ranges)):
        curr_n = str(ranges[i])
        curr_m = str(ranges[i])
        #print str(curr_n)
        leng = len(str(ranges[i]))
        length = len(str(curr_n))
        #print length
        list_tem =[]
        for j in range(0,length):
          curr_mi = int(curr_m[j:] + curr_m[:j])
          #print curr_mi
          if curr_mi > int(curr_n) and curr_mi <= b and curr_mi not in list_tem:
            result +=1
            list_tem.append(curr_mi)
      s = "Case #" + str(line) + ": " + str(result) + "\n" 
      f.write(s)	  
  f.close()	
	
def main():
  recycledNumbers(sys.argv[1])

if __name__ == '__main__':
  main()