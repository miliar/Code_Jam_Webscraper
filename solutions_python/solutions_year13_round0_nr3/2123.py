import math

f = open('C-small-attempt0.in')
q = open('output.txt','w')
lines =[]
count = 0

def is_square(num):
    sqrt_num=math.sqrt(num)
    return int(sqrt_num+0.5)**2==num

for line in f:
    if count!=0:
        num_count=0
        a,b = line.split()
        a,b = int(a), int(b)
        for num in range(a,b+1):
            if num%4==0 or num%4==1:
                if is_square(num):
                    sqrt_num=int(math.sqrt(num)+0.5)
                    if num==int(str(num)[::-1]) and sqrt_num==int(str(sqrt_num)[::-1]):
                        num_count+=1
        q.write("Case #"+str(count)+": "+str(num_count)+"\n")
    else:
        amount_of_cases=int(line)
    count+=1

f.close()
q.close()
