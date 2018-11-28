#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); ++i)

int n, q, w[100][100];
pair<int, int> h[100];

double dp[100];

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		printf("Case #%d:", tc);
		scanf("%d%d", &n, &q);
		f(i, 0, n)scanf("%d%d", &h[i].first, &h[i].second);
		f(i, 0, n)f(j, 0, n)scanf("%d", w[i] + j);
		while (q--){
			int a, b;
			scanf("%d%d", &a, &b);
			f(i, 1, n){
				dp[i] = 1e18;
				ll dis = 0;
				for (int j = i - 1; j >= 0; --j){
					dis += w[j][j + 1];
					if (h[j].first >= dis)dp[i] = min(dp[i], dp[j] + (double)dis / h[j].second);
				}
			}
			printf(" %.7lf", dp[n - 1]);
		}
		printf("\n");
	}
}