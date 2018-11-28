fileinput = "A-large.in"
fileoutput = "A-large.out"

f = file(fileinput)
data = f.read()
f.close()

output = ""

def array_contains(array,element):
    try:
        if array.index(element) > -1:
            return True
        else: return False
    except:
        return False

lines = data.split("\n")

cases = int(lines[0])

cindex = 0
cindex += 1
for case in range(1,cases + 1):
    
    search_engines_num = int(lines[cindex])
        
    search_engines = lines[cindex + 1:cindex + 1 + search_engines_num]

    cindex += (len(search_engines) + 1)

    queries_num = int(lines[cindex])
    queries = lines[cindex + 1:cindex + 1 + queries_num]

    cindex += (len(queries) + 1)

    #Processing
    switches = 0
    temp_search_engines = []

    last_query = ""

    for q in queries:

        if (q == last_query):continue
        
        if not array_contains(temp_search_engines,q):
            temp_search_engines.append(q)
            if len(temp_search_engines) == len(search_engines):
                switches += 1
                temp_search_engines = [q]

        last_query = q


    output = output + "Case #"+str(case) + ": " + str(switches) + "\n"


f2 = file(fileoutput,"w")
f2.write(output)
f2.close()

    

    

    
    
    
    
