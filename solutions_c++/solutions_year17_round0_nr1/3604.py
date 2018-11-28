#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void solve(int testCase, ifstream &input, ofstream &output) {
	int k;
	string sequence;
	bool isPossible = true;
	int64_t count = 0;
	int64_t plusCount = 0;

	input >> sequence;
	input >> k;

	while (isPossible) {
		for (int i = 0; i < sequence.length(); i++) {
			if (sequence[i] == '-') {
				if (sequence.length() - i < k) {
					isPossible = false;
				} else {
					for (int j = i; j < i + k; j++) {
						sequence[j] = (sequence[j] == '+' ? '-' : '+');
					}

					count++;
				}

				break;
			} else {
				plusCount++;
			}
		}

		//cout << "Plus count: " << plusCount << endl;

		cout << sequence << endl;

		if (plusCount == sequence.length()) {
			break;
		}

		plusCount = 0;
	}

	output << "Case #" << testCase << ": ";

	if (!isPossible) {
		output << "IMPOSSIBLE" << endl;
	} else {
		output << count << endl;
	}
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