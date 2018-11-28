#include <fstream>
#include <iostream>
#include <string>

using namespace std;

char flip(char* ch) {
	if (*ch == '+') {
		*ch = '-';
		return '-';
	} else {
		*ch = '+';
		return '+';
	}
}

bool valid(string tstStr) {
	for (int i = 0; i < tstStr.size(); ++i) {
		if (tstStr[i] != '+') {
			return false;
		}
	}
	return true;
}

int main() {

	// Redirect cin to input file
	std::ifstream inFile("A-large.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); // Save old buf to reset at end
	std::cin.rdbuf(inFile.rdbuf()); // Redirect cin to input file

	std::ofstream outFile("output.txt");
	std::streambuf *coutbuf = std::cout.rdbuf(); // Save old buf to reset at end
	std::cout.rdbuf(outFile.rdbuf()); // Redirect cin to input file

	int noTests;
	cin >> noTests;

	for (int testNo = 1; testNo <= noTests; ++testNo) {
		string pancakes = "";
		cin >> pancakes;
		int flipSize;
		cin >> flipSize;
		int noFlips = 0;
		for (int i = 0; i + flipSize <= pancakes.size(); ++i) {
			if (pancakes[i] == '-') {
				for (int j = i; j < i + flipSize; ++j) {
					flip(&(pancakes[j]));
				}
				++noFlips;
			}
		}
		cout << "Case #" << testNo << ": ";
		if (valid(pancakes)) {
			cout << noFlips;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}

	// Reset to std I/O
	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);
}