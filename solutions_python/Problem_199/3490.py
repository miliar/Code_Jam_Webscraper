#!/usr/bin/python
def process(ch,k):
    a=0
    s = list(ch)
    N  = len(s)
    if not '-' in s:
	   return 0
    while True:
       j=s.index('-')
       if (j+k)>N:
           return "IMPOSSIBLE"
       for l in xrange(j,j+k):
          if s[l]=='-':
             s[l]='+'
          else:
             s[l] = '-'
       a+=1
       ch= ''.join(s)
       s=list(ch)
       if ch.find('-')==-1:
	      break
    return a
def main():
    size_inputs = int(raw_input())
    j=1
    while(j<=size_inputs):
        ch, k = [s for s in raw_input().split(" ")]
        a = process(ch,int(k))
        print "Case #{}: {}".format(j, a)
        j+=1

if __name__ == '__main__':
   	main()