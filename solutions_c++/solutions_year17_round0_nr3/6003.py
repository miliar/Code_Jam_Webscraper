#define DEBUG 0
#define MOD 1000000007
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve()
{
	int n, k;
	cin >> n >> k;
	multiset<int> s;
	s.insert(n);
	ll a, b;
	for (int i = 0; i < k; ++i) {
		auto it = s.end();
		int tmp = *--it;
		s.erase(it);
		a = tmp / 2;
		b = (tmp - 1) / 2;
		//cerr << (i + 1) << ": " << tmp << ' ' << a << ' ' << b << endl;
		s.insert(a);
		s.insert(b);
	}
	cout << a << ' ' << b << '\n';
}

int main()
{
	cerr << fixed << setprecision(0);
	cout << fixed << setprecision(20);
	if (!DEBUG) {
		freopen("in", "r", stdin);
		freopen("out2", "w", stdout);
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
