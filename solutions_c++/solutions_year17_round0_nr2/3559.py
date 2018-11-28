#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void solve(int testCase, ifstream &input, ofstream &output) {
	string number;
	input >> number;

	for (int i = number.length() - 1; i > 0; i--) {
		if (number[i] < number[i - 1]) {
			number[i - 1]--;

			for (int j = i; j < number.length(); j++) {
				number[j] = '9';
			}
		}
	}

	while (number[0] == '0') {
		number.erase(0, 1);
	}

	output << "Case #" << testCase << ": " << number << endl;
}

int main(int argc, char *argv[]) {
	if (argc > 0) {
		ofstream outputFile(argv[2]);
		ifstream inputFile(argv[1]);

		int t;
		inputFile >> t;

		for (int i = 0; i < t; i++) {
			cout << "Solving case " << i + 1 << endl;

			solve(i + 1, inputFile, outputFile);
		}
	}

	return 0;
}