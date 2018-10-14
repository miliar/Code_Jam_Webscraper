import sys

# read the whole file specified as an argument into memory
filename = "saving_the_universe.in"
if len(sys.argv) > 1:
    filename = sys.argv[1]
lines = [line.strip() for line in open(filename)]

# process the cases
cases = int(lines[0])
offset = 1
for case in range(1, cases + 1):

    # extract the engine and query lists
    engine_count = int(lines[offset])
    engines = [lines[i] for i in range(offset + 1, offset + engine_count + 1)]
    offset = offset + engine_count + 1
    query_count = int(lines[offset])
    queries = [lines[i] for i in range(offset + 1, offset + query_count + 1)]
    offset = offset + query_count + 1

    # we need to switch every time we see all of the search engines
    switches = 0
    used_engines = set()
    for i in range(0, len(queries)-1):
        query = queries[i]
        next_query = queries[i+1]
        used_engines.add(query)
        if (next_query not in used_engines) and (len(used_engines) == engine_count - 1):
            switches = switches + 1
            used_engines = set()

    # output the results
    print "Case #%d: %d" % (case, switches)
