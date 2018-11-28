#include <bits/stdc++.h>

using namespace std;

#define N 18

long long dp[N + 1][10][2];
long long pot[N + 1];
long long s[N + 1];
char str[N + 2];
int n;

long long solve(int x, int last, bool bigger){
	long long ret;

	if (x == n){
		return 0;
	}

	if (dp[x][last][bigger] != -1){
		return dp[x][last][bigger];
	}

	dp[x][last][bigger] = -2;

	if (bigger){
		ret = solve(x + 1, 9, true);

		if (ret != -2){
			dp[x][last][bigger] = 9ll * pot[n - x - 1] + ret;
		}
	}
	else{
		if (last <= s[x]){
			ret = solve(x + 1, s[x], false);

			if (ret != -2){
				dp[x][last][bigger] = s[x] * pot[n - x - 1] + ret;
			}
		}

		if (last <= s[x] - 1){
			ret = solve(x + 1, s[x] - 1, true);

			if (ret != -2){
				dp[x][last][bigger] = max(dp[x][last][bigger], (s[x] - 1ll) * pot[n - x - 1] + ret);
			}
		}
	}

	return dp[x][last][bigger];
}

int main(){
	int t, i, j;

	pot[0] = 1;

	for (i = 1; i <= N; i++){
		pot[i] = pot[i - 1] * 10ll;
	}

	scanf("%d%*c", &t);
	
	for (i = 1; i <= t; i++){
		scanf("%[^\n]%n%*c", str, &n);

		for (j = 0; j < n; j++){
			s[j] = str[j] - '0';
		}

		memset(dp, -1, sizeof(dp));

		printf("Case #%d: %lld\n", i, solve(0, 0, false));
	}

	return 0;
}