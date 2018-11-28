import os
import sys
import copy

def tower_intersection(input_file, output_file):
    input_lines = open(input_file).readlines()
    tc_count = int(input_lines[0])
    counter = 0
    pos_counter = 1
    output_data = ""
    while(counter < tc_count):
        #print input_lines[pos_counter]
        connection_count  = int(input_lines[pos_counter].strip())
        pos_counter = pos_counter+1
        intersection_count = 0
        connection_points = []
        destination_list = []
        for i in range(0, connection_count):
            connection_points.append(map(int, input_lines[pos_counter].split()))
            destination_list.append(int(input_lines[pos_counter].split()[1]))
            pos_counter = pos_counter + 1
        connection_points.sort()
        calc_connection_points = copy.deepcopy(connection_points)
        destination_list.sort()
        for connection_counter in range(0, connection_count):
            current_connection = connection_points[connection_counter]
            current_source_position = calc_connection_points.index(current_connection)
            current_destination_position = destination_list.index(current_connection[1])
            if current_source_position != current_destination_position :
                intersection_count = intersection_count + abs(
                                    current_destination_position - current_source_position)
            calc_connection_points.remove(current_connection)
            destination_list.remove(current_connection[1])
            
        counter = counter + 1
        output_data = output_data + "Case #%d: %s\n"%(counter, str(intersection_count))


    output_data = output_data.strip()
    open(output_file, 'w').write(output_data)

tower_intersection(sys.argv[1],sys.argv[2])
