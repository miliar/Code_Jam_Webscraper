def walk(qindex):
    global result
    endindex = qindex
    while (endindex < qlen) and (len(engines - set(queries[qindex:endindex+1])) > 0):
        endindex = endindex + 1
    if (len(engines - set(queries[qindex:endindex+1])) == 0):
        result = result + 1
    return endindex
                
def switches(search_engines,queries):
    global result
    result = 0
    index = 0
    while (index < qlen):
        index = walk(index)
    return result

try: 
    import sys
    filename = sys.argv[1] 
except: 
    filename = 'A-large.in'
inputfile = open(filename)
outputfile = open('output.txt','w')    

number_of_input_sets = int(inputfile.readline()) #N
for input_set in range(number_of_input_sets):
    print input_set
    number_of_search_engines = int(inputfile.readline()) #S
    search_engines = []
    for search_engine in range(number_of_search_engines):
        search_engines.append(inputfile.readline().rstrip())
    engines = set(range(len(search_engines)))
    qlen = int(inputfile.readline()) #Q
    queries = []
    for query in range(qlen):
        queries.append(search_engines.index(inputfile.readline().rstrip()))
    output = switches(range(len(search_engines)),queries)
    outputfile.write('Case #' + str(input_set+1) + ': ' + str(output) + '\n')
    
outputfile.close()
inputfile.close()

