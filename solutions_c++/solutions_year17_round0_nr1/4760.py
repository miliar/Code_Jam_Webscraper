#include <iostream>
#include <vector>
#include <string>

using namespace std;

int lastNegativeIndex = 0;
int cantNegatives;

char flipSingle(char c) {

	if (c == '+') {
		cantNegatives++;
		return '-';
	}
	cantNegatives--;
	return '+';
}

void flip(string& pank, int first, int cant) {

	int last = first + cant;

	if (last > pank.size()) {
		first = first - (last % pank.size());
		last = first + cant;
	}

	for (int i = first; i < last; ++i) {
		pank[i] = flipSingle(pank[i]);
	}
}

int getFirstPanksToFlip(const string& s) {


	int size = s.size();
	for (int i = 0; i < size; i++) {
		if (s[i] == '-') {
			return i;
		}
	}
}

int countNegatives(const string& s) {

	for (char c : s)
		if (c == '-')
			cantNegatives++;
}

int main(int argc, char* argv[]) {


	int testCases = 0;
	cin >> testCases;

	int n = 0, flipCount = 0;
	string pank;
	for (int i = 0; i < testCases; i++) {

		cin >> pank >> flipCount;

		//cout << "Pancakes: " << pank << ". Count: " << flipCount << endl;
		cantNegatives = 0;
		countNegatives(pank);

		lastNegativeIndex = 0;
		int times = 0;
		while (cantNegatives > 0) {
			int firstFlipIndex = getFirstPanksToFlip(pank);
			//cout << "Times: " << times << ". Pank: " << pank << ". First index: " << firstFlipIndex << endl;
			if (firstFlipIndex < lastNegativeIndex) {
				times = -1;
				break;
			}
			++times;
			lastNegativeIndex = firstFlipIndex;
			flip(pank, firstFlipIndex, flipCount);
		}

		cout << "Case #" << i + 1 << ": " << ((times == -1) ? "IMPOSSIBLE" : to_string(times)) << endl;

		pank.clear();
	}
}