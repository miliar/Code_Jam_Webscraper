#!/usr/bin/python
import sys
import traceback

input_file = open(sys.argv[1])
servers = {}
max_queries = {}
results = []
try:
    try:
        line = input_file.readline()
        while (line != ''):
            num_cases = int(line.strip())

            for ii in range(0, num_cases):
                num_switches = 0
                max_queries.clear()
                servers.clear()

                line = input_file.readline()
                num_servers = int(line.strip())
                if (num_servers > 0):
                    for jj in range(0, num_servers):
                        line = input_file.readline()
                        servername = line.strip()
                        servers[servername] = 0

                    line = input_file.readline()
                    num_queries = int(line.strip())
                    for kk in range(0, num_queries):
                        line = input_file.readline()
                        query = line.strip()
                        if (query in max_queries):
                            max_queries[query] += 1
                        else:
                            max_queries[query] = 1
                        if (len(max_queries) == len(servers)):
                            num_switches += 1
                            max_queries.clear()
                            max_queries[query] = 1
                else:
                    line = input_file.readline()
                    num_queries = int(line.strip())
                    if (num_queries > 0):
                        for kk in range(1, num_queries):
                            line = input_file.readline()
                    num_switches = 0

                results.append(num_switches)
            line = input_file.readline()

        output = open("gcj_p1_a", 'w')
        for ll in range (0, len(results)):
            output.write("Case #%d: %d\n" % (ll+1, results[ll]));
        output.close()
    except Exception, e:
        traceback.print_exc(file=sys.stderr)
        print "Unexpected error: %s" % e[0]
finally:
    input_file.close()
