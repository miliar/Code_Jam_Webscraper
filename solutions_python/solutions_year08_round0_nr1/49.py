##SAVING THE UNIVERSE##

##Thomas Pollom##

def calc_num_switches(engine_list, query_list):
    """
    Given a list of engines and a list of queries, returns the minimum number of
    switches required.
    """
    num_switches = 0
    used_engines = []
    for query in query_list:
        if query not in used_engines:
            used_engines.append(query)
        if len(used_engines) == len(engine_list):
            num_switches += 1
            used_engines = []
            used_engines.append(query)
    return num_switches

# Transform file to list.

input_file = open('/Users/scotty/Desktop/input_file1.txt', 'r')
raw_lines = input_file.readlines()
input_file.close()
lines = []
for line in raw_lines:
    line = line.rstrip('\n')
    lines.append(line)

output_file = open('/Users/scotty/Desktop/output_file1.txt', 'w')

# Calculate minimum number of switches for each case. Assumes correct format for input file.

num_cases = int(lines[0])
lines_index = 1
current_case = 1
while current_case <= num_cases:
    num_engines = int(lines[lines_index])
    num_queries = int(lines[lines_index + num_engines + 1])
    engines = lines[(lines_index + 1):(lines_index + num_engines + 1)]
    queries = lines[(lines_index + num_engines + 2):(lines_index + num_engines + num_queries + 2)]
    switches = calc_num_switches(engines, queries)
    output = 'Case #%s: %s' %(current_case, switches)
    output_file.write(output)
    output_file.write('\n')
    lines_index = lines_index + num_engines + num_queries + 2
    current_case += 1

output_file.close()

print 'done'
