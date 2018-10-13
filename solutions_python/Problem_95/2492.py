dictionary = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 
		'c':'e', 'w':'f', 'l':'g', 'b':'h', 
		'k':'i', 'u':'j', 'o':'k', 'm':'l', 
		'x':'m', 's':'n', 'e':'o', 'v':'p', 
		'z':'q', 'p':'r', 'd':'s', 'r':'t', 
		'j':'u', 'g':'v', 't':'w', 'h':'x', 
		'a':'y', 'q':'z', ' ':' ', '\n':'\n'}; 

def main():
	inputList = input("A-small-attempt2.in");
	outputList = list();
	number = 1;
	for string in inputList:
		outputList.append("Case #" + str(number) + ": " + convert(string));
		number += 1;
	output(outputList);	

def convert(string):
	newString = "";
	for c in string:
		newString += dictionary[c];
	return newString;

def input(fileName):
	file = open(fileName);
	inputList = list();
	number = file.readline();
	while 1:
		line = file.readline();
		if not line:
			break;
		inputList.append(line);
	return inputList;
	
def output(outputList):
	file = open("speaking_in_tongues_output.txt", "w");
	file.writelines(outputList);
	file.close();

if __name__ == "__main__":
	main()
