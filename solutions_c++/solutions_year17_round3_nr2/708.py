#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)|1)
#define mi ((l+r)>>1)
#define fk puts("fuck!")
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

pair<pair<int,int>,int> a[233];
int dp[1443][723][2];
const int INF = 12345;

void up(int &x, int y) {
	x = min(x, y);
}

void db(int x, int y, int z) {
	printf("dp[%d][%d][%d] = %d\n", x, y, z, dp[x][y][z]);
}

int main()
{
	int T; scanf("%d", &T);
	for(int cas=1; cas<=T; ++cas) {
		int AC, AJ; scanf("%d%d", &AC, &AJ);
		for(int i=1; i<=AC; ++i) {
			scanf("%d%d", &a[i].X.X, &a[i].X.Y);
			a[i].Y = 0;
		}
		for(int i=1; i<=AJ; ++i) {
			scanf("%d%d", &a[AC+i].X.X, &a[AC+i].X.Y);
			a[AC+i].Y = 1;
		}
		int sum = AC + AJ;
		sort(a+1, a+sum+1);
		int ans = INF;
		// 0 first
		if(a[1].X.X > 0 || a[1].Y == 0) {
			memset(dp, 123, sizeof dp);
			dp[0][0][0] = 1;
			int An = 1, i = 0;
			while(i <= 1440) {
				if(An <= sum && a[An].X.X == i) {
					int now = a[An].Y;
					int til = a[An].X.Y;
					int add = a[An].X.Y - a[An].X.X;
					for(int j=0; j<=i && j<=720; ++j) {
						if(dp[i][j][0]<INF) {
							if(now == 0 && j+add <= 720)
								up(dp[til][j+add][0], dp[i][j][0]);
							if(now == 1)
								up(dp[til][j][1], dp[i][j][0]+1);
						}
						if(dp[i][j][1]<INF) {
							if(now == 0 && j+add <= 720)
								up(dp[til][j+add][0], dp[i][j][1]+1);
							if(now == 1)
								up(dp[til][j][1], dp[i][j][1]);
						}
					}
					i = a[An++].X.Y;
				} else {
					for(int j=0; j<=i && j<=720; ++j) {
						if(dp[i][j][0]<INF) {
							if(j+1 <= 720)
								up(dp[i+1][j+1][0], dp[i][j][0]);
							up(dp[i+1][j][1], dp[i][j][0]+1);
						}
						if(dp[i][j][1]<INF) {
							up(dp[i+1][j][1], dp[i][j][1]);
							if(j+1 <= 720)
								up(dp[i+1][j+1][0], dp[i][j][1]+1);
						}
					}
					++i;
				}
			}
			up(ans, dp[1440][720][0]-1);
			up(ans, dp[1440][720][1]);
		}
		// 1 first
		if(a[1].X.X > 0 || a[1].Y == 1) {
			memset(dp, 123, sizeof dp);
			dp[0][0][1] = 1;
			int An = 1, i = 0;
			while(i <= 1440) {
				if(An <= sum && a[An].X.X == i) {
					int now = a[An].Y;
					int til = a[An].X.Y;
					int add = a[An].X.Y - a[An].X.X;
					for(int j=0; j<=i && j<=720; ++j) {
						if(dp[i][j][0]<INF) {
							if(now == 0 && j+add <= 720)
								up(dp[til][j+add][0], dp[i][j][0]);
							if(now == 1)
								up(dp[til][j][1], dp[i][j][0]+1);
						}
						if(dp[i][j][1]<INF) {
							if(now == 0 && j+add <= 720)
								up(dp[til][j+add][0], dp[i][j][1]+1);
							if(now == 1)
								up(dp[til][j][1], dp[i][j][1]);
						}
					}
					i = a[An++].X.Y;
				} else {
					for(int j=0; j<=i && j<=720; ++j) {
						if(dp[i][j][0]<INF) {
							if(j+1 <= 720)
								up(dp[i+1][j+1][0], dp[i][j][0]);
							up(dp[i+1][j][1], dp[i][j][0]+1);
						}
						if(dp[i][j][1]<INF) {
							up(dp[i+1][j][1], dp[i][j][1]);
							if(j+1 <= 720)
								up(dp[i+1][j+1][0], dp[i][j][1]+1);
						}
					}
					++i;
				}
			}
			up(ans, dp[1440][720][0]);
			up(ans, dp[1440][720][1]-1);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}





