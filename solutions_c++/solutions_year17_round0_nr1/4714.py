#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void solve() {
	string pan;
	cin >> pan;
	int k;
	cin >> k;
	int res = 0;
	for (int i = 0; i < pan.size(); i++) {
		if (i + k > pan.size()) {
			if (pan[i] == '-') {
				cout << "IMPOSSIBLE";
				return;
			}
			continue;
		}
		if (pan[i] == '-') {
			for (int j = 0; j < k; j++) {
				if (pan[i+j] == '+') pan[i+j] = '-';
				else if (pan[i+j] == '-') pan[i+j] = '+';
			}
			res++;
		}
	}
	cout << res;
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