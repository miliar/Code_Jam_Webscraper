def copy_row(row0,row1,data):
  for i in range(0, len(data[row0])):
    data[row0][i] = data[row1][i]

t = int(input())
for i in range(1, t + 1):
  value = input();
  rows, columns = [int(s) for s in value.split(" ")];
  
  data = [["?" for x in range(columns)] for y in range(rows)]
  #read input
  for row in range(0, rows):
    row_data = input();
    for index in range(0, len(row_data)):
      data[row][index] = row_data[index]

  #SOLVE
  #Copy left
  changes = True
  while(changes):
    changes = False;
    for x in range(0, rows):
      for y in range(0, columns-1):
        if(data[x][y] == "?" and data[x][y+1] != "?"):
          data[x][y] = data[x][y+1]
          changes = True;
  #Copy right
  changes = True
  while(changes):
    changes = False;
    for x in range(0, rows):
      for y in range(columns-1, 0, -1):
        if(data[x][y] == "?" and data[x][y-1] != "?"):
          data[x][y] = data[x][y-1]
          changes = True;
  #Copy rows up
  changes = True
  while(changes):
    changes = False;
    for x in range(0, rows-1):
      if(data[x][0] == "?" and data[x+1][0] != "?"):
        copy_row(x,x+1,data)
        changes = True;
  #Copy rows down
  changes = True
  while(changes):
    changes = False;
    for x in range(rows-1, 0, -1):
      if(data[x][0] == "?" and data[x-1][0] != "?"):
        copy_row(x,x-1,data)
        changes = True;


  #PRINT RESULT
  print("Case #{}:".format(i));
  for x in range(0, rows):
    row = ""
    for y in range(0, columns):
      row += data[x][y]
    print(row)









