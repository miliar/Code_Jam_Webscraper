

if __name__ == '__main__':
  #filename = 'sample.txt'
  #filename = 'C-small-1-attempt0.in'
  #filename = 'C-small-2-attempt0.in'
  filename = 'C-large.in'
  outFilename = 'out_' + filename
  f_in = open(filename, 'r')
  f_out = open(outFilename,'w')

  T = int(f_in.readline()[:-1])

  for i in range(T):
    N, K = (f_in.readline()[:-1]).split()
    N = int(N)
    K = int(K)
    K_len = len(bin(K)[2:])
    r = K - (2 ** (K_len -1 ) - 1)
    N_r = N - (2 ** (K_len - 1) - 1)
    d = N_r / (2 ** (K_len - 1))
    remainder = N_r % (2 ** (K_len - 1))
    #print 'r:',r
    #print 'remainder:',remainder
    if r <= remainder:
      s = d + 1
    else:
      s = d
    if s % 2 == 0:
      maxLR = s/2
      minLR = s/2 - 1
    else:
      maxLR = s/2
      minLR = s/2

    outputLine = 'Case #' + str(i+1) + ': ' + str(maxLR) + ' ' + str(minLR) + '\n'
    f_out.write(outputLine)

  f_in.close()
  f_out.close()
