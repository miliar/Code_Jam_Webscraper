#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
const int maxn = 100000 + 10;
const double pi = acos(-1);

void solve(){
	int n, k;
	cin >> n >> k;

	assert(n == k);

	double u; cin >> u;
	vector<double> p(n);

	for (int i = 0; i < n; ++i){
		cin >> p[i];
	}

	double lo = 0, hi = 1.;

	for (int i = 0; i < 200; ++i){
		double m = (lo + hi) / 2;
		double v = u;

		for (int j = 0; j < n && v >= 0; ++j)
			v -= max(0., m - p[j]);

		if (v >= 0) lo = m;
		else        hi = m;
	}

	double ans = 1.;

	for (int i = 0; i < n; ++i)
		ans *= max(p[i], lo);

	cout.precision(10);
	cout << fixed << ans << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

#ifdef MARX
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

	int t; cin >> t;

	int tc = 1;

	while (t--){
		cout << "Case #" << tc++ << ": ";
		solve();
	}

	return 0;
}