
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <stdio.h>
#include <string.h>

using namespace std;

ifstream input("B-large.in");
ofstream output("B-large.out");

bool verifyInput() {
    if (!input.is_open()) {
    	cout << "input file not open " << endl;
    	return false;
    }
	if (!input.good()) {
		cout << "input not good " << endl;
		return false;
	}
	return true;
}

int main() {

	string line;
    int lineNumber = 1;
    string newLine;
    if (!verifyInput()) {
    	return 0;
    }
	// jump over first line number of test cases
	getline(input, line);
	while(!input.eof())
	{
		int lineLength;
		getline(input, line);
		if(line == "") break;

		lineLength = line.length();
		newLine = line;
		for (int i=0; i< lineLength-1; i++) {
			char lastCh = newLine.at(lineLength-1-i);
			char secondLastCh = newLine.at(lineLength-1-i-1);
			int last = lastCh - '0';
			int secondLast = secondLastCh - '0';
			if (secondLast > last) {
				last = 9;
				char buf1[5];
				itoa(last, buf1, 10);
				string newLast = string(buf1);
				newLine = newLine.replace(lineLength-1-i, 1, newLast);
				secondLast--;
				string nines;
				for (int d=0; d<=i;d++) {
					nines.append("9");
				}
				newLine = newLine.replace(lineLength-1-i, lineLength-1, nines);
				char buf2[5];
				itoa(secondLast, buf2, 10);
				string newSecondLast = string(buf2);
				newLine = newLine.replace(lineLength-1-i-1, 1, newSecondLast);
			}

		}
		// remove extra 0 from the beginning
		int nZeros=0;
		for (int j=0;j<(int)newLine.length();j++) {
			if (newLine.at(j) == '0') {
				nZeros++;
			}
			else break;
		}
		if(nZeros>0) {
			newLine.erase(0,nZeros);
		}
		output << "Case #" << lineNumber << ": " << newLine << endl;
		lineNumber++;
	}
	return 0;
}
