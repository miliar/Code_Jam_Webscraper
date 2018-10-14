import re;
import sys;
import io;
import math;
import fileinput
def func(argv):
	inputFile = argv[0];
	dolog_verbose(inputFile);
	
	with open(inputFile, 'r') as f:
		testCount = f.readline();
		answer = {}
		for i in range(int(testCount)):
			i+=1;
			dolog(i);
			answer[i] = solve_problems(f);

	outputFile = inputFile.replace('in','out')

	with open(outputFile, 'w') as f:
		dolog_verbose(answer);
		for k,v in answer.items():
			dolog('({0}) {1}'.format(k,v)); 
			f.write('Case #{0}: {1}\n'.format(k, v));

def solve_problems(f):
	(cost, farmProduction, goal) = getSelectedRow(f);
	time = 0;
	rate = 2;
	best = goal/rate;
	
	while True:
		time = time + cost/rate;
		rate = rate + farmProduction;
		timeToGoal = goal/rate;
		
		dolog('Best: {0: >12.7f}, New: {1: >12.7f}, Rate: {2: 12.7f}'.format(best, time + timeToGoal, rate))
		if (time + timeToGoal < best) :
			best = time + timeToGoal;
		else:
			return best;	
	return best;
		
	
def getSum(a, r, n, g):
	dolog((a*n)/(1/2*(n+1)*(r*n+4)));
	dolog(g/(2+r*(n)));
	return (a*n)/(1/2*(n+1)*(r*n+4)) + g/(2+r*(n))
		
def getClosestSum(a, r, s):
	return (math.sqrt(a*math.pow(r,2)+8*r*s-8*a*r+16*a) - math.sqrt(a) * r - math.sqrt(a)*4)/(2*r*math.sqrt(a))
	
def getSelectedRow(f):
	layout = {};
	row = f.readline().strip();
	(cost, farmProduction, goal) = row.split(' ')
	return (float(cost), float(farmProduction), float(goal))
			
testing = False;
verbose = False;

# All below here be global configs;
testing = True;
# verbose = True;

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