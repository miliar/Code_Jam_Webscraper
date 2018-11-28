// q1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <cstdint>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

bool is_tidy(int64_t N) {
	while (N != 0) {
		if ((N % 10) < ((N / 10) % 10))
			return false;
		N /= 10;
	}
	return true;
}

int64_t solve(int64_t N) {
	vector<short> digits;
	while (N > 0) {
		digits.push_back(N % 10);
		N /= 10;
	}
	reverse(digits.begin(), digits.end());

	for (size_t i = 0; i < digits.size() - 1; i++) {
		if (digits[i] > digits[i + 1]) {
			// we know that digits[i] != 0, because it's greater than other digit..
			while (i > 0 && (digits[i] == digits[i - 1])) {
				i--;
			}

			digits[i] -= 1;

			for (size_t j = i + 1; j < digits.size(); j++) {
				digits[j] = 9;
			}
			break; // surely finished
		}
	}

	int64_t res = 0;
	for (size_t i = 0; i < digits.size(); i++) {
		res *= 10;
		res += digits[i];
	}

	return res;
}

int main()
{
	//string fileName = "example";
	string fileName = "B-large";
	//string fileName = "B-small-attempt0";

	ifstream inFile;
	inFile.open("..\\..\\" + fileName + ".in");
	ofstream outFile;
	outFile.open("..\\..\\" + fileName + ".out");

	size_t T;
	inFile >> T;
	for (size_t i = 0; i < T; i++) {
		int64_t N;
		inFile >> N;

		int64_t res = solve(N);
		outFile << "Case #" << (i + 1) << ": " << res << endl;
	}

	outFile.close();
	inFile.close();
	return 0;
}

