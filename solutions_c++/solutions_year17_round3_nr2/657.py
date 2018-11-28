#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int N = 2100;

int dp[N][N][2];

typedef struct seg{
	int x,y;
}seg;

int a[N],b[N];

const int inf = ~0U>>2;

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
	int T; cin >> T;
	int nc = 0;
	while(T--){
		int n,m;
		cin >> n >> m;
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for (int i = 1;i <= n;i++){
			int x,y;
			cin >> x >> y;
			if (x > y) swap(x,y);
			for (int j = x;j < y;j++)
				a[j]++;
		}
		for (int i = 1;i <= m;i++){
			int x,y;
			cin >> x >> y;
			if (x > y) swap(x,y);
			for (int j = x;j < y;j++)
				b[j]++;
		}
		memset(dp,0,sizeof(dp));
		int ans = inf;
		for (int i = 0;i <= 1440;i++)
			for (int j = 0;j <= 1440;j++){
				dp[i][j][0] = dp[i][j][1] = inf;
			}
		dp[0][0][0] = dp[0][0][1] = 0;
		dp[0][0][0] = 1;
		for (int i = 1;i <= 1440;i++)
			for (int j = 1;j <= min(i,720);j++){
				if (!a[i]){
					dp[i][j][0] = min(dp[i-1][j-1][0],dp[i][j][0]);
					dp[i][j][0] = min(dp[i-1][i-j][1] + 1,dp[i][j][0]);
				}
				if (!b[i]){
					dp[i][j][1] = min(dp[i-1][j-1][1],dp[i][j][1]);
					dp[i][j][1] = min(dp[i-1][i-j][0] + 1,dp[i][j][1]);
				}
				if (i == 1440) ans = min(ans,dp[i][j][1]);
		}
		memset(dp,0,sizeof(dp));
		for (int i = 0;i <= 1440;i++)
			for (int j = 0;j <= 1440;j++){
				dp[i][j][0] = dp[i][j][1] = inf;
			}
		dp[0][0][0] = dp[0][0][1] = 0;
		dp[0][0][1] = 1;
		for (int i = 1;i <= 1440;i++)
			for (int j = 1;j <= min(i,720);j++){
				if (!a[i]){
					dp[i][j][0] = min(dp[i-1][j-1][0],dp[i][j][0]);
					dp[i][j][0] = min(dp[i-1][i-j][1] + 1,dp[i][j][0]);
				}
				if (!b[i]){
					dp[i][j][1] = min(dp[i-1][j-1][1],dp[i][j][1]);
					dp[i][j][1] = min(dp[i-1][i-j][0] + 1,dp[i][j][1]);
				}
				if (i == 1440) ans = min(ans,dp[i][j][0]);
		}
		printf("Case #%d: ",++nc);
		cout << ans << endl;
	}
}
