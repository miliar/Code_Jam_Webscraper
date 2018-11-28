import math

f = open("C-small-attempt0.in");

problems = int(f.readline())


def readProblem():
    nums = f.readline().strip('\n')
    nums = nums.split(' ')
    return (int(nums[0]), int(nums[1]))

def palindrome(num):
    pal = str(num)
    l = len(pal)

    for i in range(l):
        if pal[i] != pal[l-1-i]:
            return False;

    return True;

def squared2(n):
    nsqrt = math.sqrt(n)
    return nsqrt == math.trunc(nsqrt)

def squared(apositiveint):
    if (apositiveint == 1):
        return True
    
    x = apositiveint // 2
    if (x == 0):
        return False
    
    seen = set([x])
    while x * x != apositiveint:
      x = (x + (apositiveint // x)) // 2
      if x in seen: return False
      seen.add(x)
    return True    

def processProblem( start, stop, case ):
    count = 0;
    
    for i in range(start, stop + 1, 1):
        if not palindrome(i):
            continue;
        
        if not squared(i):
            continue;

        if not palindrome(int(math.sqrt(i))):
            continue;
        
        count += 1

    print(case + str(count))    
    return count;


for i in range(problems):
    (start, stop) = readProblem()
    case = "Case #" + str(i + 1) + ": "
    processProblem( start, stop, case)
    
f.close();
