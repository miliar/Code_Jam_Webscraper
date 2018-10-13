def num_added(content):
  data = content.split(' ');
  str = data[1].strip();
  index = 0;
  clappers = 0;
  added = 0;
  for val in str:
    while (index > clappers):
      added += 1;
      clappers += 1;
    clappers += int(val);
    index += 1;
  return added;

input = open('A-large.in', 'r');
output = open('out.txt', 'w');

case = 0;
for line in input:
  if (case != 0):
    output.write('Case #' + str(case) + ': ' + str(num_added(line)) + '\n');
  case += 1;


input.close();
output.close();