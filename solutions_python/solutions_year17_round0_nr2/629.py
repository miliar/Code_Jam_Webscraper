

if __name__ == "__main__":
  #filename = 'sample.txt'
  filename = 'B-large.in'
  outfilename = 'out_' + filename
  f = open(filename, 'r')
  f_out = open(outfilename, 'w')

  T = int(f.readline()[:-1])
  for i in range(T):
    N = int(f.readline()[:-1])
    N_list = [int(x) for x in list(str(N))]
    M_list = N_list
    position = 0
    broken = False
    for j in range(len(N_list)-1):
      if (N_list[j] < N_list[j+1]):
        position = j+1
      elif (N_list[j] > N_list[j+1]): # illegal
        for k in range(position+1,len(N_list)):
          M_list[k] = 0
        broken = True
        break
    if broken:
      M = int(''.join([str(x) for x in M_list])) - 1
    else: 
      M = int(''.join([str(x) for x in M_list]))
    outputLine = 'Case #' + str(i+1) + ': ' + str(M) + '\n'
    f_out.write(outputLine)

  f.close()
  f_out.close()
      
