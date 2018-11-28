
def main():  
  input = read_in()
  
  from time import time
  t0 = time()

  case = 1
  f = open('C-small-out.txt', 'w')
  for nums in input:
    a = int(nums[0])
    b = int(nums[1])
    
    cnt = 0
    checked = {}
    for i in range(a, b):
      if i not in checked:
        cnt += calc_rec(i, b, checked)
      
    #print ("Case #%d: %s\n" % (case, cnt))
    f.write("Case #%d: %s\n" % (case, cnt))
    case += 1

  f.close()
  
  t1 = time()
  print 'function vers1 takes %f' %(t1-t0)

def calc_rec(num, b, checked):
  cnt = 0
  num_s = str(num)
  l = len(num_s)
  p = {}
  for i in range(0, l):
    new_num = int(num_s[i:]+num_s[:i])    
    if new_num > num and new_num <= b and new_num not in p:
      #print num_s + " : " + str(new_num)
      p[new_num] = 1
      checked[new_num] = 1
  
  n = len(p); 
  cnt += (n*(n+1)/2)   
    
  return cnt

def read_in():
  f = open('C-large.in', 'r')
  lines = f.read().splitlines()
  input = []
  for l in lines[1:]:
    input.append(l.split())
  f.close()
  return input

if __name__ == '__main__':
  main()