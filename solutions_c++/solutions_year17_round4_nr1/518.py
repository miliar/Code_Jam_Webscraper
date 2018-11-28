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
		ll n, p; cin >> n >> p;
		vl g(n); REP(i, n) cin >> g[i];
		if (p == 1) {
			cout << n << endl;
		} else if(p == 2) {
			ll cnt = 0;
			REP(i, n) if (g[i] % 2 == 0) cnt++;
			cout << cnt + (n - cnt) / 2 + ((n - cnt) % 2 != 0) << endl;
		} else if(p == 3){
			vl box(3, 0); REP(i, n) box[g[i] % 3]++;
			ll cnt = box[0];
			cnt += min(box[1], box[2]);
			ll rest = max(box[1], box[2]) - min(box[1], box[2]);
			cout << cnt + rest / 3 + (rest % 3 != 0) << endl;
		} else if (p == 4) {
			vl box(4, 0); REP(i, n) box[g[i] % 4]++;
			ll cnt = box[0];
			cnt += min(box[1], box[3]);
			cnt += box[2] / 2;

			ll rest = max(box[1], box[3]) - min(box[1], box[3]);
			box[2] %= 2;
			if (box[2] == 1 && rest >= 2) {
				cnt++;
				rest -= 2;
				box[2]--;
			}
			cout << cnt + rest / 4 + (rest % 4 != 0 || box[2] == 1) << endl;
		}
	}

	return 0;
}
