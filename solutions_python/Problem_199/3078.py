#! /usr/bin/env python
def get_stream(file):
	for line in file:
		for token in line.strip().split():
			yield token
 
def get_int(stream):
	retour = int(stream.next())
	return retour
	
def get_str(stream):
	retour = str(stream.next())
	return retour
 
def get_solution(stream):

#mise ne forme
#=============

    S = list(get_str(stream))
    K = get_int(stream)
    #print S
    #print K
    count=0

#traitement
#==========

    for i in xrange(len(S)-K+1):
        #print "i vaut : ", i
        #print "S[i] vaut : ", S[i]
        if S[i]=='-':
            #print "S[i:i+K] = ", S[i:i+K]
            
            for j in xrange(len(S[i:i+K])):
                if S[i+j]=='-': S[i+j]='+'
                else: S[i+j]='-'
            #print "S[i:i+K] apres = ", S[i:i+K]
            count+=1
            #print "S vaut : ", S

    #print S

    if ''.join(S)=='+'*len(S): return count
    else: return "IMPOSSIBLE"
    
def main(path): 
	print "Fonction main\n"
	file = open(path, 'r')
	outfile = open(path + '.out', 'w')
	stream = get_stream(file)  
	cases = get_int(stream)
	  
	solution = []
	for case in range(0, cases):
		solution = get_solution(stream)
		buffer = "Case #" + str(case+1) + ": " + str(solution) + "\n"
		outfile.write( buffer )
		#print buffer
 
	outfile.close()

print "Appel traitement\n"
main("in")



