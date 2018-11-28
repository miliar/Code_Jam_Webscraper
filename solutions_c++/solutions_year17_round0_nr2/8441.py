#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string> 

using namespace std;  // since cin and cout are both in namespace std, this saves some text

char decrease(char x) {
	
	int value = int(x) - '0' - 1;
	return std::to_string(value)[0];
}


long long solve(std::string n) {
	// specical case n contains 0
	/*if (n.find("0") != std::string::npos) {
		// multiply "9" length - 1 times using str constructor
		auto result = std::string("9", (n.length() - 1));
		return std::stoi(result);
	}*/

	bool setTo9 = false;
	bool redo = false;
	//treat normal case
	while (true) {
		redo = false;
		setTo9 = false;
		for (int i = 0; i < n.length(); i++) {
			if (setTo9) {
				n[i] = '9';
				continue;
			}
			// check for 0
			if (n[i] == 0) {
				decrease(n[i - 1]);
				// check if n[i-1] is smaller than i-2
				redo = true;
				n[i] = '9';
				setTo9 = true;
			}

			// check for wrong order
			if (i + 1 < n.length() && n[i] > n[i + 1]) {
				// set n[i] to smaller number and the rest to 9
				n[i] = decrease(n[i]);
				setTo9 = true;
				redo = true;
			}
		}
		if (!redo)
			break;
	}
	return std::atoll(n.c_str());

}

void main() {
	int t;
	long long n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n
		cout << "Case #" << i << ": " << solve(std::to_string(n)) << endl;
	}
}
