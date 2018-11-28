#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int,int> pii;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

const double EPS = 1e-10;
int t;
int n, q;
const int N = 105;
pii city[N];
int ar[N][N];
double dp[N];
int main(){
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc){
		scanf("%d %d", &n, &q);
		for(int i = 1;i <= n; ++i) scanf("%d%d", &city[i].fi, &city[i].se);

		for(int i = 1; i <= n; ++i){
			for(int j = 1;j <= n; ++j){
				scanf("%d", &ar[i][j]);
			}
		}

		printf("Case #%d:", tc);
		for(int ii = 0;ii < q; ++ii){
			int u, v;
			scanf("%d%d", &u, &v);
			for(int i = 0;i <= n; ++i) dp[i] = 1000000000000000.0;
			dp[1] = 0;
			for(int i = 1;i <= n; ++i){
				int dists = 0;
				for(int j = i + 1;j <= n; ++j){
					dists += ar[j-1][j];
					if(city[i].fi - dists < 0) break;
					dp[j] = min(dp[j], dp[i] + ((double)dists / (double)city[i].se));
					//printf("%d %d %d: %lf\n", i, j, dists, dp[j]);
				}
			}
			printf(" %lf", dp[n]);
		}
		printf("\n");
	}
	return 0;
}