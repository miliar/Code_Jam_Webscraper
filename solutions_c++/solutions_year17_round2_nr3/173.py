#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <queue>
#include <map>
#define maxn 109
#define maxm 100000
using namespace std;
const long long INF = 1e18;
int  n, Q;
int E[maxn], D[maxn];
long long a[maxn][maxn];
double d[maxn][maxn];
int main(){
	int cot = 1;
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round1B/A.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round1B/A.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	while(tt--){
		cin >> n >> Q;
		for(int i = 1; i <= n; i++)
			cin >> D[i] >> E[i];
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= n; j++){
				cin >> a[i][j];
				if(i == j)
				 	a[i][j] = 0;
				if(a[i][j] == -1)
					a[i][j] = INF;
			}
		}
		
		for(int k = 1; k <= n; k++)
			for(int i = 1; i <= n; i++)
				for(int j = 1; j <= n; j++)
					a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
					
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++)
				if(i == j)
					d[i][j] = 0;
				else
					d[i][j] = INF;
		
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= n; j++){
				if(i == j)
					continue;
				if(a[i][j] <= D[i]){
					d[i][j] = 1.0 * a[i][j] / E[i];
				}
			}
		}
		
		for(int k = 1; k <= n; k++)
			for(int i = 1; i <= n; i++)
				for(int j = 1; j <= n; j++)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
		
		printf("Case #%d:", cot++);
		for(int i = 1; i <= Q; i++){
			int u, v;
			scanf("%d%d", &u, &v);
			printf(" %.8f", d[u][v]);
		}
		puts("");
	}
	return 0;
}
