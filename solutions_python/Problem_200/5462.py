import pdb
fin = open("in.txt")   # input file
fout = open("out.txt", "w") # output file

lines = fin.readline()

j = 1

for line in fin.readlines():
  str_num = line.rstrip()
  num = int(str_num)
  exit = False

  while(num > 10):
    for i, n in enumerate(str_num):
      print(num, i, n)  # testing
 
      # exit for-enum and while loops if end of string is reached
      try:
        str_num[i+1]
      except IndexError:
        exit = True
      else:
        exit = False
      if exit:
        break
      
      # exit for-enum loop if next digit is less than current (not ordered)
      if int(str_num[i+1]) < int(n):
        swap = str(int(n)-1)
        for k in range(i, len(str_num)-1):
          swap += '9'
        str_num = str_num[:i] + swap
        num = int(str_num)
        break;
    
    if exit:
      break

  out = "Case #" + str(j) + ": " + str(num) + '\n'
  print(out)
  fout.write(out)
  j += 1