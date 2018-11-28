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
		ll ac, aj; cin >> ac >> aj;
		struct D { ll c, d, p; };
		vector<D> d(ac + aj);
		REP(i, ac) {
			cin >> d[i].c >> d[i].d;
			d[i].p = 0;
		}
		REP(i, aj) {
			cin >> d[ac + i].c >> d[ac + i].d;
			d[ac + i].p = 1;
		}
		sort(ALL(d), [](D lhs, D rhs) { return lhs.c < rhs.c; });

		ll sep_num = 0;
		ll sep = 0; // ‚Ç‚¿‚ç‚ª’S“–‚µ‚Ä‚à—Ç‚¢ŽžŠÔ
		vl sep_c, sep_j; // c, j ‚ª’S“–‚·‚é‚Æ—Ç‚¢ŽžŠÔ
		REP(i, ac + aj) {
			ll range;
			if (i == 0) {
				if (d[ac + aj - 1].d < d[i].c) {
					range = d[i].c - d[ac + aj - 1].d;
				} else {
					range = 24 * 60 - d[ac + aj - 1].d + d[i].c;
				}
			} else {
				range = d[i].c - d[i - 1].d;
			}
			assert(range >= 0);
			ll i_prev = (ac + aj + i - 1) % (ac + aj);
			if (d[i_prev].p != d[i].p) {
				sep += range;
				sep_num++;
			} else {
				if (d[i_prev].p == 0) {
					sep_j.push_back(range);
				} else {
					sep_c.push_back(range);
				}
			}
		}

		sort(ALL(sep_c));
		sort(ALL(sep_j));

		ll timec = 0, timej = 0;
		REP(i, ac + aj) {
			ll range;
			if (d[i].d > d[i].c) {
				range = d[i].d - d[i].c;
			} else {
				range = 24 * 60 + d[i].d - d[i].c;
			}
			assert(range > 0);
			if (d[i].p == 0) {
				timej += range;
			} else {
				timec += range;
			}
		}
		ll cnum = 0, jnum = 0;
		REP(i, sep_c.size()) {
			if (timec + sep_c[i] <= 12 * 60) {
				timec += sep_c[i];
			} else {
				cnum = sep_c.size() - i;
				break;
			}
		}
		REP(i, sep_j.size()) {
			if (timej + sep_j[i] <= 12 * 60) {
				timej += sep_j[i];
			} else {
				jnum = sep_j.size() - i;
				break;
			}
		}
		cout << (cnum + jnum) * 2 + sep_num << endl;
	}
}
