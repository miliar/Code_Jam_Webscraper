#!/usr/bin/python2.4
#import timeit

def _combinators(_handle, items, n):
    ''' factored-out common structure of all following combinators '''
    if n==0:
        yield [  ]
        return
    for i, item in enumerate(items):
        this_one = [ item ]
        for cc in _combinators(_handle, _handle(items, i), n-1):
            yield this_one + cc

def uniqueCombinations(items, n):
    ''' take n distinct items, order is irrelevant '''
    def afterIthItem(items, i):
        return items[i+1:]
    return _combinators(afterIthItem, items, n)
     

def main():
#  t = timeit.Timer()
  for test_case in range(input()): #Looping through each test case
     n, A, B, C, D, x0, y0, M = map(int, raw_input().split())
     X = x0
     Y = y0
     nt=0
     trees =[[x0,y0]]
     for i in range(n-1): # Get list of trees
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees.append([X,Y])
   
     #print trees

      

     for x in uniqueCombinations(trees, 3):
       cx=0
       cy=0
       for v in range(3):
          cx+=x[v][0]
          cy+=x[v][1]
       if cx%3==0:
           if cy%3==0:
               nt+=1    

     

    
     print 'Case #%s: %s' % ((test_case + 1), nt)
    # print t,m1
  #print "%.2f usec/pass" % (1000000 * t.timeit(number=100000)/100000)
main()
