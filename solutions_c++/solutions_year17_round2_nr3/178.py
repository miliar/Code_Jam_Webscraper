#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#define LL long long
#define eps 1e-8
#define mem(a,b) memset(a,b,sizeof(a))
#define zero(x) ((x > +eps) - (x < -eps))
#define MAX 100010
#define INF 100000000
#define MAXEDGE 50010
#define MAX 2100
using namespace std;
//freopen("", "r", stdin);
//freopen("", "w", stdout);
//printf("Case #%d: ", ii);

struct NODE{
	LL d, s;
}nodes[110];

int n, q;
LL mp[110][110];
LL dis[110][110];
int f[110][110];
double dp[110][110];

int main(){
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	int T;
	int a, b;
	scanf("%d", &T);
	for (int ii = 1; ii <= T; ii++){
		scanf("%d%d", &n, &q);
		for (int i = 1; i <= n; i++){
			scanf("%lld%lld", &nodes[i].d, &nodes[i].s);
		}
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= n; j++){
				scanf("%lld", &mp[i][j]);
				if (mp[i][j] == -1){
					mp[i][j] = 100000000000000LL;
				}
			}
			mp[i][i] = 0;
		}
		for (int k = 1; k <= n; k++){
			for (int i = 1; i <= n; i++){
				for (int j = 1; j <= n; j++){
					mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j]);
				}
			}
		}
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= n; j++){
				if (mp[i][j] <= nodes[i].d){
					dp[i][j] = mp[i][j] * 1.0 / nodes[i].s;
				}
				else{
					dp[i][j] = 1000000000000000.0;
				}
			}
		}
		for (int k = 1; k <= n; k++){
			for (int i = 1; i <= n; i++){
				for (int j = 1; j <= n; j++){
					dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
				}
			}
		}
		printf("Case #%d:", ii);
		while(q--){
			scanf("%d%d", &a, &b);
			printf(" %.10lf",dp[a][b]);
		}
		printf("\n");
	}
	return 0;
}