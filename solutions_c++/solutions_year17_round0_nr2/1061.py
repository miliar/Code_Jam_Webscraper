#include <bits/stdc++.h>
using namespace std;

#ifdef HELTHAZAR
	#define DEBUG true
#else
	#define DEBUG false
#endif

#define dout if (DEBUG) cout

void solve() {
	string number;
	cin >> number;

	string tidy = string(number.length(), '0');

	for (int i = 0; i < number.length(); i++) {
		for (int j = tidy[i]; j <= '9'; j++) {
			bool can = true;
			for (int k = i; k < number.length(); k++) {
				if (j > number[k]) {
					can = false;
					break;
				}
				else if (j < number[k]) {
					break;
				}
			}
			for (int k = i; k < number.length(); k++) {
				if (can) {
					tidy[k] = j;
				}
			}
		}
		if (tidy[i] < number[i]) {
			for (int k = i + 1; k < number.length(); k++) {
				number[k] = '9';
			}
		}
	}

	while (tidy[0] == '0') {
		tidy.erase(0, 1);
	}

	cout << tidy;
}

int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		//printf("\n");
	}
}
