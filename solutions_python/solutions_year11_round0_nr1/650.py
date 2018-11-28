#Bot trust
#By Sean Egan
i = 0
total_buttons = []
button_array = []
button_double_array = []
color_array = []
color_double_array = []
file_ = open('A-large.txt','r')
for line in file_:
    i = i + 1
    if (i == 1):
        total_cases = int(line)
    else:
        split_line = line.split(' ')
        for x in range(0,len(split_line)):
            if (x == 0):
                total_buttons.append(int(split_line[x]))
            elif(x % 2 == 0):
                button_array.append(int(split_line[x]))
            elif(x % 2 == 1):
                color_array.append(split_line[x])
        button_double_array.append(button_array)
        color_double_array.append(color_array)
        button_array = []
        color_array = []

for x in range (0,total_cases):
        answer = 0
        current_orange = 1
        current_blue = 1
        for i in range(0,len(button_double_array[x])):
            if(color_double_array[x][i] == 'O'):
                time_needed = abs(button_double_array[x][i] - current_orange) + 1
                current_orange = button_double_array[x][i]

                no_blue_found = True
                future_blue = 0
                for z in range(i+1,len(button_double_array[x])):
                    if (no_blue_found):
                        if(color_double_array[x][z] == 'B'):
                            no_blue_found = False
                            future_blue = button_double_array[x][z]

                if (future_blue > 0):
                    if(abs(future_blue - current_blue) <= time_needed):
                        current_blue = future_blue
                    else:
                        if(current_blue > future_blue):
                            current_blue = current_blue - time_needed
                        else:
                            current_blue = current_blue + time_needed

                
                
            elif(color_double_array[x][i] == 'B'):
                time_needed = abs(button_double_array[x][i] - current_blue) + 1
                current_blue = button_double_array[x][i]

                no_orange_found = True
                future_orange = 0                
                for z in range(i+1,len(button_double_array[x])):
                    if (no_orange_found):
                        if(color_double_array[x][z] == 'O'):
                            no_orange_found = False
                            future_orange = button_double_array[x][z]

                if (future_orange > 0):
                    if(abs(future_orange - current_orange) <= time_needed):
                        current_orange = future_orange
                    else:
                        if(current_orange > future_orange):
                            current_orange = current_orange - time_needed
                        else:
                            current_orange = current_orange + time_needed

            answer = answer + time_needed
        string_answer = "Case #{0}: {1}" .format(x+1, answer)
        print string_answer
