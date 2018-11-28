#include <bits/stdc++.h>

#define ll long long
using namespace std;

const int MAXN = 2005;
const int MOD = 1000000007;

int dp[2][MAXN][MAXN][2],A[MAXN],B[MAXN];

int main(){
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		cout << "Case #" << tc << ": ";
		int n,m; cin >> n >> m;
		for(int i=0;i<n;i++){
			int a,b; cin >> a >> b;
			for(int j=a;j<b;j++) A[j] = 1;
		}
		for(int i=0;i<m;i++){
			int a,b; cin >> a >> b;
			for(int j=a;j<b;j++) B[j] = 1;
		}
		for(int k=0;k<2;k++)
			for(int i=0;i<MAXN;i++)
				for(int j=0;j<MAXN;j++)
					dp[k][i][j][0] = dp[k][i][j][1] = MAXN;
		if(!A[0]) dp[0][0][1][0] = 0;
		if(!B[0]) dp[1][0][0][1] = 0;
		int day = 24*60;
		for(int k=0;k<2;k++){
			if(k == 0 && A[0]) continue;
			if(k == 1 && B[0]) continue;
			for(int i=1;i<day;i++){
				if(!B[i])
					dp[k][i][0][1] = dp[k][i-1][0][1];
				for(int j=1; j <= min(day/2,i+1) ;j++){
					if(!A[i]){
						dp[k][i][j][0] = min(dp[k][i-1][j-1][0],dp[k][i-1][j-1][1]+1);
					}
					if(!B[i]){
						dp[k][i][j][1] = min(dp[k][i-1][j][1],dp[k][i-1][j][0]+1);
					}
					//if(dp[k][i][j][0] != MAXN) cout << i << ' ' << j << ' ' << "0 " << dp[k][i][j][0] << '\n';
					//if(dp[k][i][j][1] != MAXN) cout << i << ' ' << j << ' ' << "1 " << dp[k][i][j][1] << '\n';
				}
			}
		}
		int ans = MAXN;
		for(int i=0;i<2;i++){
			for(int j=0;j<2;j++){
				ans = min(ans , dp[i][day-1][day/2][j] + (i != j));
			}
		}
		cout << ans << '\n';
		// clear
		memset(A,0,sizeof A);
		memset(B,0,sizeof B);
	}
	return 0;
}

