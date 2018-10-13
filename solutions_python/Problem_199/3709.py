

def pank(s,k):
   a= list(s)
   count = 0
   for i in xrange(len(a)-k+1):
	if "-" == a[i]:
             for j in xrange(k):
                 if a[i+j] == "+":
                     a[i+j] = "-"
                 else:
                     a[i+j] = "+"
             count += 1
   if "-" in a[len(a)-k:]:
          return "impossible"        
   return str(count)


file = open("test.txt","w") 
nums = raw_input()
for i in xrange(int(nums)):
    line = raw_input().split()
    answer = pank(line[0], int(line[1]))
    file.write("Case #"+str(i+1)+": "+ answer+"\n")
