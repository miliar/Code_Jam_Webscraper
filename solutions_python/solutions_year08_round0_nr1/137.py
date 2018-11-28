import sys;

def isInSet(p, l):
    for item in l:
        if p == item:
            return True;
    return False;

def checkEnginesNotInQueries(engines, queries):
    for engine in engines:
        if not isInSet(engine, queries):
            return True;
    return False;

def distanceToCollision(engine, queries):
    index = 0;
    while index < len(queries):
        if queries[index] == engine:
            break;
        index += 1;
    return index;
        
fNameBase = "/home/craig/projects/contests/codejam/2008/Qualify/A/A-large";

fIn = file(fNameBase + ".in");
fOut= file(fNameBase + ".out", "w");

num_tests = int(fIn.readline().strip());

current_test = 0;

num_engines = None;
engines = [];
num_queries = None;
queries = [];
while current_test < num_tests:
    num_engines = int(fIn.readline().strip());
    engines = [];
    current_read = 0;
    while current_read < num_engines:
        engines.append(fIn.readline().strip());
        current_read += 1;

    num_queries = int(fIn.readline().strip());
    queries = [];
    current_read = 0;
    while current_read < num_queries:
        queries.append(fIn.readline().strip());
        current_read += 1;

    current_max = 0;
    current_read = 0;
    if len(queries) == 0 or checkEnginesNotInQueries(engines, queries):
        current_max = 0;
    else:
        current_max = 0;
        while len(queries) > 0:
            distance = 0;
            for engine in engines:
                test_distance = distanceToCollision(engine, queries);
                if test_distance > distance:
                    distance = test_distance;
            if distance == len(queries):
                break;
            else:
	    	current_max += 1;
                queries = queries[distance:];

    fOut.write("Case #" + str(current_test + 1) + ": " + str(current_max) + "\n");
    current_test += 1;


fIn.close();
fOut.close();
