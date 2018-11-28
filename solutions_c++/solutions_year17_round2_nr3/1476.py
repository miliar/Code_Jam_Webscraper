#include<bits/stdc++.h>
#define MAXN 110
using namespace std;
int m[MAXN][MAXN];
int E[MAXN], S[MAXN];
double dp[MAXN];
int N, Q;
double solve(){
	dp[N] = 0.;
	for(int i = N-1; i > 0; i--){
		dp[i] = (double)(1LL << 50);
		int dist = 0;
		for(int j = i+1; j <= N; j++){
			dist += (m[j-1][j]);
			if(dist > E[i])
				break;
			
			dp[i] = min(dp[i], dp[j] + (double)dist/(double)S[i]);
		}
	}
	return dp[1];
}
int main(){
	int T;
	cin >> T;
	for(int l = 1; l <= T; l++){
		cout << "Case #" << l << ": ";
		cin >> N >> Q;
		for(int i = 1; i <= N; i++)
			cin >> E[i] >> S[i];
		
		for(int i = 1; i <= N; i++)
			for(int j = 1; j <= N; j++){
				cin >> m[i][j];
			}

		while(Q--){
			int ui, vi;
			cin >> ui >> vi;
			cout << fixed << setprecision(8) << solve() << "\n";
		}
	}
}