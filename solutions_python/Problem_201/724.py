def get_distance(stalls,people):
	if people == 1:
		left = (stalls-1)//2
		right = stalls-left-1
		return (left,right)

	parent, parent_order = get_parent(people)
	on_right = people<(3*parent_order)
	space = 0
	
	if on_right:
		space = get_distance(stalls,parent)[1]
	else:
		space = get_distance(stalls,parent)[0]
		
	left = (space-1)//2
	right = space-left-1
		
	return (left,right)

def get_parent(number):
	nearest_pow_2 = 2**(len(bin(number))-4)
	return (nearest_pow_2 + (number%nearest_pow_2),nearest_pow_2)
	
def main():
	cases = int(input())

	for i in range(cases):
		data = input().split(' ')
		stalls = int(data[0])
		people = int(data[1])
		skip = False
		
		
		'''if people-1 > int(stalls/2) or ((stalls % 2 == 0) and people > int(stalls/2)):
			print('Case #{}: {} {}'.format(i+1,0,0))
			continue'''
		

		small, big = get_distance(stalls,people)
			
			
		print('Case #{}: {} {}'.format(i+1,big,small))

main()		

			

	
	
	