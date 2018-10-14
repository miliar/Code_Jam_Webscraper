def read():
      input = raw_input()
      input = raw_input().replace('\n','').split(' ')
      input = map(lambda x : int(x),input)
      return input
      

def solve1():
      l = read()
      xor_sum=0
      for i in l :
            xor_sum^=i
      if xor_sum != 0 :
            return 'NO'
      
      max=0
      for i in xrange(1,2**len(l)-1):
            bin_str= bin(i)
            set1,set2= get_set(l,bin_str)
            #print set1,set2
            s1 = find_sum(set1)
            s2= find_sum(set2)
            if s1 == s2 :
                  ss1 = sum(set1)
                  ss2 = sum(set2)
                  if ss1 > max:
                        max = ss1
                  if ss2 > max:
                        max = ss2
      return max

def get_set (l,bin_str):
      bin_str=list(bin_str)
      bin_str= bin_str[2:]
      bin_str.reverse()
      bin_str = bin_str+range(2,100,1)
      set1=[]
      set2=[]
      for i in xrange(len(l)):
            if bin_str[i]=='1':
                  set1.append(l[i])
            else :
                  set2.append(l[i])
      return set1,set2

def find_sum (nums):
      total = 0
      for i in nums:
            total ^=i
      return total 
      
      
      
      
def solve():
      c = int(raw_input().replace('\n',''))
      for i in xrange(c) :
            result= solve1()
            print "Case #"+str(i+1)+": "+str(result)
            
            
solve()