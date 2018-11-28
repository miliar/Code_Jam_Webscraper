//writted by dnvtmf
#include <bits/stdc++.h>
#define INF 1000000007
#define FI first
#define SE second
#define PB push_back
#define VI vector<int>
#define MP make_pair
#define FOR(x, st, ed) for(auto x = (st); x < (ed); ++x)
#define FORE(x, st, ed) for(auto x = (st); x <= (ed); ++x)
#define CLR(arr, val) memset(arr, val, sizeof(arr))
#define INFO(tag, st, ed, x) printf("%s: ", tag); \
	FOR(_i, st, ed) cout << x[_i] << ' '; puts("");
using namespace std;
typedef long long LL;
typedef pair <int, int> PII;
const int NUM = 1010;
int d, n;
int k[NUM], s[NUM];
int main() {
#ifdef ACM_TEST
	freopen("in.txt", "r", stdin);
#endif
	int T; scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		printf("Case #%d: ", cas);
		scanf("%d%d", &d, &n);
		double t = 0.0;
		for(int i = 0; i < n; ++i) {
			scanf("%d%d", &k[i], &s[i]);
			t = max(t, 1.0 * (d - k[i]) / s[i]);
		}
		printf("%.10f\n", d / t);
	}
	return 0;
}
