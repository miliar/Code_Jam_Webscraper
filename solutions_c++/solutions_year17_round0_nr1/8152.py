#include <iostream>
#include <string>

using namespace std;

void solve() {
	string s;
	int k;
	cin >> s >> k;
	int n = s.size();
	int ans = 0;
	for(int i = 0; i <= n-k; i++) {
		if(s[i] == '-') {
			ans++;
			for(int j = 0; j < k; j++) {
				s[i+j] = '+' + '-' - s[i+j];
			}
		}
	}
	for(int i = n-k+1; i < n; i++) {
		if(s[i] == '-') {
			cout << "IMPOSSIBLE\n";
			return;
		}
	}
	cout << ans << '\n';
}

int main() {
	int _T;
	cin >> _T;
	for(int _i = 1; _i <= _T; _i++) {
		cout << "Case #" << _i << ": ";
		solve();
	}
}
