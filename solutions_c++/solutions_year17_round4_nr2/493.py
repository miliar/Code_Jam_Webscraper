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

	ll T; cin >> T;
	REP(t, T) {
		cout << "Case #" << t + 1 << ": ";
		ll n, c, m; cin >> n >> c >> m;
		vl p(m), b(m);
		REP(i, m) {
			cin >> p[i] >> b[i];
			p[i]--; b[i]--;
		}
		vvl persons(c); // persons[i] : 客iの予約している席のリスト
		REP(i, m) persons[b[i]].push_back(p[i]);
		vvl tickets(n); // tickets[i] : 席iを予約している人のリスト
		REP(i, m) tickets[p[i]].push_back(b[i]);

		ll num = 0;
		REP(i, c) num = max<ll>(num, persons[i].size());
		{
			ll sum = 0;
			REP(i, n) {
				sum += tickets[i].size();
				num = max<ll>(num, sum / (i + 1) + (sum % (i + 1) != 0));
			}
		}

		ll ans = 0;
		REP(i, n) ans += max(0ll, tickets[i].size() - num);
		cout << num << " " << ans << endl;
		//cout << persons[0].size() << " " << persons[1].size() << " " << m << endl;
		//cout << tickets[0].size() << " " << tickets[1].size() << endl;
	}

	return 0;
}
