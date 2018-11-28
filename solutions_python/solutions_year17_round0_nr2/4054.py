#!/usr/bin/python
def process(number):
    if number%10==number:
	   return number
    while number>0:
       i=0
       ch = list(str(number))
       N = len(ch)
       ok=0
       while(i<N-1):
        if (ch[i]<=ch[i+1]):
          ok=1
        else:
          ok=0
          break
        i+=1
       if ok==1:
        break
       number-=1
       #print number  
    return number
def main():
    size_inputs = int(raw_input())
    j=1
    while(j<=size_inputs):
        number = int(raw_input())
        a = process(number)
        print "Case #{}: {}".format(j, a)
        j+=1

if __name__ == '__main__':
   	main()