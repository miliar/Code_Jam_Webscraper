def patrick_sum( vals ):
	j = 0
	for i in vals:
		j = j ^ i
	return j

def split_shone( vals ):
	if patrick_sum( vals ) != 0:
		return 'NO'
	else:
		vals.sort()
		vals.reverse()
		return sum( vals[0:-1] )
		
def test( count, vals ):
	count = int(count)
	vals = [ int(i) for i in vals.split( ' ' )]
	return split_shone( vals )

def main():
	data = file( "cin.txt", "r" ).readlines()
	count_tests = int(data[0])
	for i in range( 1, count_tests + 1 ):
		print 'Case #%d: %s'%( i, test( data[ i * 2 - 1 ], data[ i * 2] ))
		
if __name__ == "__main__":
	main()
