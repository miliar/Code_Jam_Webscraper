#include <iostream>
#include <string>

using namespace std;

string no_trailing_zeros(string n) {
	for (int i = 0; i < n.length(); i++) {
		if (n[i] != '0') {
			return n.substr(i);
		}
	}

	return "0";
}

int main(void) {
	int t;
	cin >> t;

	// For each test case.
	for (int tc = 1; tc <= t; tc++) {
		string n;
		cin >> n;
		n = no_trailing_zeros(n); // Maybe not necessary.

		// Just a "do it yourself" algorithm.
		for (int l = 0, r = 1; r < n.length(); l = r++) {
			while (r < n.length() and n[l] == n[r]) r++;
			if (r == n.length()) break;
			if (n[l] < n[r]) continue;

			if (n[r] == '0' and n[l] == '1') {
				n[0] = '0';
				for (int i = 1; i < n.length(); i++) n[i] = '9';
			} else {
				n[l]--;
				for (int i = l + 1; i < n.length(); i++) n[i] = '9';
			}
		}

		cout << "Case #" << tc << ": " << no_trailing_zeros(n) << endl;
	}
}