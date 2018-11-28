#include <fstream>
#include <sstream>
#include <iostream>
#include <string>

using namespace std;

// The tidy number property: for some number in base b, x_n*b^n + x_(n-1)*b^(n-1) + ... + x_1*b has x_i < x_(i-1) for all i from 2 to n

int main() {

	// Save ptr to old bufs to reset at end if needed
	std::streambuf *cinbuf = std::cin.rdbuf();
	std::streambuf *coutbuf = std::cout.rdbuf();

	// Redirect cin to input file
	std::ifstream inFile("B-large.in");
	std::cin.rdbuf(inFile.rdbuf()); // Redirect cin to input file

	std::ofstream outFile("output.txt");
	std::cout.rdbuf(outFile.rdbuf()); // Redirect cin to input file

	int noTests;
	cin >> noTests;

	for (int testNo = 1; testNo <= noTests; ++testNo) {
		string numStr;
		cin >> numStr;

		for (int i = 0; i < numStr.size() - 1; ++i) {
			if (numStr[i] > numStr[i + 1]) {
				--numStr[i];
				for (int j = i + 1; j < numStr.size(); ++j) {
					numStr[j] = '9';
				}
				i = -1; // Sets i to 0 in next iteration (i will be incremented at end of loop)
				// Important reset: decrementing the digit at i may violate tidy number property earlier in the number
			}
		}

		cout << "Case #" << testNo << ": ";
		int startI = 0;
		while (numStr[startI] == '0' && startI < numStr.size()) { // Avoid leading 0s
			++startI;
		}
		if (startI >= numStr.size()) { // All 0 digits case
			cout << "0";
		}
		for (int i = startI; i < numStr.size(); ++i) {
			cout << numStr[i];
		}
		cout << endl;

		//delete numArr;
	}

	// Reset I/O
	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);
}