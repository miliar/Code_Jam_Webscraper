#
# she noticed that some integers, when written in base 10 with no leading zeroes,
# have their digits sorted in non-decreasing order. Some examples of this are 
# 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that
# do not have this property, like 20, 321, 495 and 999990, are not tidy.
#
# 1 <= N <= 10**18.
# Input 
#  9
#  132
#  1000
#  7
#  1111
#  11110
#  12110
#  19110
#  10110
#  22220
#  20220
#  2222
#  2022
#  111111111111111110 	
# Output 
#  Case #1: 129
#  Case #2: 999
#  Case #3: 7
#  Case #4: 1111
#  Case #5: 9999
#  Case #6: 11999
#  Case #7: 18999
#  Case #8: 9999
#  Case #9: 19999
#  Case #10: 19999
#  Case #11: 2222
#  Case #12: 1999
#  Case #13: 99999999999999999



def problem():
	
	N = int( raw_input() )
	return count_back( N )

def is_tidy(num):
	strnum = str(num)
	if ( '0' in strnum ):
		return False

	prev = int(strnum[0])
	for d in strnum:
		if ( int(d) >= prev ):
			prev = int(d)
		else:
			return False
	return True

def count_back(num):
	while ( num > 0 ):
		if( is_tidy( num ) ):
			return num
		num = num - steps(num)

def steps(num):
	step = 0
	curr = 0
	value = 0
	mult  = 10
	if( num % 10  == 0 and num > 100 ):
		num = num / 10
		value = num % 10
		while ( num > 0 ):
			if num % 10 == value:
				curr = (num % 10)
				num /= 10
				if ( num == 0 ):
					return step
				else:
					step += curr
					step *= mult
			else:
				if step > 100:
					return step
				else:
					return 1
	return 1

 
if __name__ == '__main__':
	T = int(raw_input())
	case = 1
	while ( T > 0 ):
		print "Case #%s: %s" % ( case, problem() )
		case = case + 1
		T = T - 1
 