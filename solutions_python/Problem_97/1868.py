#CHANGE FILE NAME

f = open("C:\\Users\\Shaun\\Downloads\\C-small-attempt4.in")
nums = f.read().replace("\n"," ").strip().split()
nums = [ int(w) for w in nums ]

out = open("C:\\Users\\Shaun\\Desktop\\recycleout","w")


def recycled(x,y):
    x = str(x)
    y = str(y)

    if len(x) != len(y):
        return False
    if not samechars(x,y):
        return False

    for i in range(1,len(x)):
        if (x[-i:] + x[:-i]) == y:
            return True

    return False



def samechars(x,y):
    for c in x:
        if x.count(c)!= y.count(c):
            return False
    return True

    

def count(low,high):
    total = 0
    for i in range(low,high+1):
        for j in range(i+1,high+1):
            if recycled(i,j):
                total +=1
    return total

def stamp(line, number):
    print("Case #" + str(line) + ": " + str(number),file = out)



def go():
    global nums
    num = nums[0]
    nums = nums[1:]
    for i in range( len(nums)//2):
        x = nums[2*i]
        y = nums[2*i + 1]
        stamp(i+1,count(x,y))
    

go()

f.close()
out.close()

    
