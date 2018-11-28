#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<LL, double> PII;
typedef set<int>::iterator SIT; 

const int maxn = 105;

int n, q, E[maxn], S[maxn], u, v;
int mat[maxn][maxn];
double dp[maxn];

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cases;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d", &n, &q);
		for(int i = 1; i <= n; ++i){
			scanf("%d%d", &E[i], &S[i]);
		}
		for(int i = 1; i <= n; ++i){
			for(int j = 1; j <= n; ++j){
				scanf("%d", &mat[i][j]);
			}
		}
		printf("Case #%d:", ++cases);
		while(q--){
			scanf("%d%d", &u, &v);
			dp[n] = 0;
			for(int i = n - 1; i > 0; --i){
				int tot = 0;
				dp[i] = 1e50;
				for(int j = i + 1; j <= n; ++j){
					tot += mat[j - 1][j];
					//printf("tot = %d\n", tot);
					if(tot > E[i]) break;
					if(dp[j] > 1e40) continue;
					dp[i] = min(dp[i], 1.0 * tot / S[i] + dp[j]);
					//printf("j = %d, tot = %d, dp[i] = %lf\n", j, tot, dp[i]);
				}
			}
			printf(" %.10lf", dp[1]);
		}
		puts("");
	}
	return 0;
}
