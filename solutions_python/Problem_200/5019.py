def solve(num):
  if(solve_helper(num) == True):
      return num
  else:
         return solve(num-1)
    


def solve_helper(num):
    numberList = []
    while num:
        digit = num % 10

        numberList.append(digit)

        num //= 10
    
    if(ordertest(numberList) == True):
        return True
    else:
        return False
    

def ordertest(A):
    for i in xrange(len(A) - 1):
        if A[i]<A[i+1]:
            return False

    return True
   


t=int(raw_input())
for i in xrange(1,t+1):
    n=int(raw_input())
    print "Case #{}: {}".format(i,solve(n))
