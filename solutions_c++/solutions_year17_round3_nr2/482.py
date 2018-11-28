#include <cstdio>
#include <algorithm>
#include <vector>
#define PI 3.1415926535897932384626433832795028841971
using namespace std;

typedef long long lint;
typedef double db;
const int N = 1450;
int a[N];
int b[N];
int dp[N][N][2];
int dp2[N][N][2];
typedef pair < lint, lint > ll;
const int INF = 98754321;

void init() {
	for (int i = 0; i < N; ++i)a[i] = b[i] = 0;

	for (int i = 0; i < N; ++i)
		dp[i][0][0] = dp2[i][0][0] = dp[i][0][1] = dp2[i][0][1]= INF;
	
	for (int i = 0; i < N; ++i)
		dp[0][i][0] = dp2[0][i][0] = dp[0][i][1] = dp2[0][i][1] = INF;
}
const int D = 720;
int go() {
	int ans[2];
	for (int i = 1; i <= D; ++i) {
		if (a[i])break;
		dp[i][0][0] = 0;
	}
	for (int i = 1; i <= D; ++i) {
		if (b[i])break;
		dp2[0][i][1] = 0;
	}
	for (int i = 1; i <= D; ++i) {
		for (int j = 1; j <= D; ++j) {
			for (int k = 0; k < 2; ++k)
				dp[i][j][k] = dp2[i][j][k] = INF;
			int t1, t2;
			if (!a[i + j]) {
				dp[i][j][0] = min(dp[i-1][j][1]+1,dp[i-1][j][0]);
				dp2[i][j][0] = min(dp2[i-1][j][1]+1,dp2[i-1][j][0]);
			}
			if (!b[i + j]) {
				dp[i][j][1] = min(dp[i][j - 1][0] + 1, dp[i][j-1][1]);
				dp2[i][j][1] = min(dp2[i][j-1][0]+1,dp2[i][j-1][1]);
			}
			//dp[i][j][0]
			//dp[i][j][1]
			//dp2[i][j][0]
			//dp2[i][j][1] 
		}
	}

	ans[0] = min(dp[D][D][0], dp2[D][D][0] + 1);
	ans[1] = min(dp[D][D][1] + 1, dp2[D][D][1]);

	return min(ans[0], ans[1]);
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i=1;i<=t;++i) {
		init();
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			int x, y;
			scanf("%d%d", &x, &y);
			for (int j = x; j < y; ++j)a[j+1] = 1;
		}

		for (int i = 0; i < m; ++i) {
			int x, y;
			scanf("%d%d", &x, &y);
			for (int j = x; j < y; ++j)b[j+1] = 1;
		}
		printf("Case #%d: %d\n",i, go());
	}
	return 0;
}