#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define all(x) begin(x),end(x)
#define sz(x) ((int)(x).size())
#define F(i,n) for (int i = 0; i < n; ++i)
#define pb push_back
using namespace std;
typedef vector<int> vi;
typedef pair<int, int> pii;

template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) {
  s<<"[ "; for (auto it : c) s << it << " "; s<<"\b]\n";
  return s;
}

int main () {
	//ios_base::sync_with_stdio(0); cin.tie(0)
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	int _; cin >> _; for(int __ = 0; __ < _; ++__) {
	int n, k; double ma; cin >> n >> k >> ma;
	vector<double> v; v.resize(n);
	map<double, int> m;
	m[1.0] = 1;
	double t;
	while (k --> 0) {
		cin >> t; ++m[t];
	}
	while (true) {
		//for (auto meow : m) {
		//	cout << meow.fi << ' ' << meow.se << '\t';
		//}
		//cout << '\n';
		if (ma <= 0) break;
		auto it = m.begin();
		double cur = it -> fi; double ti = it -> se;
		if (cur == 1) break;
		++it;
		if ((it -> fi - cur) * ti <= ma) {
			ma -= (it -> fi - cur) * ti;
			m.erase(m.begin());
			m[m.begin() -> fi] += ti;
		} else {
			m.erase(m.begin());
			m[cur + ma / ti] += ti;
			ma = 0;
		}
	}
	double ans = 1;
	for (auto meow : m) {
		ans *= pow(meow.fi, meow.se);
	}
	cout << "Case #" << __ + 1 << ": " << fixed << setprecision(6) << ans << '\n';
	}
 	return 0;
}

