import numpy as np

######################################################################
# Note: I pregenerate a list of fair and square numbers
# prior to downloading the contest data (I was told this was ok).
# The code for both pieces is in this file, and is toggled by the 
# boolean variable PRE_GENERATE (True to generate, False for contest)
######################################################################

PRE_GENERATE=False


def makelist():
  cent = ['','0','1','2']
  pal_list=[]
  #check length one strings
  for c in ['0','1','2','3']:
    pal2 = long(c)**2
    if str(pal2)==str(pal2)[::-1]:
      pal_list.append(pal2)
  #check longer strings of binary
  for k_len in xrange(1,26):
    print k_len
    for k in xrange(2**(k_len-1),2**k_len):
      k_b = bin(k).split('b')[1]
      if k_len==25:
        pal2 = long(k_b + k_b[::-1])**2
        if str(pal2)==str(pal2)[::-1]:
          pal_list.append(pal2)
      else:
        for c in cent:
          pal2 = long(k_b + c + k_b[::-1])**2
          if str(pal2)==str(pal2)[::-1]:
            pal_list.append(pal2)
    #also check string starting with 2, then 0s
    k_b = '2'+'0'*(k_len-1)
    if k_len==25:
      pal2 = long(k_b + k_b[::-1])**2
      if str(pal2)==str(pal2)[::-1]:
        pal_list.append(pal2)
    else:
      for c in cent:
        pal2 = long(k_b + c + k_b[::-1])**2
        if str(pal2)==str(pal2)[::-1]:
          pal_list.append(pal2)
  return pal_list

if PRE_GENERATE:
  #Pregenerate list before downloading data
  fairsquares = np.matrix(makelist())
  np.save("fairsquares.npy",fairsquares)
else:
  fairsquares = np.load("fairsquares.npy")
  fin = open("input.txt",'r')
  fout = open("output.txt",'w')
  T = int(fin.readline().strip())
  for i_case in range(T):
    AB_str = fin.readline().strip().split(' ')
    A = long(AB_str[0])
    B = long(AB_str[1])
    count = np.multiply(np.less_equal(fairsquares,B),np.greater_equal(fairsquares,A)).sum()
    out = "Case #"+str(i_case+1)+": "+str(count)+"\n"
    fout.write(out)
  fin.close()
  fout.close()

