#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sz(x) ((int)(x).size())
#define rep(i,l,r) for(int i=(l);i<(r);++i)
//-------
const int N = 107;
const int INF = 1e9 + 7;
int n, p, a[4];
int dp3[N][N][3];
int dp[N][N][N][4];
inline void _max(int &x, int y) {
	x = max(x, y);
}
int solve() {
	int ret = 0;
	if (p == 2) {
		ret = (a[1] + 1) / 2;		
	} else if (p == 3) {
		rep(i, 0, a[1] + 1)
			rep(j, 0, a[2] + 1)
				rep(k, 0, 3)
					dp3[i][j][k] = -INF;
		dp3[0][0][0] = 0;
		rep(i, 0, a[1] + 1)
			rep(j, 0, a[2] + 1)
				rep(k, 0, 3) {
					if (dp3[i][j][k] < 0)
						continue;
					if (i < a[1])
						_max(dp3[i + 1][j][(1 + k) % 3], dp3[i][j][k] + (k == 0));
					if (j < a[2])
						_max(dp3[i][j + 1][(2 + k) % 3], dp3[i][j][k] + (k == 0));
				}
		rep(i, 0, a[1] + 1)
			rep(j, 0, a[2] + 1)
				rep(k, 0, 3) 
					_max(ret, dp3[i][j][k]);	
	} else if (p == 4) {
		rep(i, 0, a[1] + 1)
			rep(j, 0, a[2] + 1)
				rep(k, 0, a[3] + 1)
					rep(r, 0, 4)
						dp[i][j][k][r] = -INF;
		dp[0][0][0][0] = 0;
		rep(i, 0, a[1] + 1)
			rep(j, 0, a[2] + 1)
				rep(k, 0, a[3] + 1) 
					rep(r, 0, 4) {
						if (dp[i][j][k] < 0)
							continue;
						if (i < a[1])
							_max(dp[i + 1][j][k][(1 + r) % 4], dp[i][j][k][r] + (1 + r) % 4 == 0);
						if (j < a[2])
							_max(dp[i][j + 1][k][(2 + r) % 4], dp[i][j][k][r] + (2 + r) % 4 == 0);
						if (k < a[3])
							_max(dp[i][j][k + 1][(3 + r) % 4], dp[i][j][k][r] + (3 + r) % 4 == 0);
					}
		rep(i, 0, a[1] + 1)
			rep(j, 0, a[2] + 1)
				rep(k, 0, a[3] + 1)
					rep(r, 0, 4)
						_max(ret, dp[i][j][k][r]);	

	}
	return ret + a[0];
}
int main() {
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(cas, 0, T) {
		scanf("%d%d", &n, &p);					
		memset(a, 0, sizeof(a));
		rep(i, 0, n) {
			int g;
			scanf("%d", &g);
			++a[g % p];
		}
//		rep(i, 0, p)
//			printf("%d ", a[i]);puts("");
		printf("Case #%d: %d\n", cas + 1, solve()); 
	}
	return 0;
}
