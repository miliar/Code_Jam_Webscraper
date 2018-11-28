import time

def get_num_recycled( number_s, num_digits, limit ):
  num_s = number_s + number_s
  num = int(number_s)
  r_nums = []
  for i in range( 1, num_digits ):
    r_num_s = num_s[i:num_digits+i]
    r_num = int(r_num_s)
    if ( r_num > num and r_num <= limit ):
      r_nums.append( r_num )

  return len(set(r_nums))

def get_num_recycled2( num, num_digits, power, limit ):
  r_nums = []
  r_num = num
  for i in range( 1, num_digits ):
    r_num = ( r_num % 10 ) * power + ( r_num / 10 )
    if ( r_num > num and r_num <= limit ):
      r_nums.append( r_num )

  return len(set(r_nums))

num_cases = input()
#start_t = time.clock()
for i in range( 1, num_cases + 1 ):
  start_s, limit_s = raw_input().split()
  #start_s = '1000000'
  #limit_s = '2000000'
  num_recycled = 0
  num_digits = len(start_s)
  power = pow( 10, num_digits - 1 )
  limit = int(limit_s)
  start = int(start_s)
  for num in range( start, limit + 1 ):
     #num_recycled += get_num_recycled( str(num), num_digits, limit )
     num_recycled += get_num_recycled2( num, num_digits, power, limit )
  print 'Case #' + str(i) + ': ' + str( num_recycled )
#end_t = time.clock()
#print start_t, end_t, end_t - start_t
