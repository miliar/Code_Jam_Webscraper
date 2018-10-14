import math

def volume(radius, r2 = 0):
  return math.pi * ((radius - r2) * (radius + r2))
      
def solve_case(case):
  ml = int(case[1])
  radius = int(case[0])
  result = 0
  while ml > 0:
    print result
    ml -= ((radius + 1.0)**2.0 - radius**2.0)
    radius += 2
    if ml >= 0:
      result += 1
    else:
      break
  
  print result
  return result

input_file = open('small.in', 'r')
lines = input_file.readlines()
case_count = int(lines[0])
lines = lines[1:]
output = ""
for i in range(len(lines)):
  output += "Case #" + str(i + 1) + ": " + str(solve_case(lines[i].split(' '))) + '\n'

output_file = open('small.out', 'w+b')
output_file.write(output)
  
def solve_case_old(case):
  paint_volume = volume(1) * int(case[1])
  curr_area = 0
  curr_radius = int(case[0]) + 1
  result = 0
  while curr_area <= paint_volume:
    curr_area += volume(curr_radius, curr_radius - 1)
    curr_radius += 2
    if curr_area > paint_volume:
      break
    else:
      result += 1
  print result
  return result