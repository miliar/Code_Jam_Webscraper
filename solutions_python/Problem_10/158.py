import os, sys, array

#######################################
def process(P, K, L, freq):
	
	if P * K < L:
		return "Impossible"
	
	freq.sort()
	freq.reverse()
	
	key_presses = 0
	wave = 1
	wave_index = 0
	for f in range(0, L):
		
		key_presses += freq[f] * wave
		
		wave_index += 1
		if (wave_index == K):
			wave_index = 0
			wave += 1
		
	return key_presses


#######################################
file = open("test_in.txt", "r");
fileOut = open("test_out.txt", "w");

numTasks = int(file.readline())

# ------------
for taskIndex in range(0,numTasks):
	#print "---------------"
	#print "---------------"
	#print "---------------"
	#print "--- Task", taskIndex+1
	
	
	# max letters to place on a key (P)
	# number of keys available (K)
	# number of letters in our alphabet (L)	
	
	tmp = file.readline().strip().split(" ")
	P = int(tmp[0])
	K = int(tmp[1])
	L = int(tmp[2])
	
	freq = file.readline().strip().split(" ")
	freqNr = []
	for f in freq:
		freqNr.append( int(f) )
		
	
	#print "T =", turnAroundTime
	#print "P =", P
	#print "K =", K
	#print "L =", L
	#print "Freq =", freq
	
	result = process(P, K, L, freqNr)
	print "Results:", result
	
	fileOut.write("Case #" + str(taskIndex+1) + ": " + str(result) + "\n")
	fileOut.flush()
# ------------
	
fileOut.close()
file.close()


# output:
# Case #X: Y
#
# ie:
# Case #1: 1
# Case #2: 0
