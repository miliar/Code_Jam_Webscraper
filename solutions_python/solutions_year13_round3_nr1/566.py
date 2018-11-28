import sys
def isvalid(s, n):
  vowels = ['a','e','i','o','u']
  for i in range(len(s)):
    temp = s[i:]
    count = 0
    for x in temp:
       if x not in vowels : 
         count+=1
       else: break
    if count >=n : return True
  return False

def nval(s):
  name = s[0]
  n = s[1]
  count = 0
  substr = [name[i:j] for i in range(len(name))  for j in range(i+1,len(name)+1,1)]
  #print substr
  for s in substr:
    if isvalid(s,n) : count +=1
  return count 
  
      
def main():
  f = open('cons.in', 'r')
  input = []
  for line in f:
    input.append(line)
  numoftests = int(input.pop(0))
  strings = []
  output = []
  for line in input:
    [st, n] = line.split()
    [st, n ] = [st, int(n)]
    strings.append([st,n])
  for s in strings:
    output.append(nval(s))
  for i in range(numoftests):
    print 'Case #%d: %d' %(i+1,output[i])
  sys.exit(0)

if __name__ == '__main__':
  main()
