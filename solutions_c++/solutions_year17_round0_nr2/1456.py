#include <bits/stdc++.h>
using namespace std;

void solve() {
	string n;
	cin >> n;
	int i = 0;
	for(int j = 1; j < n.size(); ++j) {
		if(n[j] > n[i]) {
			i = j;
		} else if(n[j] < n[i]) {
			--n[i++];
			for(; i < n.size(); ++i) {
				n[i] = '9';
			}
			break;
		}
	}
	if(n[0] == '0') {
		n = n.substr(1);
	}
	cout << ' ' << n << '\n';
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ':';
		solve();
	}
	return 0;
}
