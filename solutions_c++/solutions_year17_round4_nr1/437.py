#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld double
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define pii pair<int,int>
#define vll vector<ll >
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1)
#define all(a) (a).begin(), (a).end()
#define print(s) cerr<<#s<<" : ";for(auto i:(s))cerr<<i<<" ";cerr<<"\n";
#define sd(t) scanf("%d",&(t))
#define pd(t) printf("%d\n",(t))
#define endl "\n"
const int inf = 1e9 + 10;
int cnt[4];
const int N = 101;
int dp[4][N][N][N][N];
int main(){
	int t = 1;
	sd(t);
	for(int tt = 1; tt <= t; tt++){
		int n, p;		
		sd(n); sd(p);
		memset(cnt, 0, sizeof cnt);
		for(int i = 0; i < n; i++){
			int x;
			sd(x);
			cnt[x % p]++;
		}
		memset(dp, 0, sizeof dp);

		for(int j = 0; j <= cnt[0]; j++){
			for(int k = 0; k <= cnt[1]; k++){
				for(int l = 0; l <= cnt[2]; l++){
					for(int l1 = 0; l1 <= cnt[3]; l1++){
						for(int i = 0; i < 4; i++){
							if(j > 0)
								dp[i][j][k][l][l1] = max(dp[i][j][k][l][l1], (i == 0) + dp[i][j - 1][k][l][l1]);
							if(k > 0)
								dp[i][j][k][l][l1] = max(dp[i][j][k][l][l1], (i == 0) + dp[(i+1)%p][j][k - 1][l][l1]);
							if(l > 0)
								dp[i][j][k][l][l1] = max(dp[i][j][k][l][l1], (i == 0) + dp[(i+2)%p][j][k][l - 1][l1]);
							if(l1 > 0)
								dp[i][j][k][l][l1] = max(dp[i][j][k][l][l1], (i == 0) + dp[(i+3)%p][j][k][l][l1 - 1]);
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",tt, dp[0][cnt[0]][cnt[1]][cnt[2]][cnt[3]]);
	}
}