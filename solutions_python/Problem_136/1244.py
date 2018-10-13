def get_current_time(farms, target, multiplier):
  denom = float(farms) * float(multiplier) + 2.0;
  return float(target) / denom;

input_file = open('B-large.in', 'r')
out = open('cookie_output.txt', 'w')
num_testcases = input_file.readline()
num_testcases = int(num_testcases)
for idx in range(0, num_testcases):
  line = input_file.readline()
  (c, f, x) = line.split()
  num_farms = 0;
  cur_time = get_current_time(num_farms, x, f);
  print "cur time ", cur_time
  new_farm_time = get_current_time(num_farms, c, f) + get_current_time(num_farms + 1, x, f)
  print "with a farm ", new_farm_time
  while cur_time >= new_farm_time:
    farm_time = get_current_time(num_farms, x, f);
    num_farms += 1
    cur_time = get_current_time(num_farms, x, f);
    print "cur time ", cur_time
    new_farm_time = get_current_time(num_farms, c, f) + get_current_time(num_farms + 1, x, f)
    print "with a farm ", new_farm_time
  elapsed_time = 0.0
  for i in range (0, num_farms):
    elapsed_time += get_current_time(i, c, f)
  ans = elapsed_time + get_current_time(num_farms, x, f)
  ans = round(ans, 7)
  out.write("Case #" + str(idx+1) + ": " + str(ans) + '\n');

