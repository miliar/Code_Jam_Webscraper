

def parser(filename):

  qinput = open(filename)
  aoutput = open('output.txt', 'w')
  T = int(qinput.readline())
  string = '';

  for question in range(T):

    n1 = int(qinput.readline())
    M1 = []
    for counter in range(4):
      M1.append(list())
      line = qinput.readline();
      for char in line.split():
        M1[counter].append(int(char));
    n2 = int(qinput.readline())
    M2 = []
    for counter in range(4):
      M2.append(list())
      line = qinput.readline();
      for char in line.split():
        M2[counter].append(int(char));
    string += "Case #" + str(question+1) + ": " + solver(M1[n1-1], M2[n2-1]) + "\n"

  aoutput.write(string)
  aoutput.close()
  qinput.close()


def solver(m1, m2):

  count = 0
  number = 0
  
  for i in m1:
    if i in m2:
      count += 1
      number = i

  if count == 0:
    return "Volunteer cheated!"
  elif count == 1:
    return str(number)
  else:
    return "Bad magician!"