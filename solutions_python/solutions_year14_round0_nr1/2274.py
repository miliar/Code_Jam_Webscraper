import sys

f = open(sys.argv[1], 'r')
out = open("out.txt", 'w')
num_cases = int(f.readline())

for case_num in range(1, num_cases + 1):
  possible_nums1 = set()
  answer1 = int(f.readline())
  for row in range(1, 5):
    line = f.readline()
    if row == answer1:
      [possible_nums1.add(int(num)) for num in line.split()]

  possible_nums2 = set()
  answer2 = int(f.readline())
  for row in range(1, 5):
    line = f.readline()
    if row == answer2:
      [possible_nums2.add(int(num)) for num in line.split()]

  possible_nums = possible_nums1.intersection(possible_nums2)
  output = "Volunteer cheated!"
  if len(possible_nums) == 1:
    output = str(list(possible_nums)[0])
  elif len(possible_nums) > 1:
    output = "Bad magician!"
  print "Case #" + str(case_num) + ": " + output
  out.write("Case #" + str(case_num) + ": " + output + "\n")

out.close()