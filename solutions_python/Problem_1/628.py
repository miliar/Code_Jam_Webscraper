def number_of_switches(engines, queries):
    """Calculates a number of switches necessary for a given list of queries."""
    test_set = engines.copy()
    switches = 0
    for query in queries:
        test_set.discard(query)
        if len(test_set) == 0:
            switches += 1
            test_set = engines.copy()
            test_set.discard(query)
    return switches

def save_the_universe(input, output):
    """Processes the given input and returns the result to the given output."""
    # Prepare files
    input_file = open(input, 'r')
    output_file = open(output, 'w')
 
    n_cases = int(input_file.readline())
    for j in range(n_cases):
        # Get engine information
        n_engines = int(input_file.readline())
        engines = set()
        for i in range(n_engines):
            engines.add(input_file.readline().strip())

        # Get query information
        n_queries = int(input_file.readline())
        queries = []
        for k in range(n_queries):
            queries.append(input_file.readline().strip())

	# Write each case to a file
        output_file.write('Case #%s: %s\n' % (j+1, number_of_switches(engines, queries)))
    output_file.close()

if __name__ == '__main__':
    import sys
    try:
        input = sys.argv[1]
        output = sys.argv[2]
    except (Exception):
        print "Script should be called in format 'universe.py input output'"
        sys.exit(1)

    save_the_universe(input, output)
