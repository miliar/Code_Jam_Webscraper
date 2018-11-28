#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define outfile "output.txt"

ofstream outs;

void main() {
	outs.open(outfile);
	if (outs.fail()) {
		cout << "Error: There was a problem opening the output file: " << outfile << endl;
		system("pause");
		return;
	}

	int t;
	long number, result;
	string numStr;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> number;

		for (long j = number; j >= 1; j--) {
			numStr = to_string(j);
			int prevDigit = (numStr[numStr.length()-1]) - '0';

			bool isTidy = true;

			for (int k = numStr.length() - 2; k >= 0; k--) {
				int first = (numStr[k] - '0');
				int second = prevDigit;
				if ((numStr[k] - '0') > prevDigit) {
					isTidy = false;
					break;
				}
				prevDigit = (numStr[k]) - '0';
			}

			if (isTidy) {
				result = j;
				break;
			}
		}

		outs << "Case #" << i << ": " << result << endl;
	}

	system("pause");
}