#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define all(x) begin(x),end(x)
#define sz(x) ((int)(x).size())
#define F(i,n) for (int i = 0; i < n; ++i)
#define mp make_pair
#define double long double
using namespace std;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
 
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) {
  s<<"[ "; for (auto it : c) s << it << " "; s<<"\b]\n";
  return s;
}


int main () {
	//ios_base::sync_with_stdio(0); cin.tie(0)
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t; cin >> t; for (int tt = 0; tt < t; ++tt) {
	int n, k; cin >> n >> k;
	vector<pdd> meow;
	double PI = acos(-1);
	for (int i = 0; i < n; ++i) {
		double a, b; cin >> a >> b;
		meow.pb(mp(a, a * 2.0 * PI * b));
		//cout << a << ' ' << a * 2.0 * PI * b << '\n';;
	}
	sort(meow.begin(), meow.end());
	double ans = 0;
	double sumr = 0;
	multiset<double> s;
	for (int i = 0; i < k - 1; ++i) {
		s.insert(meow[i].se);
		sumr += meow[i].se;
	}
	for (int i = k - 1; i < n; ++i) { 
		ans = max(ans, sumr - *s.begin() + meow[i].se + meow[i].fi * meow[i].fi * PI);
		if (i == k - 1) ans = max(ans, sumr + meow[i].se + meow[i].fi * meow[i].fi * PI);
		if (i == k - 1 || meow[i].se >= *s.begin()) {
			if (i != k - 1) {
				sumr -= *s.begin();
				s.erase(*s.begin());
			}
			s.insert(meow[i].se);
			sumr += meow[i].se;
		}
	}
	cout << "Case #" << tt + 1 << ": " << fixed <<  setprecision(9) << ans << '\n';
	}
	return 0;
}

