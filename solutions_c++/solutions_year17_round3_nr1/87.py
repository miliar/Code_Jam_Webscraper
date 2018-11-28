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
	ll t; cin >> t;
	REP(_, t) {
		cout << "Case #" << _ + 1 << ": ";

		ll n, k; cin >> n >> k;
		vector<pair<ll, ll>> rh(n); REP(i, n) cin >> rh[i].first >> rh[i].second;
		sort(ALL(rh), [](pair<ll, ll> lhs, pair<ll, ll> rhs) {
			if (lhs.first != rhs.first) return lhs.first > rhs.first;
			return lhs.second > rhs.second;
		});

		vvl dp(n + 1, vl(k + 1, 0));
		REP(i, n) REP(j, k) {
			ll s = rh[i].first * 2 * rh[i].second;
			if (j == 0) {
				dp[i + 1][j + 1] = max(dp[i][j + 1], s + rh[i].first * rh[i].first);
			} else {
				dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i][j] + s);
			}
		}
		cout << dp[n][k] * M_PI << endl;
	}
}
