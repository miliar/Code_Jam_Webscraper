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

int main() {
	#ifdef INPUT_FROM_FILE
	ifstream cin("sample.in");
	ofstream cout("sample.out");
	#endif
	cin.tie(0);
	ios_base::sync_with_stdio(false);
	cout << fixed << setprecision(50);

	ll T; cin >> T;
	REP(t, T) {
		cout << "Case #" << t + 1 << ": ";
		ll n, q; cin >> n >> q;
		vl e(n), s(n);
		REP(i, n) cin >> e[i] >> s[i];
		vvl d(n, vl(n));
		REP(i, n) REP(j, n) cin >> d[i][j];

		vl dd(n, 0);
		FOR(i, 1, n) dd[i] = dd[i - 1] + d[i-1][i];

		ll from, to; cin >> from >> to;

		vvd tm(n, vd(n-1, TEN(15))); // tm[i‚É‚¨‚¢‚Ä][j‚Ì‚¤‚Ü‚Å“’…‚µ‚½‚Æ‚«‚ÌÅ’ZŠÔ]
		tm[0][0] = 0;
		REP(i, n-1) {
			REP(j, i) if (tm[i][j] != TEN(15)) {
				if (dd[i + 1] - dd[j] <= e[j]) {
					tm[i + 1][j] = tm[i][j] + d[i][i + 1] / (double)s[j];
				}
			}
			if (dd[i + 1] - dd[i] <= e[i]) {
				REP(j, n - 1) if (tm[i][j] != TEN(15)){
					tm[i + 1][i] = min(tm[i + 1][i], tm[i][j] + d[i][i + 1] / (double)s[i]);
				}
			}
		}
		double mi = TEN(15);
		REP(i, n-1) mi = min(mi, tm[n-1][i]);
		cout << mi << endl;
	}
}
