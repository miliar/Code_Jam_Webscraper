//============================================================================
// Name        : A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <iostream>
#include <set>
#include <queue>
#define MAXN 100050
#define eps 1e-8
#define max(x,y) ((x)>(y)?(x):(y))
#define min(x,y) ((x)<(y)?(x):(y))
#define LL long long
using namespace std;
double f[111][111];
LL dis[111][111];
int e[111], s[111];
int mp[111][111];
double dp[111][111];
bool bo[111][111];
struct node {
	int x, y;
	node(){
	}
	node(int xx, int yy) {
		x = xx, y = yy;
	}
} st[2111111];
int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int tt, ri = 0;
	scanf("%d", &tt);
	while (tt--) {
		int n, q;
		scanf("%d%d", &n, &q);
		for (int i = 1; i <= n; ++i)
			scanf("%d%d", &e[i], &s[i]);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j) {
				scanf("%d", &mp[i][j]);
				dis[i][j] = mp[i][j];
			}
		for (int k = 1; k <= n; ++k) {
			for (int i = 1; i <= n; ++i) {
				for (int j = 1; j <= n; ++j) {
					if (dis[i][k] < 0 || dis[k][j] < 0)
						continue;
					if (dis[i][j] < 0 || dis[i][k] + dis[k][j] < dis[i][j])
						dis[i][j] = dis[i][k] + dis[k][j];
				}
			}
		}
		for(int i=1;i<=n;++i)
			dis[i][i]=0;
//		for(int i=1;i<=n;++i){
//			for(int j=1;j<=n;++j){
//				printf("%I64d ",dis[i][j]);
//			}
//			puts("");
//		}
		printf("Case #%d:",++ri);
		for (int cas = 0; cas < q; ++cas) {
			memset(bo, 0, sizeof(bo));

			for(int i=1;i<=n;++i){
				for(int j=1;j<=n;++j)
					dp[i][j]=-1.0;
			}
			int star, ed;
			scanf("%d%d", &star, &ed);
			bo[star][star] = true;
			dp[star][star] = 0;
			int tail = 0;
			st[tail++] = node(star, star);
			double ans = -1;
			for (int i = 0; i < tail; ++i) {
				int x = st[i].x;
				int y = st[i].y;
				bo[x][y] = false;
				if (ans > eps && dp[x][y] > ans - eps)
					continue;
				if (x == ed) {
					if (ans < -eps || dp[x][y] < ans)
						ans = dp[x][y];
					continue;
				}
//				printf(":::::::::%d %d %lf\n",x,y,dp[x][y]);
				for (int j = 1; j <= n; ++j) {
					if (dis[x][j] < -eps)
						continue;
//					printf("1:%d\n",j);
					if (dis[y][x] + dis[x][j] > e[y])
						continue;
//					printf("2:%d \n",j);
					if (dp[j][y]<-eps||dp[j][y] > dp[x][y] + dis[x][j] * 1.0 / s[y]) {
//						printf("sy:%d %d\n",y,s[y]);
						dp[j][y] = dp[x][y] + dis[x][j] * 1.0 / s[y];
						if (bo[j][y] == false) {
							st[tail++] = node(j, y);
							bo[j][y]=true;
//							puts("ssssssssss");
						}
					}
					if (dp[j][j]<-eps||dp[j][j] > dp[x][y] + dis[x][j] * 1.0 / s[y]) {
//						printf("st:%d %d\n",y,s[y]);
						dp[j][j] = dp[x][y] + dis[x][j] * 1.0 / s[y];
						if (bo[j][j] == false) {
							st[tail++] = node(j, j);
							bo[j][j]=true;
						}
					}
				}
			}
			printf(" %.8lf",ans);
		}
		puts("");
	}
	return 0;
}
