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
		ll d, n; cin >> d >> n;
		double ma_time = 0;
		REP(i, n) {
			ll k, s; cin >> k >> s;
			ma_time = max(ma_time, (d - k) / (double)s);
		}
		cout << "Case #" << t + 1 << ": " << d / ma_time << endl;
	}
}
