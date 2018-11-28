#define DEBUG 0
#define MOD 1000000007
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve()
{
	string s;
	cin >> s;
	int e = s.size() - 1;
	bool works = true;
	//cerr << s << ' ' << works << endl;
	for (int i = 1; i < s.size(); ++i) {
		if (s[i] < s[i - 1]) {
			works = false;
			break;
		}
	}
	//cerr << s << ' ' << works << endl;
	if (works) {
		cout << s << '\n';
		return;
	}
	for (int i = 1; i < s.size(); ++i) {
		if (s[i] <= s[i - 1]) {
			e = i - 1;
			break;
		}
	}
	if (e == s.size() - 1) {
		cout << s << '\n';
	} else {
		ll a = atoll(s.substr(0, e + 1).c_str());
		string b = s.substr(e + 1);
		if (a - 1 == 0) {
			cout << string(b.size(), '9') << '\n';
		} else {
			cout << (a - 1) << string(b.size(), '9') << '\n';
		}
	}
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
