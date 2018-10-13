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

    N = list(str(get_int(stream)))
    #print N
#traitement
#==========
    
    N = map(int, N)
    
    for i in xrange(len(N)-2,-1,-1):
        #print "i = ", i
        #print "N[i:i+1]", N[i:i+1]
        
        if N[i+1]==0:
            N[i+1:]=[9]*(len(N[i+1:]))
            for j in xrange(i+1):
                if N[i+1-j]==0:
                    N[i+1-j]=9
                else:
                    N[i-j]-=1
                    break
        else:
            if N[i]<=N[i+1]:
                pass
            else:
                N[i]-=1
                N[i+1:]=[9]*(len(N[i+1:]))

    return ''.join(map(str, N)).lstrip("0")
    
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



