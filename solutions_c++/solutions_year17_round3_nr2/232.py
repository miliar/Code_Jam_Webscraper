#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); ++i)

int dp[1441][722][2][2], in[1441], out[1441];

void up(int &x, int y) { x = min(x, y); }

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		printf("Case #%d: ", tc);
		int n[2];
		scanf("%d%d", n, n + 1);
		f(i, 0, 1441)in[i] = 0;
		f(i, 0, 1441)out[i] = 0;
		f(i, 0, n[0]){
			int a, b;
			scanf("%d%d", &a, &b);
			in[a] = 1;
			out[b] = 1;
		}
		f(i, 0, n[1]){
			int a, b;
			scanf("%d%d", &a, &b);
			in[a] = 2;
			out[b] = 2;
		}
		f(i, 0, 1441)f(j, 0, 721)f(k, 0, 2)f(w, 0, 2)dp[i][j][k][w] = 1e9;
		dp[0][0][0][0] = dp[0][0][1][1] = 0;
		int g = 2;
		f(i, 0, 1440)f(j, 0, 721)f(k, 0, 2)f(w, 0, 2){
			int &r = dp[i][j][k][w];
			if (out[i])g = 2;
			if (in[i] == 1)g = 0;
			else if (in[i] == 2)g = 1;
			if (g == 2){
				up(dp[i + 1][j + (w == 0)][k][w], r);
				up(dp[i + 1][j + (w == 0)][k][!w], r + 1);
			}
			else if (w ^ g){
				up(dp[i + 1][j + (w == 0)][k][w], r);
				if (out[i + 1])up(dp[i + 1][j + (w == 0)][k][!w], r + 1);
			}
		}
		int an = 1e9;
		f(i, 0, 2)f(j, 0, 2)up(an, dp[1440][720][i][j] + (i ^ j));
		printf("%d\n", an);
	}
}