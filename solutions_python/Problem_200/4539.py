



def tidy(x):
        holder = None
	while x > 0:
            if holder is None:
               holder = x % 10
               x = x//10 
            if holder < x%10:
               return False
            holder = x%10
            x = x//10
        return True

def last(x):
    for i in xrange(x,0, -1):
	if tidy(i):
           return i


file = open("testTidy.txt","w") 
nums = raw_input()
for i in xrange(int(nums)):
    line = raw_input()
    answer = last(int(line))
    file.write("Case #"+str(i+1)+": "+ str(answer)+"\n")

