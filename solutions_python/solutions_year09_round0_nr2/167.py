infile = open('/home/patanjali/Desktop/B-large.in')
outfile = open('/home/patanjali/codejam/B-large.out','w')

#infile = open('/home/patanjali/Desktop/B-small-attempt0.in')
#outfile = open('/home/patanjali/codejam/B-large.out','w')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

num_cases = int(infile.readline().strip())

def update_sinks_with_new_sources(i,j, new_sources):
  if sinks[i][j]:
    sources[sinks[i][j][0]][sinks[i][j][1]].extend(new_sources)
    update_sinks_with_new_sources(sinks[i][j][0], sinks[i][j][1], new_sources)
    

for case_no in xrange(num_cases):				## Test case iterator
  print "Testing %s of %s test cases." %(case_no, num_cases)
  rows, cols = [int(x) for x in infile.readline().strip().split(' ')]
  map = []
  
  map_ = [[[(i,j)] for j in xrange(cols)] for i in xrange(rows)] ## The sink coords for each of the cells.

  sources = [[[] for j in xrange(cols)] for i in xrange(rows)]	## Sources list for each cell.
  
  sinks = [[[] for j in xrange(cols)] for i in xrange(rows)]	## Sinks list for each cell.
  
  sinks_list = []
  for row in xrange(rows):					 ## Creating the map.
    map.append([int(x) for x in infile.readline().strip().split(' ')])
    
  ## Updating the sink coords.
  for i in xrange(rows):
    for j in xrange(cols):
      sink, k, l, is_sink = map[i][j], i, j, True
      
      if i != 0:					##North
	if map[i-1][j] < sink:
	  #print "Flowing North",
	  k, l, is_sink = i-1, j, False
	  sink = map[i-1][j]
	
      if j != 0:					##West
	if map[i][j-1] < sink:
	  #print "Flowing West",
	  k, l, is_sink = i, j-1, False
	  sink = map[i][j-1]

      if j != cols-1:					##East
	if map[i][j+1] < sink:
	  #print "Flowing East",
	  k, l, is_sink = i, j+1, False
	  sink = map[i][j+1]

      if i != rows-1:					##South
	if map[i+1][j] < sink:
	  #print "Flowing South",
	  k, l, is_sink = i+1, j, False
	  sink = map[i+1][j]
      
      if is_sink:
	sinks_list.append((i,j))
      else:
	sinks[i][j] = (k,l)
	update_sinks_with_new_sources(i,j,sources[i][j]+[(i,j)])
      #print i, j, sink_
  
  ##Updating the sink indexes of the sources for each sink
  for i, j in sinks_list:
    for source in sources[i][j]:
      map_[source[0]][source[1]] = map_[i][j]




  ## Naming the sinks.
  sink_number = 0
  tt = type((1,))
  #print "Sources are"
  #for x in sources:
  #  for y in x:
  #    print y
  for i in xrange(rows):
    for j in xrange(cols):
      if type(map_[i][j][0]) == tt:
	map_[i][j][0] = alphabet[sink_number]
	sink_number += 1
  
  outfile.write('Case #%s:\n' %(case_no + 1))
  for i in xrange(rows):
    outfile.write(' '.join([x[0] for x in map_[i]])+'\n')
