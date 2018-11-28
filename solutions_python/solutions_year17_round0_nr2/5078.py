        
t = int(raw_input())  # read a line with a single integer
for z in xrange(1, t + 1):
  n= int(raw_input())  # read a list of integers, 2 in this case
  if n < 10:
       tidy_number = n
  else:
    for i in range(n, 0, -1):
            c = 1
            k = i % 10
            j = i/10
            while j != 0 :
                if k >= j%10 :
                    c=1
                    k = j % 10
                    j = j/10
 
		else:
                    c = 0
                    break
            if c == 1:
                tidy_number = i
                break
		
  print "Case #{}: {} ".format(z,tidy_number)

 
