import sys
import heapq
size = raw_input()
a = []
for line in sys.stdin:
	a.append(line.split())

def second_highest(array_of_nums):
	# use i to block arrays of size 2 or less
    i = 0
    max_1 = max_2 = float('-inf')
    for x in array_of_nums:
        i += 1
        if x > max_2:
            if x >= max_1:
                max_1, max_2 = x, max_1            
            else:
                max_2 = x
    return max_2 if i >= 2 else None

	
def printCase(iteration, NK):
	out = "Case #" + str(iteration) + ": "
	N, K = int(NK[0]), int(NK[1])
	# used this map to keep counts of open stall groups/sections
	section_counts = {}
	section_counts[N] = 1
	# stores max value in section_counts
	first_max = N
	# stores second highest value in section_counts
	second_max = 0
	i = 0
	while (i < K):
		#print section_counts
		#print first_max
		#print second_max
		
		# look at max value in dictionary section_counts
		section_counts_first_max = section_counts[first_max]
		cur_max = first_max
		# remove max and split that section into two
		cur_max -= 1
		left, right = cur_max/2, cur_max/2
		if cur_max % 2 != 0:
			right += 1
		# increment counts in section_counts for inserted elements
		# we just use the section count for current max and split it
		# that many times by adding that count
		section_counts[left] = section_counts.get(left, 0) + section_counts_first_max
		section_counts[right] = section_counts.get(right, 0) + section_counts_first_max
		# skip unneccessary iterations
		i += section_counts_first_max
		
		# remove first_max from dictionary since it has been accounted for
		# and reset both max values
		del section_counts[first_max]
		first_max = max(second_max, left, right)
		second_max = second_highest(set([second_max, left, right]))
		
		if ( K <= i):
			print out + str(max(abs(left), abs(right))) + " " + str(min(abs(left), abs(right)))

	

for i in xrange(len(a)):
	printCase(i+1, a[i])