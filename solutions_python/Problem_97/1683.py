import sys
import math

n = int(sys.stdin.readline())

for i in range( 1,n+1 ) :
	pairs = []	
	limits = sys.stdin.readline().split()



	A = int(limits[0])
	B = int( limits[1] )

	num = A
	while num <= B :
		#print "(num,pairs ) :",num,pairs
		#string = str( num )
		log_num = math.floor( math.log10( num ) )
		divisor = 10
		multiply = int(10**math.floor( math.log10( num ) ))
		while ( num / divisor ) > 0 :
			##print "(num,div) is :(%d,%d)"%(num,divisor)
			p = num/divisor
			if p == 0 :
				break
			q = num%divisor

			#divide = math.floor( math.log10( p ) )+1
			##print "multiply is :",multiply
			recycled = q*multiply + p
			##print "( num,recycled ) : ( %d,%d) "%( num,recycled )
			if len( str(recycled ) )  != len( str( num ) ) :
			#if math.floor( math.log10( num ) ) != math.floor( math.log10( recycled ) ) :
				##print "num digits mismatch"
				divisor*= 10
				multiply /= 10
				continue
			elif ( recycled >= A ) and ( recycled <= B ) :
				##print "check for ",(num,recycled )
				#tuples = pairs.items()
				##print "tuples are :",tuples
				a = 0
				b = 0
				if recycled > num :
					a = num
					b = recycled
				else :
					b = num
					a = recycled
				#if ( (num,recycled) in pairs ) or ( ( recycled,num ) in pairs ) or num == recycled :
				if (a,b) in pairs or a == b :
					##print "pass"
					pass
				else :
					pairs.append( (a,b) )
					##print "pairs added :",(num,recycled),pairs
			divisor *= 10
			multiply /= 10

			##print "after small while ",num,divisor

			

		num += 1


	print "Case #%d: %s"%( i,len( pairs) )
