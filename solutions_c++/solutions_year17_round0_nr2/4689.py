#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void solve() {
	string cislo;
	cin >> cislo;
	string pref = "";
	for (uint i = 1; i < cislo.size(); i++) {
		if (cislo[i] >= cislo[i-1]) continue;

		for (uint j = i; j > 0; j--) {
			if (cislo[j] > cislo[j-1]) {
				cislo[j]--;
				for (uint k = j+1; k < cislo.size(); k++) {
					cislo[k] = '9';
				}
				cout << cislo;
				return;
			}
		}
		if (cislo[0] == '1') {
			for (uint j = 0; j < cislo.size() - 1; j++) cout << '9';
				return;
		} else {
			cislo[0]--;
			for (uint k = 1; k < cislo.size(); k++) cislo[k] = '9';
			cout << cislo;
			return;
		}
	}
	cout << cislo;
}

int main() {
	int t;
	cin >> t;
	for (int i=1; i <=t; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}