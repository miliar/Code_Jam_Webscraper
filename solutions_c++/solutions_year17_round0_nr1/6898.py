#include <iostream>

using namespace std;

void solve() {
	string s;
	int k;
	cin >> s >> k;
	int ans = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '+') continue;
		if (i + k > s.size()) {
			cout << "IMPOSSIBLE" << endl;;
			return;
		}
		for (int j = 0; j < k; j++)
			if (s[i+j] == '-') s[i+j] = '+';
			else s[i+j] = '-';
		ans += 1;
	}
	cout << ans << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}	
	return 0;
}

