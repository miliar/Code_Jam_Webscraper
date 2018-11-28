#include <string>
#include <iostream>
#include <sstream>

using namespace std;

int main() {
	int T; cin >> T;
	for (int tC = 1; tC <= T; ++tC) {
		string n; cin >> n;
		// one-digit numbers are always tidy
		if (n.size() == 1) {
			cout << "Case #" << tC << ": " << n << endl;
			continue;
		}
		int lastIncIdx = 0;
		for (int i = 0; i < n.size() - 1; ++i) {
			if (n[i] > n[i + 1]) {
				break;
			} else {
				++lastIncIdx;
			}
		}

		if (lastIncIdx == n.size() - 1) {
			cout << "Case #" << tC << ": " << n << endl;
			continue;
		}

		int toReplaceStart = lastIncIdx;
		while (n[toReplaceStart - 1] == n[lastIncIdx]) {
			--toReplaceStart;
		}

		//cout << "(TEMP) Case #" << tC << ": " << toReplaceStart << endl;
		cout << "Case #" << tC << ": ";
		for (int idx = 0; idx < toReplaceStart; ++idx) {
			cout << n[idx];
		}

		// print the index to replace minus 1; except if it will lead to the number
		// having leading zeros
		if (toReplaceStart != 0 || n[0] != '1') {
			cout << char(n[toReplaceStart] - 1);
		}



		for (int numFinish = toReplaceStart + 1; numFinish < n.size(); ++numFinish) {
			cout << '9';
		}

		cout << endl;
	}
	return 0;
}