#include <iostream>
#include <vector>
#include <string>

using namespace std;

int flipperMeth(int input, int length, int size) {
	int flips = 0;
	int mask = (1 << size) - 1;
	for (int i = 0; i <= length - size; i++) {
		if ((input & (1 << i)) == 0) {
			input ^= (mask << i);
			flips++;
		}
	}
	for (int i = 0; i < length; i++) {
		if ((input & (1 << i)) == 0) {
			return -1;
		}
	}
	return flips;
}

int main() {
	unsigned int T = 0;
	cin >> T;
	vector<int> pancakes;
	vector<int> flippers;
	for (unsigned int i = 0; i < T; i++) {
		string input = "";
		char space = ' ';
		int flipper = 0;
		cin >> input >> flipper;
		int pancake = 0;
		for (int k = 0; k < input.length(); k++) {
			if (input[k] == '+') {
				pancake |= 1 << k;
			}
		}
		int result = flipperMeth(pancake, input.length(), flipper);
		cout << "Case #" << (i + 1) << ": ";
		if (result > -1) {
			cout << result;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}

