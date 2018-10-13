# Usage: python search.py <input_file> [<output_file>]
# If "output_file" isn't specified, the program simply write it to console.

import sys

input_file = open(sys.argv[1])
output_text = ""

num_tests = int( input_file.readline() )

for i in range(num_tests):
    switches = 0
    num_engines = int( input_file.readline() )
    engines = []

    for j in range(num_engines):
        engines.append( input_file.readline().split("\n")[0] )
    tmp_engines = list(engines)
    num_querys = int( input_file.readline() )

    curr_engine = ""
    for k in range(num_querys):
        query = input_file.readline().split("\n")[0]
        if(curr_engine == ""):
            if(query in engines):
                if(len(engines) > 1):
                    engines.pop( engines.index(query) )
                else:
                    curr_engine = engines[0]
                    engines = list(tmp_engines)
                    engines.pop( engines.index(curr_engine) )
        if(query == curr_engine):
            curr_engine = ""
            switches += 1

    output_text += "Case #" + str(i+1) + ": " + str(switches) + "\n"

input_file.close()

if(len(sys.argv) > 2):
    output_file = open(sys.argv[2], "w")
    output_file.write(output_text)
    output_file.close()
else:
    print output_text
