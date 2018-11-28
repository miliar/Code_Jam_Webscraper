#define DEBUG 0
#define MOD 1000000007
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

pair<int, int> p[1000];
double ms[1000];

void solve()
{
	int d, n;
	cin >> d >> n;
	for (int i = 0; i < n; ++i) {
		scanf("%d%d", &p[i].first, &p[i].second);
	}
	p[n] = {0, 1e9};
	sort(p, p + n);
	ms[0] = p[0].second;
	for (int i = 1; i < n; ++i) {
		ms[i] = min(double(p[i].second), ms[i - 1] * (d - p[i].first) / (d - p[i - 1].first));
	}
	//cout << ms[0] << ' ' << (d - p[1].first) << ' ' << (d - p[0].first) << endl;
	ms[n] = ms[n - 1] * (d - p[n].first) / (d - p[n - 1].first);
	cout << ms[n] << endl;
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
