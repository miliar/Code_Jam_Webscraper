import re;
import sys;
import io;
import fileinput
def func(argv):
	inputFile = argv[0];
	dolog_verbose(inputFile);
	
	with open(inputFile, 'r') as f:
		testCount = f.readline();
		answer = {}
		for i in range(int(testCount)):
			i+=1;
			dolog_verbose(i);
			answer[i] = solve_problems(f);

	outputFile = inputFile.replace('in','out')

	with open(outputFile, 'w') as f:
		dolog_verbose(answer);
		for k,v in answer.items():
			dolog('({0}) {1}'.format(k,v)); 
			f.write('Case #{0}: {1}\n'.format(k, v));

def solve_problems(f):
	rowA = getSelectedRow(f);
	rowB = getSelectedRow(f);
	
	answer = set(rowA) & set(rowB)
	
	if len(answer) == 1:
		return list(answer)[0];
	if len(answer) < 1:
		return 'Volunteer cheated!';
	if len(answer) > 1:
		return 'Bad magician!';
		
def getSelectedRow(f):
	layout = {};
	rowSelection = f.readline();
	rowSelection = rowSelection.strip();
	for i in range(1,5):
		vals = readInputFileAsArray(f);
		if vals==False:
			dolog_verbose('EOF');
			break;
		dolog_verbose(vals);
		layout[i]=vals;
		
	dolog(layout);
	dolog(rowSelection);
	dolog(layout[int(rowSelection)]);
	
	return layout[int(rowSelection)];
			
# All below here be global configs;
testing = False;
verbose = False;

# All below here be util functions;
def dolog(string):
	if testing:
		print('[DOLOG]', end="");
		print(string);
		
def dolog_verbose(string):
	if verbose:
		dolog(string);

def readInputFileAsArray(fileHandle):
	line = fileHandle.readline();
	if len(line) == 0:
		return False;
	return line.strip().split(' ');

def writeArrayAsOutputFile(fileHandle, array):
	dolog_verbose(array)
	fileHandle.write(' '.join(array));

if __name__ == "__main__":
	func(sys.argv[1:])