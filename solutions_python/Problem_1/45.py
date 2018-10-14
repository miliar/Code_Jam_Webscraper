import sys

sys.setrecursionlimit( 10000 )

case=0
cases=int( sys.__stdin__.readline() )
while case < cases:
	case+=1
	
	engine=0
	engines_c=int( sys.__stdin__.readline() )
	engines=[]
	while engine < engines_c:
		engines.append( sys.__stdin__.readline().rstrip() )
		engine+=1
	
	request=0
	requests_c=int( sys.__stdin__.readline() )
	requests=[]
	while request < requests_c:
		requests.append( engines.index( sys.__stdin__.readline().rstrip() ) )
		request+=1

## Brute-force is ineffective =(
##
#	def find_min_switches( rqs, ngc, last_request = 0 ):
#		min_switches = -1
#		if last_request >= len( rqs ):
#			return 0
#		for ngine in range( ngc ):
#			if rqs[ last_request ] == ngine:
#				continue
#			switch = 0
#			for rq in range( last_request + 1, len( rqs ) ):
#				if rqs[ rq ] == ngine:
#					switch = find_min_switches( rqs, ngc, rq ) + 1
#			if min_switches < 0 or switch < min_switches:
#				min_switches = switch
#		return min_switches

## Greedy
	def find_min_switches( rqs, ngc, last_request = 0 ):
		max_len = -1 
		max_len_ngine = 0;
		if last_request >= len( rqs ):
			return 0
		for ngine in range( ngc ):
			if rqs[ last_request ] == ngine:
				continue
			switch = 0
			for rq in range( last_request + 1, len( rqs ) ):
				if rqs[ rq ] == ngine:
					switch = 1
					if max_len < 0 or rq > max_len:
						max_len = rq
						max_len_ngine = ngine
					break
			if not switch:
				return 0
		return 1 + find_min_switches( rqs, ngc, max_len ) 
	

	min_switches = find_min_switches( requests, engines_c )
	print "Case #%d: %d" % ( case, min_switches )


