from copy import deepcopy
def war(naomis_blocks, kens_blocks, number_of_blocks):
	naomi_points = 0
	
	for i in range(number_of_blocks):
		naomi = naomis_blocks.pop(0)
		
		kens = [block for block in kens_blocks if block > naomi]
		if len(kens) > 0:
			ken = min(kens)
			kens_blocks.remove(ken)
		else:
			ken = min(kens_blocks)
			kens_blocks.remove(ken)
		
		
		if naomi > ken:
			naomi_points += 1
			
	return naomi_points

def deceitful_war(naomis_blocks, kens_blocks, number_of_blocks):
	naomi_points = 0
	
	for i in range(number_of_blocks):
		if max(naomis_blocks) > max(kens_blocks):
			naomi = max(naomis_blocks)
			naomis_blocks.remove(naomi)
		else:
	
	
			naomi = min(naomis_blocks)
			naomis_blocks.remove(naomi)
		
		ken_max = max(kens_blocks)
		kens_blocks.remove(ken_max)
		if len(kens_blocks) > 0:
			ken_second = max(kens_blocks)
		else:
			ken_second = ken_max
		
		if naomi < ken_max:
			ken_average = (ken_max + ken_second) / 2 
			
			naomi_told = ken_average
			if naomi_told > ken_max:
				# This will never happen
				naomi_points += 1
		else:
			naomi_points += 1
			
	return naomi_points
	
def get_user_input():
	number_of_blocks = int(raw_input(""))
	naomi_blocks = raw_input("").split(" ")
	ken_blocks = raw_input("").split(" ")
	
	naomis_blocks = [float(block) for block in naomi_blocks]
	kens_blocks = [float(block) for block in ken_blocks]
	
	return naomis_blocks, kens_blocks, number_of_blocks


def main():
	tests = int(raw_input(""))
	for i in range(tests):
		naomis_blocks, kens_blocks, blocks = get_user_input()
		war_points = war(deepcopy(naomis_blocks), deepcopy(kens_blocks), blocks)
		deceitful_war_points = deceitful_war(naomis_blocks, kens_blocks, blocks)
		print("Case #{0}: {1} {2}".format((i+1), deceitful_war_points, war_points))
	
if __name__ == "__main__":
	main()
