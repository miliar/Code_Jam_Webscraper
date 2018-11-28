#include <bits/stdc++.h>

using namespace std;

#define FOE(i, s, t) for (int i = s; i <= t; i++)
#define FOD(i, s, t) for (int i = s; i >= t; i--)
#define FOR(i, s, t) for (int i = s; i < t; i++)
#define mp make_pair
#define pb push_back
#define LL long long

int t;

#define K 61

int n, k;
double p[K], p2[K];
double chance;
double ans;

double dp[K][K];

void calc(){
	memset(dp, 0.00, sizeof(dp));
	dp[1][0] = 1.00;
	FOE(i, 1, n) FOE(j, 0, n){
		dp[i + 1][j] += dp[i][j] * (1.00 - p2[i]);
		dp[i + 1][j + 1] += dp[i][j] * p2[i];
	}

	double sol = 0.00;
	FOE(i, k, n) sol += dp[n + 1][i];
	if (ans < sol) ans = sol;
}

void solve(){
	scanf("%d%d", &n, &k);
	scanf("%lf", &chance);
	FOE(i, 1, n) scanf("%lf", &p[i]);
	ans = 0.00;
	
	sort(p + 1, p + n + 1);

	FOE(i, 1, n){
		FOE(j, 1, n) p2[j] = p[j];
		int ptr = i;
		int tot = 1;
		double cc = chance;
		while (true){
			if (ptr == n){
				double left = cc / tot;
//				printf("i = %d, left = %.9f\n", i, left);
				FOE(j, i, ptr) p2[j] += left;
				break;
			}

			double tar = p2[ptr + 1];
			double req = (tar - p2[ptr]) * tot;
//			printf("req = %.9f for ptr = %d, i = %d\n", req, ptr, i);
			if (req > cc){
				double can = cc / tot;
				FOE(j, i, ptr) p2[j] += can;
				break;
			} else {	
				cc -= (tar - p2[ptr]) * tot;
				FOE(j, i, ptr) p2[j] = tar;
				ptr++;
				tot++;
			}
		}
		FOE(j, 1, n) if (p2[j] > 1.00) p2[j] = 1.00;
//		FOE(j, 1, n) printf("%.9f\n", p2[j]);
//		FOE(j, 1, n) printf("%.9f\n", p[j]);
//		puts("");
		calc();
//		printf("i = %d, sol = %.9f\n", i, ans);
	}

	printf("%.9f\n", ans);
}

int main(){
	scanf("%d", &t);
	FOE(i, 1, t){
		printf("Case #%d: ", i);
		solve();
	}
}
