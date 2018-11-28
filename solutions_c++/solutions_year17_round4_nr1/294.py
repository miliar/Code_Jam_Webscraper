#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

int dp[5][101][101][101];
int get(int p, int i, int j, int k){ // 1,2,3
	if(i < 0 || j < 0 || k < 0) return -100;
	if(i > 100 || j > 100 || k > 100) return -100;
	return dp[p][i][j][k];
}
main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	FILE *fout = freopen("A-large.out", "w", stdout);
	assert( fin!=NULL );
	for(int i = 0; i <= 100; i++){
		for(int j = 0; j <= 100; j++){
			for(int k = 0; k <= 100; k++){
				for(int p = 2; p <= 4; p++){
					dp[p][i][j][k] = 0;
					if(p == 2){
						dp[p][i][j][k] = max(dp[p][i][j][k], 1+get(p,i-2,j,k));
					}
					if(p == 3){
						dp[p][i][j][k] = max(dp[p][i][j][k], 1+get(p,i-3,j,k));
						dp[p][i][j][k] = max(dp[p][i][j][k], 1+get(p,i,j-3,k));
						dp[p][i][j][k] = max(dp[p][i][j][k], 1+get(p,i-1,j-1,k));
					}
					if(p == 4){
						dp[p][i][j][k] = max(dp[p][i][j][k], 1+get(p,i-4,j,k));
						dp[p][i][j][k] = max(dp[p][i][j][k], 1+get(p,i,j-2,k));
						dp[p][i][j][k] = max(dp[p][i][j][k], 1+get(p,i,j,k-4));
						dp[p][i][j][k] = max(dp[p][i][j][k], 1+get(p,i-2,j-1,k));
						dp[p][i][j][k] = max(dp[p][i][j][k], 1+get(p,i,j-1,k-2));
						dp[p][i][j][k] = max(dp[p][i][j][k], 1+get(p,i-1,j,k-1));
					}
				}
			}
		}
	}

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int n, p;
		cin >> n >> p;
		int g[n];
		int freq[5];
		for(int i = 0; i < 5; i++){
			freq[i] = 0;
		}
		int sum = 0;
		for(int i = 0; i < n; i++){
			cin >> g[i];
			freq[g[i] % p]++;
			sum = (sum + g[i]) % p;
		}
		int ans = freq[0] + dp[p][freq[1]][freq[2]][freq[3]];

		if(sum % p != 0) ans++;
		cout << ans << endl;
	}
	exit(0);
}