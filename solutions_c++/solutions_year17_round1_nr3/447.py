/*input
4
11 5 16 5 0 0
3 1 3 2 2 0
3 1 3 2 1 0
2 1 5 1 1 1
*/
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;
#define sp ' '
#define endl '\n'
#define fi first
#define se second
#define mp make_pair
#define int long long
#define N 105

int dp[N][N][N][N];
int b, d;
int orh;
int cal(int hd, int ad, int hk, int ak) {
	int &ret = dp[hd][ad][hk][ak];
	if (ret != -1) return ret;
	ret = 1e18;
	int nhd = hd, nad = ad, nhk = hk, nak = ak;
	// attack
	nhk -= nad;
	if (nhk <= 0) return ret = 1;
	nhd -= nak; if (nhd > 0) ret = min(ret, 1 + cal(nhd, nad, nhk, nak));
	// buff
	nhd = hd; nad = ad; nhk = hk; nak = ak;
	nad += b; nhd -= nak; if (nhd > 0) ret = min(ret, 1 + cal(nhd, nad, nhk, nak));
	// Cure
	nhd = hd; nad = ad; nhk = hk; nak = ak;
	nhd = orh; nhd -= nak; if (nhd > 0) ret = min(ret, 1 + cal(nhd, nad, nhk, nak));
	// debuff
	nhd = hd; nad = ad; nhk = hk; nak = ak;
	nak -= d; nak = max(nak, 0LL); nhd -= nak; if (nhd > 0) ret = min(ret, 1 + cal(nhd, nad, nhk, nak));
	return ret;
}

int hd, ad, hk, ak;
signed main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef UncleGrandpa
	freopen("1test.inp", "r", stdin);
	freopen("1test.out", "w", stdout);
#endif
	int T; cin >> T;
	int ct = 0;
	while (T--) {
		ct++;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		orh = hd;
		memset(dp, -1, sizeof(dp));
		int rec = cal(hd, ad, hk, ak);
		cout << "Case #" << ct << ": ";
		if (rec >= 1e9) cout << "IMPOSSIBLE" << endl;
		else cout << rec << endl;
	}

}