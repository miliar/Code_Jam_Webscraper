numtests = int(raw_input())

def print_cake(case_num,matrix,r,c):
  print "Case #"+str(case_num)+":"
  for i in range(r):
    temp_list = ''.join(matrix[i])
    print temp_list

for n in range(numtests):
  num_row,num_col = map(int,raw_input().split())
  cake = []
  initials = set()
  for i in range(num_row):
    temp_row = list(raw_input())
    cake.append(temp_row)
    for j in range(num_col):
      initials.add(temp_row[j])
  if '?' not in initials:
    print_cake(n+1,cake,num_row,num_col)
  else:
    # row wise
    for i in range(num_row):
      for j in range(num_col):
        if(cake[i][j]!='?'):
          found_letter = cake[i][j]
          tj = j-1
          while(tj>-1 and cake[i][tj]=='?'):
            cake[i][tj] = found_letter
            tj -= 1
          tj = j+1
          while(tj<num_col and cake[i][tj]=='?'):
            cake[i][tj] = found_letter
            tj += 1
    for i in range(num_row):
      for j in range(num_col):
        if(cake[i][j]!='?'):
          found_letter = cake[i][j]
          ti = i-1
          while(ti>-1 and cake[ti][j]=='?'):
            cake[ti][j] = found_letter
            ti -= 1
          ti = i+1
          while(ti<num_row and cake[ti][j]=='?'):
            cake[ti][j] = found_letter
            ti += 1
    print_cake(n+1,cake,num_row,num_col)