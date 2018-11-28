import math
def isSq(st):
         num = int(st)
         if (math.sqrt(num)%1==0 and isP(str(int(math.sqrt(num))))):
                  return True
         else:
                  return False
