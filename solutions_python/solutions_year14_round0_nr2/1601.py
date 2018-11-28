

with open('sample.in','rb') as f, open('solution.txt','wb') as o:
  number_of_test_cases = int(f.readline())
  for case in xrange(0,number_of_test_cases):
    param = [float(x) for x in f.readline().split(' ')]
    current_time = 0.0
    current_rate = 2.0
    current_cookies = 0.0
    while True:
      current_time += param[0]/float(current_rate)
      if (current_time + (param[2]-param[0])/current_rate) <= (current_time+ param[2]/(current_rate+param[1])):
        solution = current_time + (param[2]-param[0])/current_rate
        o.write('Case #%i: %.7f\n'%(case+1,solution))
        break
      else:
        current_rate+=param[1]
