import sys, os
from string import rstrip

# Returns the index of the site in sites that occurs last in queries
# Returns len(queries) if one or more sites does not occur in queries
def farthest(sites, queries):
	i = 0
	loc = {}
	for query in queries:
		if not loc.has_key(query):
			loc[query] = i
		i += 1
	farthest = 0
	for site in sites:
		if not loc.has_key(site):
			return len(queries)
		elif loc[site] > farthest:
			farthest = loc[site]
	return farthest

# Set up input file to be read
input_file = open(os.getcwd() + '/' + sys.argv[1], 'r')
# Set up output file to be written to
output_file = open(os.getcwd() + '/output.txt', 'w')

# Process the input
c = int(input_file.readline())
for i in xrange(c):
	s = input_file.readline()
	sites = []
	for j in xrange(int(s)):
		site_name = rstrip(input_file.readline(), '\n')
		sites.append(site_name)
	q = int(rstrip(input_file.readline(), '\n'))
	queries = []
	for j in xrange(int(q)):
		query_name = rstrip(input_file.readline(), '\n')
		queries.append(query_name)
	loc = 0
	switches = 0
	while loc < q:
		rem_sites = []
		rem_sites.extend(sites)
		rem_sites.remove(queries[loc])
		loc = farthest(rem_sites, queries[loc:]) + loc
		if loc < q:
			switches += 1
	output_file.write('Case #%d: %d\n' % (i + 1, switches))

# Close the input file stream
input_file.close()
# Close the output file stream
output_file.close()
