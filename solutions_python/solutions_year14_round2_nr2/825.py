#google code jam round 1B
#problem 2
#Joel "the man" Maupin



def num_pairs(a, b, k):
  count = 0
  for i in range(a):
    for j in range(b):
      if (i & j) < k:
        count += 1
  return count


def run_program():
  f = open("text.in", 'r')
  out = open('output.txt', 'a')
  numProblems = int(f.readline())
  for i in range(numProblems):
    line = f.readline().strip()
    each = line.split(' ')
    s = "Case #" + str(i+1) + ": " +str(num_pairs(int(each[0]), int(each[1]), int(each[2]))) + '\n'
    out.write( s)

run_program()


