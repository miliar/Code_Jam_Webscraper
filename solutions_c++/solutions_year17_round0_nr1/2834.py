#include <iostream>
#include <map>

using namespace std;

map <char, char> mp;

void solve(int test) {
	cout << "Case #" << test << ": ";
	string s;
	cin >> s;
	int n = s.size();
	
	int k;
	cin >> k;
	int cnt = 0;

	for (int i = 0; i + k - 1 < n; i++) {
		if (s[i] == '-') {
			cnt++;
			for (int j = 0; j < k; j++) {
				s[i + j] = mp[s[i + j]];
			}
		}
	}
	bool possible = true;
	for (char c : s) {
		if (c == '-') possible = false;
	}
	if (!possible) {
		cout << "IMPOSSIBLE\n";
	} else {
		cout << cnt << "\n";
	}
}

int main() {
#ifdef KOBRA
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	mp['+'] = '-';
	mp['-'] = '+';
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
	return 0;
}
