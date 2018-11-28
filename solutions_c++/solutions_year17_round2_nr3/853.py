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
const int NUM = 110;
int n, q;
int E[NUM], S[NUM];
int d[NUM][NUM];
int st, ed;
LL dis[110];
double dp[110];
void small() {
	assert(st == 1 && ed == n);
	dis[1] = 0;
	for(int i = 2; i <= n; ++i)
		dis[i] = dis[i - 1] + d[i - 1][i];
//	INFO("dis", 1, n + 1, dis);
//	INFO("E", 1, n + 1, E);
//	INFO("S", 1, n + 1, S);
	for(int i = 1; i <= n; ++i)
		dp[i] = 1e20;
	dp[1] = 0.;
	for(int i = 2; i <= n; ++i) {
		for(int j = 1; j < i; ++j) {
			if(dis[i] - dis[j] <= E[j]) {
				dp[i] = min(dp[i], dp[j] + 1. * (dis[i] - dis[j]) / S[j]);
			}
		}
//		printf("at %d: %f\n", i, dp[i]);
	}
	printf(" %.10f ", dp[n]);
}
void solve() {
	scanf("%d%d", &n, &q);
	for(int i = 1; i <= n; ++i)
		scanf("%d%d", &E[i], &S[i]);
	for(int i = 1; i <= n; ++i) {
		for(int j = 1; j <= n; ++j) {
			scanf("%d", &d[i][j]);
		}
	}
	while(q--) {
		scanf("%d%d", &st, &ed);
		// for small
		small();
	}
}
int main() {
#ifdef ACM_TEST
	freopen("in.txt", "r", stdin);
#endif
	int T = 0;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		printf("Case #%d:", cas);
		solve();
		puts("");
	}
	return 0;
}
