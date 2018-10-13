def read_file(input_file):
  inputs = []
  for line in input_file:
    inputs.append(line.rstrip("\n"))
  return inputs

input_file = open("A-large.in","r")
inputs = read_file(input_file)[1:]
input_file.close()

output_file = open("large.out", "w")
j = 0
for line in inputs:
    j += 1
    split_line = line.split()
    highest_shyness = int(split_line[0])
    shyness_levels = []
    for level in split_line[1]:
        shyness_levels.append(int(level))
    clapping = 0
    plants= 0
    while clapping + plants < highest_shyness:
        for i in range (highest_shyness):
            clapping += int(shyness_levels[i])
            if clapping + plants <= i:
                plants += 1
    output_file.write("Case #"+str(j)+": "+str(plants)+"\n")

output_file.close()