#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

string solve(string input) {
	for (int c = 0; c < input.length() -1; c++) {
		if (input[c] > input[c + 1]) {
			input[c] -= 1;
			for (int i = c + 1; i < input.length(); i++) {
				input[i] = '9';
			}
			if (c - 1 >= 0) {
				c -= 2;
			}
		}
	}
	while (input[0] == '0') {
		input.erase(input.begin());
	}
	return input;
}

void main() {
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int inputs = 0;
	string input = "";
	
	fin >> inputs;

	for (int i = 0; i < inputs; i++) {
		fin >> input;

		string output = solve(input);

		fout << "Case #" << i + 1 << ": ";
		fout << output;
		if (i + 1 < inputs) {
			fout << endl;
		}
	}

	fin.close();
	fout.close();
}