#! /usr/bin/python
import sys

inf = open(sys.argv[1],'r').readlines()
inf_line = 0
n = int(inf[inf_line])
inf_line += 1
output = ''
for i in range(n):
   # collect the data
   s = int(inf[inf_line])
   inf_line += 1
   engines = []
   for j in range(s):
      engines.append(inf[inf_line].strip())
      inf_line += 1
#  print engines
   q = int(inf[inf_line])
   inf_line += 1
   queries = []
   for j in range(q):
      queries.append(inf[inf_line].strip())
      inf_line += 1
#  print queries

   # figure out what to do
   query_idx = 0
   engines_to_use = []
   found = []
#  if i == 4:
#     import pdb; pdb.set_trace()
   while query_idx < q:
      query = queries[query_idx]
      
      if query not in found:
         found.append(query)
      if len(found) == s: # we've found one of each engine
         engines_to_use.append(query)
         found = [query]
      query_idx += 1
         
   output += "Case #%d: %d\n" % (i+1, len(engines_to_use)) 
#  print "searches:",s
#  print "queries:",q
#  print "engines to use:", engines_to_use
#  print "Case #%d: %d\n" % (i+1, len(engines_to_use)) 
#  user = raw_input('hit enter..')

outf = open(sys.argv[2],'w')
outf.write(output)
outf.close()
