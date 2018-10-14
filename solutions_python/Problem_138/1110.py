import sys

NaomisBloqs = []
KensBloqs = []
naomiChosen = 0
KenChosen = 0



# open file
def main ():
	
	try:
		fileIn = open( "D-large.in", "r" ) # open file in read mode
		fileOut = open ( "output.txt", "w" )		# open file in write mode
	except IOError, message: # file open failed
		print >> sys.stderr, "File could not be opened:", message
		sys.exit( 1 )

	records = fileIn.readlines()
	record = records[0]
	T = int(records[0].split()[0])

	for counter in range( 1, T + 1 ):	
		lie = 0
		naomisDeceitfulPoint = 0
		naomisWarPoint = 0
		if ( counter != 1 ):
			fileOut.write( "\n" )

		NumberOfBloqs = int ( records[ counter * 3 - 2 ].split()[0])
		NaomisBloqs = records[ counter * 3 - 1 ].split()
		KensBloqs = records[ counter * 3 ].split()

		aux = []
		for bloq in NaomisBloqs:
			aux += [float(bloq)]	
		
		NaomisBloqs = aux
		NaomisBloqs = sorted( NaomisBloqs )

		aux = []
		for bloq in KensBloqs:
			aux += [float(bloq)]	
		KensBloqs = aux
		KensBloqs = sorted( KensBloqs )					


		j = 0
		auxKen = KensBloqs
		auxNaomi = NaomisBloqs		
		
		while j < NumberOfBloqs:		
			#print "naomibloqs arriba2: ", NaomisBloqs	
			naomiChosen = NaomiPlayWar( NaomisBloqs )
			KenChosen = KenPlayWar( naomiChosen, KensBloqs )
			if naomiChosen > KenChosen:
				naomisWarPoint += 1

			KensBloqs = BurnKensBloq(KenChosen, KensBloqs)
			NaomisBloqs = BurnNaomisBloq (naomiChosen, NaomisBloqs)			
			j += 1
		

		NaomisBloqs = auxNaomi
		KensBloqs = auxKen

		#print "naomibloqs arriba: ", NaomisBloqs

		#print "------------------------------------------"
		#print "NaomisBloqs: ", NaomisBloqs
		#print "KensBloqs: ", KensBloqs
		#print "------------------------------------------\n\n"

		j = 0
		while j < NumberOfBloqs:
			"""if ( NaomisBloqs[len( NaomisBloqs ) - 1] > KensBloqs[len(KensBloqs) - 1] ):
				naomiChosen = 			
			if ( NaomisBloqs[0] < KensBloqs[ len(KensBloqs) - 1] ):
				naomiChosen = NaomiPlayDeceitfulWar( KensBloqs, NaomisBloqs )
			else:
				naomiChosen = NaomiPlayWar( NaomisBloqs ) la siguiente esta repetidaaaaaaaa"""
			#print NaomisBloqs
			naomiChosen, naomiTold = NaomiPlayDeceitfulWar( KensBloqs, NaomisBloqs, lie )
			KenChosen = KenPlayWar( naomiTold, KensBloqs )
			#print "NaomisBloqs: ", NaomisBloqs
			#print "KensBloqs: ", KensBloqs
			#print "naomiChosen: ", naomiChosen			
			#print "KenChosen: ", KenChosen			
			#print "real naomiChosen: ", naomiChosen
			if naomiChosen > KenChosen:
				naomisDeceitfulPoint += 1
			
			

			KensBloqs = BurnKensBloq(KenChosen, KensBloqs)
			NaomisBloqs = BurnNaomisBloq(naomiChosen, NaomisBloqs)			
			j += 1		
		fileOut.write( "Case #%d: %d %d" % ( counter, naomisDeceitfulPoint, naomisWarPoint	 ) )
		




def NaomiPlayWar( NaomisBloqs ):	
	return NaomisBloqs[0]

def NaomiPlayDeceitfulWar ( KensBloqs, NaomisBloqs, lie ):
	if len(KensBloqs) > 0 and not (( NaomisBloqs[len( NaomisBloqs ) - 1] > KensBloqs[len(KensBloqs) - 1] )) :
		lie += 1
		return  NaomisBloqs[0] , KensBloqs[len(KensBloqs) - 1] - 0.00000001 * lie
	if len(KensBloqs) > 0 and ( NaomisBloqs[len( NaomisBloqs ) - 1] > KensBloqs[len(KensBloqs) - 1] ):
		for i in range ( 0, len( NaomisBloqs )):
			if ( NaomisBloqs[i] > KensBloqs[0] ):
				return NaomisBloqs[i], NaomisBloqs[len(NaomisBloqs) - 1] + 0.00000007 * lie
	return NaomisBloqs[0], NaomisBloqs[0]

def BurnNaomisBloq( naomiChosen, NaomisBloqs ):		
	for i in range ( 0, len(NaomisBloqs) ):
		if naomiChosen == NaomisBloqs[i]:
			if i == 0:
				return NaomisBloqs[i+1:]
			return NaomisBloqs[:i] + NaomisBloqs[i+1:]

def KenPlayWar( naomiChosen, KensBloqs ):
	for bloq in KensBloqs:
		if (bloq > naomiChosen):
			return bloq
	return 0

def BurnKensBloq( KenChosen, KensBloqs ):
	if KenChosen == 0 and len( KensBloqs ) > 0 :
		return KensBloqs[1:]
	else:
		
		for i in range ( 0, len(KensBloqs) ):
			if KenChosen == KensBloqs[i]:
				if i == 0:					
					return KensBloqs[i+1:]
				return KensBloqs[:i] + KensBloqs[i+1:]

main()