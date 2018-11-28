//============================================================================
// Name        : Startr.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool happySideUp(char c) {
	if (c=='-') {
		return false;
	} else {
		return true;
	}
}

/*void doStuff(ifstream in, ofstream out) {
	//ifstream in = *a;
	//ofstream out = *b;
	string strPancakes;
	int flipSize;
	in >> strPancakes;
	in >> flipSize;
	bool *pancakes = new bool[strPancakes.length()];
	int numPancakes = strPancakes.length();
	int numFlips = 0;
	for (int i = 0; i < numPancakes; i++) {
		pancakes[i]=happySideUp(strPancakes[i]);
	}
	for (int i = 0; i < numPancakes-flipSize+1; i++) {
		if (!pancakes[i]) {
			numFlips++;
			for (int k = 0; k < flipSize; k++) {
				pancakes[i+k]=!pancakes[i+k];
			}
		}
	}
	for (int i = 0; i < flipSize; i++) {
		if (!pancakes[i]) {
			out << "IMPOSSIBLE";
			return;
		}
	}
	out << numFlips;
	return;
}*/

int main() {
	ifstream in;
	in.open("C:\\codejam\\in.txt", ios::in);
	if (!in.is_open()) {
		cout << "error opening in" << endl;
		return -1;
	}
	ofstream out;
	out.open("C:\\codejam\\out.txt", ios::out);
	if (!out.is_open()) {
		cout << "error opening out" << endl;
		return -1;
	}
	int numCases = 0;
	in >> numCases;
	for (int i = 0; i<numCases; i++) {
		bool possible = true;
		string strPancakes;
		int flipSize;
		in >> strPancakes;
		in >> flipSize;
		bool *pancakes = new bool[strPancakes.length()];
		int numPancakes = strPancakes.length();
		int numFlips = 0;
		for (int j = 0; j < numPancakes; j++) {
			pancakes[j]=happySideUp(strPancakes[j]);
		}

		for (int j = 0; j < numPancakes-flipSize+1; j++) {
			if (!pancakes[j]) {
				numFlips++;
				for (int k = 0; k < flipSize; k++) {
					pancakes[j+k]=!pancakes[j+k];
				}
			}
			/*for (int z = 0; z < numPancakes; z++) {
				if (pancakes[z]) {
					cout << "+";
				} else
					cout << "-";
			}
			cout << endl;*/
		}
		for (int j = 0; j < flipSize; j++) {
			cout << pancakes[numPancakes-j-1] <<endl ;
			if (!pancakes[numPancakes-j-1]) {
				possible = false;
			}
		}
		out << "Case #" << i+1 << ": ";
		cout << "Case: " << i+1 << ": ";
		if (possible) {
			out << numFlips << endl;
			cout << numFlips << endl;
		} else {
			out << "IMPOSSIBLE" << endl;
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
