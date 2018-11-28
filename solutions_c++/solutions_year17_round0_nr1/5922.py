#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	int tc;
	cin >> tc;
	for (int i = 0; i < tc; i++) {
		string pancakes;
		int flipMax;
		int count = 0;
		cin >> pancakes >> flipMax;
		for (int j = 0; j < pancakes.length() - flipMax + 1; j++) {
			if (pancakes[j] == '-') {
				for (int k = j; k < j + flipMax; k++) {
					if (pancakes[k] == '-') pancakes[k] = '+';
					else if (pancakes[k] == '+') pancakes[k] = '-';
				}
				count++;
			}
		}

		bool success = true;
		for (int j = 0; j < pancakes.length(); j++) {
			if (pancakes[j] == '-') { success = false; break; }
		}

		if (success) {
			cout << "Case #" << i + 1 <<": " << count << endl;
		} else {
			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
