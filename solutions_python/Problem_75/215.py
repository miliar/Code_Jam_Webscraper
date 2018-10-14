from sys import stdin

for k in xrange(1, 1+int(stdin.readline().strip())):
  line = stdin.readline().split()
  C = int(line[0])
  combinations = dict([("".join(sorted(z[0:2])), z[2]) for z in line[1:1+C]])
  D = int(line[C+1])
  #print k, C, D
  opposedx = line[C+2:C+D+2]
  opposed = {}
  for o in opposedx:
    if o[1] not in opposed:
      opposed[o[1]] = []
    opposed[o[1]].append(o[0])
    if o[0] not in opposed:
      opposed[o[0]] = []
    opposed[o[0]].append(o[1])
  N = int(line[C+D+2])
  elin = line[C+D+3]
  
  #print C, combinations
  #print D, opposedx, opposed
  #print N, len(elin), elin
  #print
  
  seen = {}
  output = []
  for ch in elin:
    #print "Processing " + ch + "  Output at start: " , output, "seen: ", seen
    if len(output) == 0:
      toadd = ch
    else:    
	    last2sorted = "".join(sorted([output[-1],ch]))
	    if last2sorted in combinations:
	      #print "seen: ", seen 
	      seen[output[-1]] -= 1
	      output.pop()
	      toadd=combinations[last2sorted]
	      #print "combo found: " + last2sorted + "->" + toadd
	    else:
	      toadd = ch

	    opp=False
	    if toadd in opposed:
	      #print "Oppositions found! ", 
	      for opposee in opposed[toadd]:
		#print opposee,
		if opposee in seen and seen[opposee] > 0:
		  output = []
		  seen = {}
		  opp = True
		  break
	      #print
	      
    	    if opp: continue
    
    output.append(toadd)
    if toadd not in seen: seen[toadd] = 0
    seen[toadd]+=1
  
  print "Case #" + str(k) + ": [" + ", ".join(output) + "]"
    

