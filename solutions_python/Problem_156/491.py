myinf = "sample.txt"
myinf = "B-small-attempt2.in"
#myinf = "B-large-practice.in"

#myout = open("output.txt",'wt')
myout = open("output1.txt",'wt')
#myout = open("output2.txt",'wt')

def move(pancakes):
    
    print(pancakes)
    x = max(pancakes)
    
    x0 = x//2
    x1 = x-x0 #move to empty
    x3=x//3
    time=0

    save = x1-x3
    cnt = 0
    for i in range(x1,x+1):
        cnt+= pancakes.count(i)
    
    if (cnt<=save) and (x%3==0) and (x3+1)<x1 and (x-x3)>pancakes.count(x):
        print('in')
        #split into 3
        pancakes[pancakes.index(x)]=x3
        pancakes.append(x-x3)   
        time=move(pancakes)+1      
        
    elif x0>pancakes.count(x):
        print('i2')
        #split into 2
        pancakes[pancakes.index(x)]=x0
        pancakes.append(x-x0)
        time=move(pancakes)+1
        #print(time)
    return time
    

myin = open(myinf,'rt').read().split('\n')
num_case = int(myin[0])
print(num_case)
for i in range(num_case):
    shift=i*2+1   
    D=int(myin[shift])
    line1 = myin[shift+1].split()
    
    pi = [int(x) for x in line1]
    print(D,pi)
    time1 = move(pi)
    time2 = max(pi)
    y=time1+time2
    print(time1,time2,y)

    myout.write("Case #%d: %s\n"%((i+1),y))

myout.close()    
