#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < n; i ++)
typedef long long LL;
const int N = 100 + 5;

struct Time {
	int s, e;
} Cbusy[N],Jbusy[N];

using namespace std;
int dp[1445][730][2][2];

void checkmin(int &x, int val) {
	if (val < 0) {
		return;
	}
	if (x < 0) {
		x = val;
		return;
	}
	x = min(x, val);
}

int busy[1444];

int main() {
	int T, n, Ac, Aj, s, t;
	scanf("%d", &T);
	rep(cas, T) {
		scanf("%d%d", &Ac, &Aj);
		rep(i, 1445) {
			rep(j, 730) {
				rep(k, 2) {
					rep(o, 2) {
						dp[i][j][k][o] = -1e9;
					}
				}
			}
		}
		memset(busy, -1, sizeof busy);
		rep(i, Ac) {
			scanf("%d%d", &s, &t);
			for (int o = s; o < t; o ++) {
				busy[o] = 0;
			}
		}
		rep(i, Aj) {
			scanf("%d%d", &s, &t);
			for (int o = s; o < t; o ++) {
				busy[o] = 1;
			}
		}
		if (busy[0] != 0) {
			dp[0][1][0][0] = 0;
		}
		if (busy[0] != 1) {
			dp[0][0][1][1] = 0;
		}

		for (int i = 1; i < 1440; i ++) {
			for (int j = max(0, i-720); j <= min(i+1, 720); j ++) {
				rep(fir, 2) {
					int &res = dp[i][j][0][fir];
					// c to do (1,2)
					if (j && busy[i] != 0) {
						// last is c
						checkmin(res, dp[i-1][j-1][0][fir]);
						// last is j
						checkmin(res, dp[i-1][j-1][1][fir] + 1);
					}


					if (busy[i] != 1) {
						int &res2 = dp[i][j][1][fir];
						// j to do
						// last is j
						checkmin(res2, dp[i-1][j][1][fir]);
						// last is c
						checkmin(res2, dp[i-1][j][0][fir] + 1);
					}
				}
			}
		}
		int answer = -1e9;
		rep(now, 2) {
			rep(fir, 2) {
				if (now != fir) {
					dp[1439][720][now][fir] ++;
				}
				checkmin(answer, dp[1439][720][now][fir]);
			}
		}
		printf("Case #%d: %d\n", cas + 1, answer);
	}
	return 0;
}
