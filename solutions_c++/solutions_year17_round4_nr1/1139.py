#include <bits/stdc++.h>
using namespace std;

int T, N, P, Gi;
vector <int> R;

int dp[105 * 105 * 105][4];
int solve(vector <int> S, int m){
	int h = 0;
	for(int i = 1; i < P; i++)
		h = h * 102 + S[i];

	if(dp[h][m] != -1)return dp[h][m];

	bool empty = true;
	for(int i = 1; i < P; i++)
		if(S[i] > 0)empty = false;
	if(empty){
		return dp[h][m] = 0;
	}

	int r = 0;
	for(int i = 1; i < P; i++)if(S[i] > 0){
		S[i]--;
		r = max(r, solve(S, (m + i) % P));
		S[i]++;
	}
	return dp[h][m] = r + (m == 0);
}
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d %d", &N, &P);

		R.clear();
		R.resize(P);

		for(int i = 0; i < N; i++){
			scanf("%d", &Gi);
			R[Gi % P]++;
		}

		memset(dp, -1, sizeof dp);
		printf("Case #%d: %d\n", t, R[0] + solve(R, 0));
	}
	return 0;
}
