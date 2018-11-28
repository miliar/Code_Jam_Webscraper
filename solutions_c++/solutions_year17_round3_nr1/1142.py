#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;
typedef long long int Long;
typedef struct { Long r, h; } P;
int pcmp(const void *a, const void *b) {
	P *x = (P *)a, *y = (P *)b;
	if(x->r == y->r) return y->h < x->h ? -1 : 1;
	return y->r < x->r ? -1 : 1;
}
Long max(Long a, Long b) { return a > b ? a : b; }

int n, k, t;
P p[1001];
Long dp[1005][1005];

Long use(int i, int cnt) {
	if(cnt == k) { return 0; }
	if(n == i) { return -1; }
	if(dp[i][cnt] != -1) { return dp[i][cnt]; }
	
	dp[i][cnt] = use(i+1, cnt+1);
	if(dp[i][cnt] != -1) {
		dp[i][cnt] += p[i].r*(p[i].h<<1);
		if(!cnt) dp[i][cnt] += p[i].r*p[i].r;
	}
	dp[i][cnt] = max( dp[i][cnt], use(i+1, cnt) );
	dp[i][cnt] = max( dp[i][cnt], 0);
	return (dp[i][cnt]);
}

int main() {
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		scanf("%d%d", &n, &k);
		for(int i = 0; i < n; ++i) { scanf("%lld%lld", &p[i].r, &p[i].h); }
		qsort(p, n, sizeof(P), pcmp);
		
		for(int i = 0; i <= n; ++i)
			for(int j = 0; j <= k; ++j)
				dp[i][j] = -1;
		
		Long ans = use(0, 0);
		for(int i = 1; i < n; ++i) {
			ans = max(ans, dp[i][0]);
			// fprintf(stderr, "%lld %lld %lld\n", p[i].r, p[i].h, dp[i][0]);
		} // fprintf(stderr, "\n");
		
		printf("Case #%d: %.9f\n", tc, M_PI * ans);
	}
	return 0;
}
