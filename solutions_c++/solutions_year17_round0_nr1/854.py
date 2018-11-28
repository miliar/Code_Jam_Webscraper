//============================================================================
// Name        : pancake2.cpp
// Author      : Dick Carter
//============================================================================

#include <iostream>
#include <string>
using namespace std;

using size_type = string::size_type;

int main() {
	int numTests;
	cin >> numTests;
	for (int testId = 1; testId <= numTests; ++testId) {
		cout << "Case #" << testId << ": ";
		string s;
		int flipperSize;
		cin >> s >> flipperSize;
		auto numPancakes = s.size();
		size_type numFlips = 0;
		size_type leftEdge = 0;
		for (; leftEdge != numPancakes; ++leftEdge) {
//			cout << "numflips = " << numFlips << " s = " << s << endl;
			if (leftEdge + flipperSize > numPancakes) {
//				cout << "Exiting with leftEdge = " << leftEdge << " numPancakes = " << numPancakes << endl;
				break;
			}
			if (s[leftEdge] == '-') {
				++numFlips;
				for (size_type i = leftEdge; i < leftEdge + flipperSize; ++i) {
					s[i] = s[i] == '-' ? '+' : '-';
				}
			}
		}
		// No more flips possible- check last segment
		bool isPossible = true;
		while (leftEdge < numPancakes) {
			if (s[leftEdge++] == '-') {
				isPossible = false;
				break;
			}
		}
		if (isPossible)
			cout << numFlips << endl;
		else
		    cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
