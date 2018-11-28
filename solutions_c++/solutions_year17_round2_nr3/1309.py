#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

double memo[110];
long long vis[110];

long long d[110][110];

long long e[110];
long long s[110];

long long n;

double dp(long long a, long long x) {
	if (a == n - 1)
		return 0.0;
	if (vis[a] == x)
		return memo[a];
	
	double mini = 2e18;
	
	for (long long i = a + 1; i < n; i++) {
		if (d[a][i] != -1 && d[a][i] <= e[a])
			mini = min(mini, dp(i, x) + ((double)d[a][i])/s[a]);
	}
	vis[a] = x;
	return memo[a] = mini;
}

int main () {
	
	long long t;
	
	scanf("%lld", &t);
	
	for (long long i = 0; i < t; i++) {
		
		long long q;
		
		scanf("%lld %lld", &n, &q);
		
		for (long long j = 0; j < n; j++) {
			scanf("%lld %lld", &e[j], &s[j]);
		}
		for (long long j = 0; j < n; j++) {
			for (long long k = 0; k < n; k++) {
				scanf("%lld", &d[j][k]);
			}
		}
		
		printf("Case #%lld: ", i + 1);
		
		for (long long j = n - 2; j > 0; j--) {
			//n-2, n-1
			for (long long k = n - 1; k > j; k--) {
				d[j-1][k] = d[j-1][k] == -1 ? d[j][k] + d[j-1][j] :  min(d[j-1][k], d[j][k] + d[j-1][j]);
			}
		}
		
		for (long long j = 0; j < q; j++) {
			long long u, v;
			scanf("%lld %lld", &u, &v);
// 			printf("%lld %lld\n", u, v);
			u--;
			v--;
			
			printf("%.08lf\n", dp(u, i + 1));
		}
	}
	
	return 0;
	
}
