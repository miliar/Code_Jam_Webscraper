


if __name__ == "__main__":
  inputfile = 'A-large.in'
  outputfile = inputfile + '.out'
  f_in = open(inputfile,'r')
  f_out = open(outputfile,'w')

  T = int(f_in.readline()[:-1])
  for i in range(T):
    D, N = [int(x) for x in (f_in.readline()[:-1].split())]
    time = []
    for j in range(N):
      position, speed = [int(x) for x in f_in.readline()[:-1].split()]
      r = D - position
      tmp_time = r / float(speed)
      time.append(tmp_time)
    max_time = max(time)
    max_speed = D / float(max_time)
    f_out.write('Case #' + str(i+1) + ': ' + str(max_speed) + '\n')

  f_in.close()
  f_out.close()

