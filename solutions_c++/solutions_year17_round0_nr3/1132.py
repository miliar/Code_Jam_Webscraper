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
		ll n, k; cin >> n >> k;

		ll cur_mi = n;
		ll cur_ma = n;
		ll mi_num = 0, ma_num = 1;
		ll next_mi_num = 0;
		ll next_ma_num = 0;
		while (true) {
			if (ma_num != 0) {
				if (k <= ma_num) {
					cout << (cur_ma - 1) - (cur_ma - 1) / 2 << " " << (cur_ma - 1) / 2;
					break;
				} else {
					k -= ma_num;
					if (cur_ma % 2 == 0) {
						next_mi_num += ma_num;
						next_ma_num += ma_num;
					} else {
						next_ma_num += ma_num * 2;
					}
					ma_num = 0;
				}
			} else {
				if (k <= mi_num) {
					cout << (cur_mi - 1) - (cur_mi - 1) / 2 << " " << (cur_mi - 1) / 2;
					break;
				} else {
					k -= mi_num;
					if (cur_mi % 2 == 0) {
						next_mi_num += mi_num;
						next_ma_num += mi_num;
					} else {
						next_mi_num += mi_num * 2;
					}
					mi_num = next_mi_num;
					ma_num = next_ma_num;
					next_mi_num = 0;
					next_ma_num = 0;
					cur_ma = (cur_ma - 1) - (cur_ma - 1) / 2;
					cur_mi = (cur_mi - 1) / 2;
				}
			}
		}

		cout << endl;
	}

}