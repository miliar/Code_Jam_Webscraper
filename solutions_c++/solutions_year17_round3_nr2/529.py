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
const int NUM = 24 * 60 + 10;
int n, m;
int a[NUM];
int dp[NUM][NUM][2][2];
int main() {
#ifdef ACM_TEST
	freopen("in.txt", "r", stdin);
#endif
	int T; scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		memset(a, -1, sizeof(a));
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; ++i) {
			int st, ed;
			scanf("%d%d", &st, &ed);
			for(int j = st; j < ed; ++j)
				a[j] = 0;
		}
		for(int i = 0; i < m; ++i) {
			int st, ed;
			scanf("%d%d", &st, &ed);
			for(int j = st; j < ed; ++j)
				a[j] = 1;
		}
		memset(dp, 0x3f, sizeof(dp));
		dp[0][0][0][0] = 0;
		dp[0][0][1][1] = 0;
		for(int i = 0; i < 1440; ++i) {
			for(int j = 0; j <= 720; ++j) {
				if(a[i] != 1) {
					dp[i + 1][j + 1][0][0] = min(dp[i + 1][j + 1][0][0], dp[i][j][0][0]);
					dp[i + 1][j + 1][0][0] = min(dp[i + 1][j + 1][0][0], dp[i][j][1][0] + 1);
					dp[i + 1][j + 1][0][1] = min(dp[i + 1][j + 1][0][1], dp[i][j][0][1]);
					dp[i + 1][j + 1][0][1] = min(dp[i + 1][j + 1][0][1], dp[i][j][1][1] + 1);
				}
				if(a[i] != 0) {
					dp[i + 1][j][1][0] = min(dp[i + 1][j][1][0], dp[i][j][1][0]);
					dp[i + 1][j][1][0] = min(dp[i + 1][j][1][0], dp[i][j][0][0] + 1);
					dp[i + 1][j][1][1] = min(dp[i + 1][j][1][1], dp[i][j][1][1]);
					dp[i + 1][j][1][1] = min(dp[i + 1][j][1][1], dp[i][j][0][1] + 1);
				}
			}
		}
		int ans = min(min(dp[1440][720][0][0], dp[1440][720][0][1] + 1),
		              min(dp[1440][720][1][1], dp[1440][720][1][0] + 1));
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
