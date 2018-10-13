numbers = []
t = int(raw_input())
for i in xrange(1, t + 1):
  numbers = [int(s) for s in list(raw_input())]
  numbers  = [0] + numbers
  while True :
      change = False
      for j in xrange(1, len(numbers)):
         if (numbers[j] < numbers[j-1]):
             numbers[j-1]  = numbers[j-1] -1
             change = True

             for y  in xrange(j,len(numbers)) :
                 numbers[y] = 9
             break ;
      if change == False:
          break



  while(numbers[0] == 0) : del numbers[0]

  s ="".join(map(str, numbers))
  print "Case #{}: {}".format( i, s)
