#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using u32 = uint32_t;
using vi = vector<int>;    using vvi = vector<vi>;
using vb = vector<bool>;   using vvb = vector<vb>;
using vl = vector<ll>;     using vvl = vector<vl>;
using vd = vector<double>; using vvd = vector<vd>;

#define MAXC(c, x) (c = max(c, x))
#define MINC(c, x) (c = min(c, x))

#define REP(i,n) for(auto i = 0 * (n), i##_len = (n); i < i##_len; ++i)
#define ALL(c) (c).begin(), (c).end()
#define FOR(i,s,n) for(ll i=s, i##_len=(ll)(n); i<i##_len; ++i)
#define TEN(x) ((ll)1e##x)
const ll mod = TEN(9) + 7;

const ll INF = 1e9;

template<typename F> double bsearch(double ok, double ng, ll loop, F f) {
	REP(i, loop) {
		double middle = (ok + ng) / 2;
		(f(middle) ? ok : ng) = middle;
	}
	return ok;
}


int main() {
	#ifdef INPUT_FROM_FILE
	ifstream cin("sample.in");
	ofstream cout("sample.out");
	#endif
	cin.tie(0);
	ios_base::sync_with_stdio(false);
	cout << fixed << setprecision(50);
	ll t; cin >> t;
	REP(_, t) {
		cout << "Case #" << _ + 1 << ": ";
		ll n, k; cin >> n >> k;
		double u; cin >> u;
		vector<double> p(n); REP(i, n) cin >> p[i];

		sort(ALL(p));
		double x = bsearch(0, TEN(10), 1000, [&](double x) {
			double v = u;
			REP(i, n) if(x > p[i]) {
				if (v < x - p[i]) return false;
				v -= x - p[i];
			}
			return true;
		});
		double ans = 1;
		REP(i, n) ans *= (x > p[i] ? min(1.0, x) : p[i]);
		cout << ans << endl;
	}
}
