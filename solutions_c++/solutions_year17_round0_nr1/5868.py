#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int caseNum = 1; caseNum <= T; caseNum++) {
		string sequence;
		int k;
		cin >> sequence >> k;
		// cout << sequence.length() << endl;
		// cout << k << endl;
		int count = 0;
		bool fail = false;
		for (int pos = 0; pos < sequence.length(); pos++) {
			// cout << "Processing " << sequence.at(pos) << endl;
			if (sequence.at(pos) == '-') {
				if (pos + k > sequence.length()) {
					fail = true;
					break;
				} else {
					count++;
					string::iterator sb = sequence.begin();
					replace(sb + pos, sb + pos + k, '-', 'p');
					replace(sb + pos, sb + pos + k, '+', 'm');
					replace(sb + pos, sb + pos + k, 'p', '+');
					replace(sb + pos, sb + pos + k, 'm', '-');
				}
			}
		}
		cout << "Case #" << caseNum << ": ";
		if (!fail) {
			cout << count << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}