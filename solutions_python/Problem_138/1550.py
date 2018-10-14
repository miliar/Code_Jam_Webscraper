
import codecs, copy

fp = codecs.open('input.in','r','utf-8')
test_cases = int( fp.readline() )

class War( object ):

	def __init__( self, N, Nb, Kb ):

		self.N = N

		self.Nb = Nb
		self.Nb.reverse()

		self.Kb = Kb
		self.Kb.reverse()

	def play( self ):

		pts, Nidx, Kidx = 0, 0, 0
		for i in xrange( self.N ):
			
			if self.Nb[Nidx] > self.Kb[Kidx]:
				pts += 1
				Nidx += 1

			else:
				Nidx += 1
				Kidx += 1

		return pts

class DeceitfulWar( object ):

	def __init__( self, N, Nb, Kb ):

		self.N = N
		self.Nb = copy.copy( Nb )
		self.Kb = copy.copy( Kb )

	def play( self ):

		pts = 0
		for i in xrange( self.N ):

			max_kb = max( self.Kb )
			min_nb = min( self.Nb )
			next_nb_nums = [ nb for nb in self.Nb if nb > max_kb ]
			if len( next_nb_nums ) != 0:
				next_nb = min( next_nb_nums )
			else:
				next_nb = None

			if next_nb is None:
				if max_kb < min_nb:
					pts += 1

				self.Nb.remove( min_nb )
				self.Kb.remove( max_kb )
			else:
				pts += 1
				self.Nb.remove( next_nb )
				self.Kb.remove( max_kb )

		return pts

for case_number in xrange( test_cases ):

	N = int( fp.readline() )
	Nb = map( float, fp.readline().split() )
	Nb.sort()
	Kb = map( float, fp.readline().split() )
	Kb.sort()

	print 'Case #%d: %d %d' % ( case_number+1, DeceitfulWar( N, Nb, Kb ).play(), War( N, Nb, Kb ).play() )
