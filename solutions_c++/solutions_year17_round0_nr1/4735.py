#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<iomanip>
#include <cassert>
#include<algorithm>

#include<string>
#include<vector>
#include<set>
#include <queue>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())
#define mp make_pair

void solve() {
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++) {
		string s;
		int k;
		cin >> s >> k;
		bool ok = true;
		int ans = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				int b = i;
				if (b + k > s.length()) {
					b = s.length() - k;
				}
				if (b < 0) {
					ok = false;
					break;
				}
				ans++;
				for (int j = b; j < b + k; j++) {
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}

		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				ok = false;
				break;
			}
		}

		cout << "Case #" << t + 1 << ": ";
		if (!ok) {
			cout << "IMPOSSIBLE" << endl;
		}
		else cout << ans << endl;
	}
}

int main() {
#if _DEBUG
	cout << setprecision(15) << fixed;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	solve();

	return 0;
}