
def createRecycled(n):
  str_n = str(n)
  for i in range(len(str_n)+1):
    yield str_n[i:] + str_n[:i] 

def get_total(a, b):
  count = 0
  for x in range(a, b+1):
    for rec in createRecycled(x):
      #print "%d < %s < %d" % (a,rec,b)
      if a <= int(rec) <= b and int(rec) > x:
        #print "(%d, %s)" % (x, rec)
        count += 1
  return count

t = get_total(10, 40)
print 3 == t, t

INPUT_FILENAME = "C-small-attempt0.in"
OUTPUT_FILENAME = "C-small-attempt0.out"
if __name__ == "__main__":
  with open(INPUT_FILENAME, 'r') as in_file:
    with open(OUTPUT_FILENAME, 'w') as out_file:
      no_of_lines = in_file.readline()
      for line_no in range(int(no_of_lines)):
        line = in_file.readline()
        split_line = line.split(' ')
        a = int(split_line[0])
        b = int(split_line[1])
        print a,b
        
        total = 0
        if not (0<=a<=9 and 0<=b<=9):
          total = get_total(a, b)
        
        out_file.write("Case #%d: %d\n" % (line_no+1, total))
