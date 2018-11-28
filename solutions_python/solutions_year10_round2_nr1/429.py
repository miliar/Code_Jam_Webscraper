import os
import sys
def add_directory(directory, node_structure):
    dirs = directory.strip().split('/')[1:]
    node_marker = node_structure['/']
    mkdircall_count = 0
    for dirname in dirs:
        if dirname not in node_marker:
            mkdircall_count = mkdircall_count + 1
            dir_data = {dirname : None}
            node_marker[dirname]={}
        node_marker = node_marker[dirname]
    return mkdircall_count

def file_fix(input_file, output_file):
    input_lines = open(input_file).readlines()
    tc_count = int(input_lines[0])
    counter = 0
    pos_counter = 1 
    output_data = ""
    while(counter < tc_count):
        #print input_lines[pos_counter]
        node_structure = {"/":{}}
        existing_count, new_count = map(int, input_lines[pos_counter].split())
        pos_counter = pos_counter+1
        mkdircall_count = 0
        for i in range(0, existing_count):
            add_directory(input_lines[pos_counter], node_structure)
            pos_counter = pos_counter + 1
        for i in range(0, new_count):
            mkdircall_count = mkdircall_count + add_directory(
                                                              input_lines[pos_counter], 
                                                              node_structure)
            pos_counter = pos_counter + 1
        counter = counter + 1
        output_data = output_data + "Case #%d: %s\n"%(counter, str(mkdircall_count))
   
          
    output_data = output_data.strip()
    open(output_file, 'w').write(output_data)

file_fix(sys.argv[1],sys.argv[2])
