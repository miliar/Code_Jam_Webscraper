class Bad_Magician(Exception):
	def __init__(self):
		pass
		
class Volunteer_Cheated(Exception):
	def __init__(self):
		pass

def split_row(row):
	cards = []
	for i in range(3):
		space = row.index(" ")
		cards.append(int(row[:space]))
		row = row[space +1:]
	cards.append(int(row))
	return cards
		
def get_cards():
	rows = []
	for i in range(4):
		user_raw_input = raw_input("")
		rows.append(split_row(user_raw_input))
		if len(rows[i]) != 4:
			raise Bad_Magician()
			
	return rows	
	
		
		
def magic_trick():
	# Convert user raw_input zero indexed
	first_row = int(raw_input("")) - 1
	first_cards = get_cards()
	
	# Convert user raw_input zero indexed
	second_row = int(raw_input("")) - 1
	second_cards = get_cards()
	
	solution = [card for card in first_cards[first_row] if card in second_cards[second_row]]
	
	if len(solution) > 1:
		raise Bad_Magician()
		
	elif len(solution) < 1:
		raise Volunteer_Cheated()
	else:
		return solution[0]
	





def main():
	tests = int(raw_input(""))
	for i in range(tests):
		try:
			card = magic_trick()
			print("Case #%d: "%(i+1)+ str(card))
		except Bad_Magician as e:
			print("Case #%d: Bad magician!"%(i+1))
		except Volunteer_Cheated as e:
			print("Case #%d: Volunteer cheated!"%(i+1))
	
	
	

	
	
if __name__ == "__main__":
	main()
	
	
