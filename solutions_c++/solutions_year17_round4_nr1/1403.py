#include <bits/stdc++.h>

#define ll long long
using namespace std;

const int MAXN = 105;
const int MOD = 1000000007;

int n,p,A[4],dp[MAXN][MAXN][MAXN][MAXN][4];

int fun(int a,int b,int c,int d,int e){
	if(a == 0 && b == 0 && c == 0 && d == 0) return 0;
	if(dp[a][b][c][d][e] != -1) return dp[a][b][c][d][e];
	int& ans = dp[a][b][c][d][e];
	if(a > 0){
		ans = max(ans,fun(a-1,b,c,d,e)+(e == 0));
	}
	if(b > 0){
		ans = max(ans,fun(a,b-1,c,d,(p-(-e+1+p)%p)%p) + (e == 0));
	}
	if(c > 0){
		ans = max(ans,fun(a,b,c-1,d,(p-(-e+2+p)%p)%p) + (e == 0));
	}
	if(d > 0){
		ans = max(ans,fun(a,b,c,d-1,(p-(-e+3+p)%p)%p) + (e == 0));
	}
	return ans;
}

int main(){
	ios_base::sync_with_stdio(false);
	memset(dp,-1,sizeof dp);
	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		cout << "Case #" << tc << ": ";
		cin >> n >> p;
		memset(A,0,sizeof A);
		for(int i=0;i<n;i++){
			int a; cin >> a;
			A[a%p]++;
		}
		int ans = fun(A[0],A[1],A[2],A[3],0);
		cout << ans << '\n';
		//clear
		for(int i=0;i<=n;i++){
			for(int j=0;j<=n;j++){
				if(p != 2) for(int k=0;k<=n;k++){
					if(p != 3) for(int l=0;l<=n;l++){
						for(int m=0;m<4;m++) dp[i][j][k][l][m] = -1;
					}
					else for(int m=0;m<3;m++) dp[i][j][k][0][m] = -1;
				}
				else for(int m=0;m<2;m++) dp[i][j][0][0][m] = -1;
			}
		}

	}
	return 0;
}

