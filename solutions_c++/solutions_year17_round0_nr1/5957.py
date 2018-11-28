#include <iostream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <deque>
#include <string>
#include <sstream>
using namespace std;

bool happyPancakeVector(std::vector<char> pancakeVector) {
	for (int i = 0; i < pancakeVector.size(); ++i){
		if (pancakeVector[i] == '-') {
			return false;
		}
	}
	return true; 
}

char flip(char pancake) {
	if (pancake == '+'){
		return '-';
	}
	return '+';
}

bool flipPancakeVector(std::vector<char>& pancakeVector, int firstFlip, int flipperSize) {
	if (firstFlip + flipperSize > pancakeVector.size()) {
		return false;
	}
	for (int i = 0; i < flipperSize; ++i) {
		char n = flip(pancakeVector[firstFlip + i]);
		pancakeVector[firstFlip + i] = n;
	}
	return true;
}


int main(void) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
	if (!fout.is_open()) cout << "output.out swas not open successfully" << endl;
	int numCase;
	fin >> numCase;
	int i;
	string line;
	getline(fin, line);
	for (i = 0; i < numCase; i++)
	{
		getline(fin, line);
		stringstream ss(line);
		string pancake; 
		ss >> pancake; 
		int flipper; 
		ss >> flipper; 

		std::vector<char> pancakeVector(pancake.c_str(), pancake.c_str() + pancake.length() + 1);
		pancakeVector.pop_back();
		int flipCounter = 0; 
		for (int j = 0; j < pancakeVector.size(); ++j) {
			if (pancakeVector[j] == '-'){
				bool success = flipPancakeVector(pancakeVector, j, flipper);
				if (!success) {
					flipCounter = -1;
					break;
				}
				flipCounter++;
			}
		}
		fout << "Case #" << (i + 1) << ": ";
		if (flipCounter >= 0){
			fout << flipCounter << endl;
		}
		else{
			fout << "IMPOSSIBLE" << endl;
		}
	} 
	return 0;
}

