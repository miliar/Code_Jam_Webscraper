f = open('A-small-attempt0.in', 'r')
out = open('output.txt', 'w')
num_testcases = int(f.readline())
for i in range(0, num_testcases):
  first_guess = f.readline()
  rows = {}
  rows[1] = f.readline()
  rows[2] = f.readline()
  rows[3] = f.readline()
  rows[4] = f.readline()
  idx = int(first_guess)
  valid_nums = rows[idx].split()
  second = f.readline()
  rows2 = {}
  rows2[1] = f.readline()
  rows2[2] = f.readline()
  rows2[3] = f.readline()
  rows2[4] = f.readline()
  idx = int(second)
  valid2 = rows2[idx].split()
  ans = -1
  for num in valid_nums:
    if num in valid2:
      if ans < 0:
        ans = int(num)
      else:
        ans = "Bad magician!"
  if ans < 0:
    ans = "Volunteer cheated!"
  out.write("Case #" + str(i+1) + ": " + str(ans) + '\n');

