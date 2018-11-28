import math
import sys

class node():
	def __init__(self):
		b_action = None
		o_action = None
		
def main():
	case = 1
	passed_first = False
	for l in sys.stdin:
		if passed_first == False:
			passed_first = True
			continue
		l = l.strip()
		l2 = l.split(' ')
		line = ""
		for i in range(1, len(l2), 2):
			line += ' '.join(l2[i: i+2]) + ", "
		line = line[0:-2]
		string = line.strip()
		buttons = string.split(',')
		buttons = [(b.strip().split(' ')[0], int(b.strip().split(' ')[1])) for b in buttons]
		all_actions = expandActions(buttons)
		o_arr = [b for b in all_actions if b[0] == 'O']
		b_arr = [b for b in all_actions if b[0] == 'B']
		o, b = processActions(buttons, o_arr, b_arr)
		print "Case #" + str(case) + ":", len(o)
		case += 1
	
def processActions(buttons, o_acts, b_acts):
	button_index = 0
	p = "PUSH"
	m = "MOVE"
	o_final = []
	b_final = []
	o_len = len(o_acts)
	b_len = len(b_acts)
	o = 0
	b = 0
	
	while o < o_len or b < b_len:
		pushed = 0
		if o >= o_len:
			if len(o_acts) == 0:
				o_final.append(("STAY", 1))
			else:
				o_final.append(("STAY", o_acts[-1][-1]))
		else:
			#Moving
			if o_acts[o][1] == "MOVE":
				o_final.append(("MOVE", o_acts[o][2]))
				o += 1
			#Pushing buttons or staying
			elif buttons[button_index][0] == "B" and o_acts[o][1] == "PUSH":
				o_final.append(("STAY", o_acts[o][2]))
			elif buttons[button_index][0] == "O" and o_acts[o][1] == "PUSH":
				o_final.append(("PUSH", o_acts[o][2]))
				o += 1
				pushed = 1
		
		if b >= b_len:
			if len(b_acts) == 0:
				b_final.append(("STAY", 1))
			else:
				b_final.append(("STAY", b_acts[-1][-1]))
		else:
			#Moving
			if b_acts[b][1] == "MOVE":
				b_final.append(("MOVE", b_acts[b][2]))
				b += 1
			#Pushing buttons or staying
			elif buttons[button_index][0] == "O" and b_acts[b][1] == "PUSH":
				b_final.append(("STAY", b_acts[b][2]))
			elif buttons[button_index][0] == "B" and b_acts[b][1] == "PUSH":
				b_final.append(("PUSH", b_acts[b][2]))
				b += 1
				pushed = 1
				
		button_index += pushed
	
	return(o_final, b_final)
		
def expandActions(buttons):
	last_o = 1
	last_b = 1
	new_buttons = []
	for b in buttons:
		if b[0] == 'O':
			new_button = b[1]
			delta = int(math.fabs((new_button - last_o)))
			for i in range(delta):
				d = 0
				if new_button < last_o:
					d = -1
				else:
					d = 1
				new_buttons.append(("O", "MOVE", last_o + d*i + 1))
			new_buttons.append(("O", "PUSH", new_button))
			last_o = new_button
		else:
			new_button = b[1]
			delta = int(math.fabs((new_button - last_b)))
			for i in range(delta):
				d = 0
				if new_button < last_b:
					d = -1
				else:
					d = 1
				new_buttons.append(("B", "MOVE", last_b + d*i + 1))
			new_buttons.append(("B", "PUSH", new_button))
			last_b = new_button
			
	return new_buttons
	
if __name__ == '__main__':
	main()
