#!/usr/bin/python

import sys
from optparse import OptionParser


## convenience class
class TimeTable:
	def __init__( self ):
		self.times = []
	def __str__( self ):
		return str( self.times )

## error wrapper
def error( string ):
	sys.stderr.write( string )
	sys.exit( 1 )


## convert time to number of minutes 
def minutes( time_str ):
	m, s = time_str.split( ':' )
	return int( m ) * 60 + int( s )

## parse input
def parse( input ):
	it = iter( input )
	n_cases = it.next().strip()
	if not n_cases.isdigit():
		error( "ERROR parse(): expecting n_cases integer on first line\n" )
	n_cases = int( n_cases )

	timetables = []
	counter = 0
	while True:
		try:
			# turnaround time
			turnaround = it.next().strip()
			if not turnaround.isdigit():
				error( "ERROR parse(): expecting integer turnaround time, instead got:\n%s\n" % ( turnaround ) )
			turnaround = int( turnaround )

			timetable = TimeTable()
			counter += 1 

			# number of a->b, b->a
			n_a, n_b = it.next().strip().split()
			if not n_a.isdigit() or not n_b.isdigit():
				error( "ERROR parse(): error reading n_a, n_b line at line, instead found:\n%s %s\n" % ( n_a, n_b ) )
			n_a = int( n_a )
			n_b = int( n_b )

			# read n_a lines
			for i in range( n_a ):
				start, end = it.next().strip().split()
				start = minutes( start )
				end = minutes( end ) + turnaround
				timetable.times.append( ( start, end, 1 ) )

			# read n_b lines
			for i in range( n_b ):
				start, end = it.next().strip().split()
				start = minutes( start )
				end = minutes( end ) + turnaround
				timetable.times.append( ( start, end, 2 ) )

			# in-place sort times
			timetable.times.sort()

			# append to data
			timetables.append( timetable )

		except StopIteration: # end of input 
			break

	# error check
	if counter != n_cases:
		error( "ERROR parse(): only %d cases found, should be %d!\n" % ( counter, n_cases ) )

	return timetables 


## find number of minimum starting trains 
def optimal_start( timetable ):
	a = [] # track availability of next train @ city a
	b = [] # track availability of next train @ city b
	need_a = 0
	need_b = 0
	for depart, ready, dir in timetable.times:
		if dir == 1: # a -> b
			if len( a ) > 0 and a[ 0 ] <= depart:
				a = a[ 1: ]
			else:
				need_a += 1
			b.append( ready )
			b.sort()
		elif dir == 2: # b -> a
			if len( b ) > 0 and b[ 0 ] <= depart:
				b = b[ 1: ]
			else:
				need_b += 1
			a.append( ready )
			a.sort()
	return need_a, need_b


## main
if __name__ == '__main__':
	usage = "usage: %prog [OPTIONS] input_file" 
	parser = OptionParser( usage, version=0.001 )
	parser.add_option( "-o", "--output", action="store", type="string", dest="output_filename", default=None, help="output filename" )

	( options, args ) = parser.parse_args()
	if len( args ) == 0:
		parser.print_help()
		sys.exit( 1 )
	elif len( args ) < 1:
		error( "need input file" )

	out = sys.stdout
	if options.output_filename != None:
		out = open( options.output_filename, 'w' )

	f = open( args[ 0 ] )
	timetables = parse( f )
	f.close()
	
	for i in range( len( timetables ) ):
		a, b = optimal_start( timetables[ i ] )
		out.write( "Case #%d: %d %d\n" % ( i+1, a, b ) )

	out.close()

