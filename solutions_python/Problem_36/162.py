Location = "C-large.in"

welcome = "welcome to code jam"

out = open("output3", "w")

def add(list, i):
  list[i] = list[i] + list[i - 1]

def output(line, case):
  list = []
  for i in range(0, 19):
    list.append(0)
  for j in line:
    if j == "e":
      add(list, 1)
      add(list, 6)
      add(list, 14)
    elif j == "o":
      add(list, 4)
      add(list, 9)
      add(list, 12)
    elif j == " ":
      add(list, 7)
      add(list, 10)
      add(list, 15)
    elif j == "c":
      add(list, 3)
      add(list, 11)
    elif j == "m":
      add(list, 5)
      add(list, 18)
    elif j == "t":
      add(list, 8)
    elif j == "d":
      add(list, 13)
    elif j == "j":
      add(list, 16)
    elif j == "a":
      add(list, 17)
    elif j == "l":
      add(list, 2)
    elif j == "w":
      list[0] = list[0] + 1
  out.write("Case #" + str(case + 1) + ": " + ("0000" + str(list[18]))[-4:] + "\n")

file = open(Location)
numberOfTests = int(file.readline())
for i in range(0, numberOfTests):
  line = file.readline()
  output(line, i)
file.close()
out.close()
