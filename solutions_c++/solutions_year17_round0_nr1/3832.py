#include <iostream>
#include <string>
#define DEBUG(s) 0

using namespace std;

char flip(char c) {
	return (c == '+' ? '-' : '+');
}

int main() {
	int T; cin >> T;
	for (int tC = 1; tC <= T; ++tC) {
		string pancakes;
		int k;
		cin >> pancakes >> k;
		int flipCount = 0;
		for (int toCheck = 0; toCheck <= pancakes.size() - k; ++toCheck) {
			if (pancakes[toCheck] == '+') {
				continue;
			}
			++flipCount;
			for (int toFlip = toCheck; toFlip < toCheck + k; ++toFlip) {
				pancakes[toFlip] = flip(pancakes[toFlip]);
			}
			DEBUG(cout << "flipped index " << toCheck << endl);
			DEBUG(cout << "pancakes now " << pancakes << endl);
		}

		bool stillNeg = false;
		for (int toCheck = 0; toCheck < pancakes.size(); ++toCheck) {
			if (pancakes[toCheck] == '-') {
				cout << "Case #" << tC << ": IMPOSSIBLE" << endl;
				stillNeg = true;
				break;
			}
		}

		if (!stillNeg) {
			cout << "Case #" << tC << ": " << flipCount << endl;
		}
	}
}