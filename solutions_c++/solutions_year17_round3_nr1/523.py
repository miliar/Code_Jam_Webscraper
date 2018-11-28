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
const int NUM = 100010;
int n, m;
PII a[1100];
double PI = acos(-1.0);
LL dp[1100];
int main()
{
#ifdef ACM_TEST
    freopen("in.txt", "r", stdin);
#endif
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		printf("Case #%d: ", cas);
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; ++i) {
			scanf("%d%d", &a[i].FI, &a[i].SE);
		}
		sort(a, a + n);
		memset(dp, 0, sizeof(dp));
		for(int i = 0; i < n; ++i) {
			dp[m] = max(dp[m], dp[m - 1] + 2ll * a[i].FI * a[i].SE + 1ll * a[i].FI * a[i].FI);
			for(int j = m - 1; j > 0; --j)
				dp[j] = max(dp[j], dp[j - 1] + 2ll * a[i].FI * a[i].SE);
		}
		printf("%.10f\n", PI * dp[m]);
	}
	return 0;
}
