src_file = "input_bot.txt"
dest_file = "output_bot.txt"
press_button = 1
slack_or = last_or = slack_bl = last_bl = total_time = 0
count = -1
out_list = []
with open(src_file, 'r') as src:
    for line in src:
        count += 1
        if count > 0:
            slack_or = last_or = slack_bl = last_bl = total_time = 0
            tokens = line.split()    
            for i in range(1, len(tokens)):
                if tokens[i] == "O":
                    temp0 = abs(int(tokens[i + 1]) - 1 - last_or) - slack_or
                    temp = temp0 if temp0 > 0 else 0  
                    time = press_button + temp
                    total_time += time
                    slack_or = 0
                    slack_bl += time
                    last_or = int(tokens[i + 1]) - 1
                elif tokens[i] == "B":
                    temp0 = abs(int(tokens[i + 1]) - 1 - last_bl) - slack_bl
                    temp = temp0 if temp0 > 0 else 0  
                    time = press_button + temp    
                    total_time += time
                    slack_bl = 0
                    slack_or += time
                    last_bl = int(tokens[i + 1]) - 1
                    
            out_list.extend(["Case ", "#", str(count), ": ", str(total_time), "\n"])    
            
            
output_string = "".join(out_list)
with open(dest_file, 'w') as dest:
    dest.write(output_string.rstrip("\n"))
print "done"
