#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main() {
	int numTests;

	cin >> numTests;


	for(int i = 0; i < numTests; ++i) {
		string input;

		cin >> input;

		char * input_c = new char [input.length()+1];
  		std::strcpy (input_c, input.c_str());

		int flipperSize;
		cin >> flipperSize;

		int p = 0;
		int totalFlips = 0;

		while(p < input.size()) {

			if(input_c[p] == '+') {
				++p;
			} else {
				if(input.size() - p < flipperSize) {
					break;
				}
				totalFlips++;
				for(int j = 0; j < flipperSize; ++j) {
					input_c[p+j] = (input_c[p+j] == '+') ? '-' : '+';
				}
			}
		}

		if(p == input.size()) {
			cout << "Case #" << i+1 << ": " << totalFlips << endl;
		} else {
			cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		}

		delete[] input_c;
	}
	
}