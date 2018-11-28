import sys

def analyse_case(engine_num, queries):
    engines = dict()
    switch_count = 0
    for query in queries:
        engines[query] = 1
        if len(engines) == engine_num:
            switch_count += 1
	    engines.clear()
            engines[query] = 1
    return switch_count


if __name__ == "__main__":
    input_file = file(sys.argv[1], "r")
    lines = input_file.readlines()
    case_num = int(lines[0])
    offset = 1
    for case in range(1, case_num + 1):
        engine_num = int(lines[0 + offset])
        queries_num = int(lines[engine_num + 1 + offset])
        queries = lines[(2 + engine_num + offset) : (2 + engine_num + queries_num + offset)]
        print "Case #%d: %d" % (case, analyse_case(engine_num, queries))
        offset += 2 + engine_num + queries_num
        

