def myf(j):
 jam = str(j)
 result = []
 for i in range(0,len(jam)):
  s = jam[i:]+jam[:i]
  result.append(s)
 return result
def get(a,b):
 count  = 0
 for i in range(a,b+1):
  for j in range(i+1,b+1):
   per = myf(j)
   comp = str(i)
   if comp in per:
    count = count + 1
 return count
     
  
def main():
 times = input()
 s = [None]*times
 jam = [None]*times
 for i in range(0,times):
  c = raw_input()
  s[i],jam[i] = int(c.split()[0]),int(c.split()[1])
 d = []
 for i in range(0,times):
  d.append(get(s[i],jam[i]))
 i = 1
 for ans in d:
  print "Case #%d:  %d"%(i,ans)
  i = i + 1
if __name__ == "__main__":
 main()
