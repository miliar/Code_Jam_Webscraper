class Engine(object):
    def __init__(self, name):
        self.name = name
        self.next_pos = 0

def shortest_path(engines, queries):
    position = -1
    switches = 0
    
    while not position == len(queries)-1:
        cheapest_engine = engines[0]
        for i in engines:
            try:
                i.next_pos = queries.index(i.name, position+1)

            except ValueError:
                return switches

            finally:
                if i.next_pos > cheapest_engine.next_pos:
                    cheapest_engine = i
                    
        position = cheapest_engine.next_pos - 1

        if not position == len(queries)-1:
            switches += 1

    return switches

def stuff():
    output = open("C:/output.txt", 'w')
    
    with open("C:/A-small.in") as f:
        cases = int(f.readline().rstrip("\n"))

        for i in xrange(cases):
            engines_amount = int(f.readline().rstrip("\n"))
            engines = []
            for j in xrange(engines_amount):
                engines.append(Engine(f.readline().rstrip("\n")))

            queries_amount = int(f.readline().rstrip("\n"))
            queries = []
            for j in xrange(queries_amount):
                queries.append(f.readline().rstrip("\n"))
            
            output.write("Case #%s: %s\n" % (i+1, shortest_path(engines, queries)))
            
