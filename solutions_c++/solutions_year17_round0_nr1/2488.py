#include <iostream>
#include <string>
using namespace std;

void solve() {
	string s;
	int k;
	cin >> s >> k;
	int l = s.size();
	int ans = 0;
	for (int i = 0; i+k <= l; i++) {
		if (s[i] == '+') {
			continue;
		}
		ans++;
		for (int j = 0; j < k; j++) {
			s[i+j] = ('+' + '-') - s[i+j];
		}
	}
	for (int i = l-k+1; i < l; i++) {
		if (s[i] == '-') {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << ans << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << (t+1) << ": ";
		solve();
	}
	return 0;
}
