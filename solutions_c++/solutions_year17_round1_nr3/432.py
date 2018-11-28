#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

const int64_t MX = 101;

void solve() {
	int64_t hd, ad, hk, ak, b, d;
	cin >> hd >> ad >> hk >> ak >> b >> d;
	int64_t hd0 = hd, t0 = 0, ak0 = ak;
	int64_t best = numeric_limits<int64_t>::max();
	for (int64_t nd = 0; nd <= MX; ++nd) {
		int64_t hd1 = hd0, ad1 = ad, t1 = t0;
		for (int64_t nb = 0; nb <= MX; ++nb) {
			int64_t hd2 = hd1, hk2 = hk, t2 = t1;
			for (int64_t na = 0; ; ++na) {
				if (hk2 <= ad1) {
					best = min(best, t2 + 1);
					break;
				}
				if (hd2 <= ak0) {
					hd2 = hd - ak0;
					++t2;
				}
				hk2 -= ad1;
				hd2 -= ak0;
				if (hd2 < 0) break;
				++t2;
			}
			if (hd1 <= ak0) {
				hd1 = hd - ak0;
				++t1;
			}
			ad1 += b;
			hd1 -= ak0;
			if (hd1 < 0) break;
			++t1;
		}
		if (hd0 <= ak0 - d) {
			hd0 = hd - ak0;
			++t0;
		}
		ak0 -= d;
		if (ak0 < 0) ak0 = 0;
		hd0 -= ak0;
		if (hd0 < 0) break;
		++t0;
	}
	if (best == numeric_limits<int64_t>::max())
		cout << "IMPOSSIBLE\n";
	else
		cout << best << '\n';
}

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ++ti) {
		cout << "Case #" << ti << ": ";
		solve();
	}
	return 0;
}
