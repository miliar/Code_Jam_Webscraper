# inputhandler.py

def get_input(input_file):
	with open(input_file) as f:
		inputlist = f.readlines()
	
	return inputlist