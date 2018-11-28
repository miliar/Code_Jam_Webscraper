import jamio

def get_input():
    lines = jamio.get_file_lines()

    n = int(lines[0])

    engine_sets = []
    query_sets = []

    test_cases = []
    
    pos = 1
    for i in range(n):
        t = int(lines[pos])
        e = lines[pos+1:pos+1+t]
        pos += t+1
        #print q
        engine_sets +=[e]
        #print engine_sets

        t = int(lines[pos])
        q = lines[pos+1:pos+1+t]
        pos += t+1
        #print q
        query_sets +=[q]
        #print query_sets
    
    #for i in range(n):
    
    return [engine_sets, query_sets]


def output(text):
    jamio.output(text)

def find_engine(e,q):
    return list(set(e) - set(q))

def switches(e,q):
    #pass #for i in range()
    
    if len(q)==0:
        return 0

    for i in range(len(q)):
        #print q[:i]
        engine = find_engine(e,q[i:])
        if len(engine)==0: 
            continue
        else:
            return switches(e,q[:i])+1
    
    #return switches



#deal(e,q)
engine_sets,query_sets = get_input()

text = ""
for i in range(len(engine_sets)):
    ss = switches(engine_sets[i],query_sets[i])
    if ss>0:
        ss -= 1
    text += "Case #%d: %d" % (i+1, ss) + "\n"

output(text)