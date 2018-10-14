# Usage: python trains.py <input_file> [<output_file>]
# If "output_file" isn't specified, the program simply write it to console.

import sys

def read_time( line ):
    global delay
    hours = line.split(" ")
    hours[0] = hours[0].split(":")
    hours[1] = hours[1].split(":")
    hours[0] = (int(hours[0][0]) * 60) + int(hours[0][1])
    hours[1] = (int(hours[1][0]) * 60) + int(hours[1][1]) + delay
    return hours

input_file = open(sys.argv[1])
output_text = ""

num_tests = int( input_file.readline() )

for i in range(num_tests):
    num_trains_a = 0
    num_trains_b = 0
    delay = int( input_file.readline().split("\n")[0] )
    num_travels = input_file.readline().split("\n")[0].split(" ")

    travels = []
    for j in range(int(num_travels[0])):
        travels.append( read_time(input_file.readline().split("\n")[0]) )
    for j in range(int(num_travels[1])):
        travels.append( read_time(input_file.readline().split("\n")[0]) )
    curr_hour = 0
    curr_trains_in_a = 0
    curr_trains_in_b = 0
    while(1):
        finished = True
        next_hour = 9999
        next = []
        for k in travels:
            if( k[0] != -1 or k[1] != -1 ):
                finished = False
            if( next_hour >= k[1] >= curr_hour ):
                next_hour = k[1]
                next = [travels.index(k),1]
            if( next_hour > k[0] >= curr_hour ):
                next_hour = k[0]
                next = [travels.index(k),0]
        if(finished):
            break
        if(next[0] < int(num_travels[0])): # From A
            if(next[1] == 0): # Start
                if( curr_trains_in_a == 0 ):
                    num_trains_a += 1
                else:
                    curr_trains_in_a -= 1
            else: # Arrive
                curr_trains_in_b += 1
        else: # From B
            if(next[1] == 0): # Start
                if( curr_trains_in_b == 0 ):
                    num_trains_b += 1
                else:
                    curr_trains_in_b -= 1
            else: # Arrive
                curr_trains_in_a += 1
        curr_hour = travels[next[0]][next[1]]
        travels[next[0]][next[1]] = -1


    output_text += "Case #" + str(i+1) + ": "
    output_text += str(num_trains_a) + " " + str(num_trains_b) + "\n"

input_file.close()

if(len(sys.argv) > 2):
    output_file = open(sys.argv[2], "w")
    output_file.write(output_text)
    output_file.close()
else:
    print output_text
