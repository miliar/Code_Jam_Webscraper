#define DEBUG 0
#define MOD 1000000007
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve()
{
	string s;
	cin >> s;
	int k;
	cin >> k;
	int cnt = 0;
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == '-') {
			if (i + k > s.size()) {
				cout << "IMPOSSIBLE\n";
				return;
			}
			for (int j = 0; j < k; ++j) {
				s[i + j] = (s[i + j] == '-' ? '+' : '-');
			}
			++cnt;
		}
	}
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == '-') {
			cout << "IMPOSSIBLE\n";
			return;
		}
	}
	cout << cnt << '\n';
}

int main()
{
	cerr << fixed << setprecision(0);
	cout << fixed << setprecision(20);
	if (!DEBUG) {
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	}
	int _c, _start = static_cast<int>(clock());
	cin >> _c;
	for(int _cc = 1; _cc <= _c; ++_cc) {
		int _t = static_cast<int>(clock());
		cout << "Case #" << _cc << ": ";

		solve();

		cerr << "[Case #" << _cc << " complete, " << static_cast<int>(clock() - _t) << " ms, " << 100. * _cc / _c << "%]" << endl;
	}
	cerr << "Total time: " << static_cast<int>(clock() - _start) << " ms" << endl;
	return 0;
}
