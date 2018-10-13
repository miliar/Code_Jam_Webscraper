f = open('./a-large.in.txt')
#f = open('./1-l.txt')

def remove_newline(line):
    return line.split()[0]
#lines = map(remove_newline, f.readlines())

#for line in open('./ex.txt'):
line = f.readline()
engines = set()

for case_i in range(1,int(line)+1):
    line = f.readline()
    engine_count = int(line)

    for search_engine in range(int(engine_count)):
        engine = f.readline()
        engines.add(engine)

    query_count = int(f.readline())
    occured = set()
    switch_count = 0
    for i in range(query_count):
        query = f.readline()
        occured.add(query)
        if len(occured) == engine_count:
            switch_count += 1
            occured.clear()
            occured.add(query)
    print 'Case #%d: %d'%(case_i, switch_count)
