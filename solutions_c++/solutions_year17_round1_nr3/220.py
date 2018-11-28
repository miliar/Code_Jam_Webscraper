#include <bits/stdc++.h>

using namespace std;

namespace Solve {

	typedef pair<long, long> pll;

	int ans[128][128][128][128];
	long B, D, H;
	queue<tuple<long, long, long, long>> Q;

	long bfs(long hd, long ad, long hk, long ak) {
		while(Q.size()) Q.pop();
		ans[hd][ad][hk][ak] = 0;
		Q.push(make_tuple(hd, ad, hk, ak));
		while(Q.size()) {
			tie(hd, ad, hk, ak) = Q.front();
			long curans = ans[hd][ad][hk][ak];
			long nhk, nhd, nad, nak;
			Q.pop();
			// 1. Attack
			nhk = hk - ad;
			nhd = hd - ak;
			nak = ak;
			nad = ad;
			if (nhk <= 0) return curans + 1;
			if (nhd > 0 && ans[nhd][nad][nhk][nak] > curans + 1) {
				ans[nhd][nad][nhk][nak] = curans + 1;
				Q.push(make_tuple(nhd, nad, nhk, nak));
			}
			// 2. Buff
			nhk = hk;
			nhd = hd - ak;
			nak = ak;
			nad = min(ad + B, hk);
			if (nhd > 0 && ans[nhd][nad][nhk][nak] > curans + 1) {
				ans[nhd][nad][nhk][nak] = curans + 1;
				Q.push(make_tuple(nhd, nad, nhk, nak));
			}
			// 3. Heal
			nhk = hk;
			nhd = H - ak;
			nak = ak;
			nad = ad;
			if (nhd > 0 && ans[nhd][nad][nhk][nak] > curans + 1) {
				ans[nhd][nad][nhk][nak] = curans + 1;
				Q.push(make_tuple(nhd, nad, nhk, nak));
			}
			// 4. Debuff
			nhk = hk;
			nak = max(0L, ak - D);
			nhd = hd - nak;
			nad = ad;
			if (nhd > 0 && ans[nhd][nad][nhk][nak] > curans + 1) {
				ans[nhd][nad][nhk][nak] = curans + 1;
				Q.push(make_tuple(nhd, nad, nhk, nak));
			}
		}
		return -1;
	}

	void main() {
		ios::sync_with_stdio(false);
		register long i, j;
		long T;
		cin >> T;
		for (long t = 1; t <= T; ++ t) {
			long hd, ad, hk, ak;
			cin >> hd >> ad >> hk >> ak >> B >> D;
			H = hd;
			memset(ans, 0x3F, sizeof ans);
			long a = bfs(hd, ad, hk, ak);
			cout << "Case #" << t << ": ";
			if (a > 0) {
				cout << a << endl;
			} else {
				cout << "IMPOSSIBLE" << endl;
			}
		}
	}
}

int main(void) {
	Solve::main();
	return 0;
}
