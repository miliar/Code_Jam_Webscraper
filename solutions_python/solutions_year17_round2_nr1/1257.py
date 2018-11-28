import sys

def FUNC(dist, horses):
    final_speed=None
    print horses
    for horse in horses:
        horse_time=float(dist-int(horse[0]))/int(horse[1])

        speed_to_catch = dist/horse_time
        if final_speed==None or speed_to_catch<final_speed:
            final_speed=speed_to_catch
    return str(final_speed)


output = []
with open(sys.argv[1], 'rb') as input_file:
    inp = input_file.readlines()
sum_lines=1
print int(inp[0])+1
for line_num in range(1, int(inp[0])+1):
    first_data=inp[sum_lines+line_num-1].split(' ')
    print first_data
    dist=int(first_data[0])
    next_lines=int(first_data[1])
    horses=[]
    for line in range(sum_lines+line_num,sum_lines+line_num+next_lines):
        horses.append((str(inp[line]).split(' ')))
    sum_lines+=next_lines

    output.append('Case #'+str(line_num)+': '+FUNC(dist,horses))
    output.append("\r\n")
output.pop()
with open(sys.argv[2], 'wb') as out:
    out.writelines(output)
