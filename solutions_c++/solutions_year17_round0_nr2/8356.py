#include <iostream>
#include <string>
#include <fstream>
#include <bitset>
#include <unordered_set>
#include <vector>
#include <queue>

using namespace std;

void SolveProblemCase(ifstream& input, ofstream& output)
{
	string numStr;
	input >> numStr;

	vector<uint8_t> digits(numStr.size());
	for (int i = 0; i < numStr.size(); ++i) {
		digits[i] = numStr[i] - '0';
	}

	int iDigit = 0;
	while (digits.size() - iDigit > 1)
	{
		if (digits[iDigit + 1] >= digits[iDigit]) {
			++iDigit;
		}
		else {
			digits[iDigit] -= 1;
			for (int i = iDigit + 1; i < digits.size(); ++i) {
				digits[i] = 9;
			}
			if (iDigit != 0) {
				--iDigit;
			}
		}
	}

	if (digits.size() == 1) {
		output << to_string(digits[0]);
	}
	else {
		auto numStart = find_if(digits.begin(), digits.end(), [](const uint8_t& digit) { return digit != 0; });
		for (auto it = numStart; it != digits.end(); ++it)
		{
			output << to_string(*it);
		}
	}
}

int main() {
	ifstream inFile("C:\\Users\\drobson\\Downloads\\B-large.in");

	ofstream outFile("C:\\Users\\drobson\\Documents\\CodeJam\\output.txt");

	size_t numTestCases;
	inFile >> numTestCases;

	for (auto i = 1; i <= numTestCases; ++i)
	{
		outFile << "Case #" << i << ": ";
		SolveProblemCase(inFile, outFile);
		outFile << endl;
	}

	outFile.close();

	return 0;
}