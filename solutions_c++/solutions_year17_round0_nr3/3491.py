#include<stdio.h>
#define MAX 99999999999999999 
#define Min(a,b) (a < b ? a : b)
long long Rmin, Lmin;
void solve(long long lo, long long ro, long long num) {
	long long mid = (lo + ro) >> 1;
	if (num == 0) {
		Rmin = Min(ro - mid - 1,Rmin);
		Lmin = Min(mid - lo - 1, Lmin);
		return ;
	}
	long long l, r;
	l = num / 2;
	r = l + (num % 2);
	if (r)
		solve(mid, ro, r - 1);
	if (l) 
		solve(lo, mid, l - 1);
	return;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test = 1, t;
	scanf("%d", &t);
	while (test <= t) {
		long long N, K;
		Rmin = Lmin = MAX;
		scanf("%lld %lld", &N, &K);
		solve(0, N + 1, K-1);
		printf("Case #%d: %lld %lld\n", test++, Rmin, Lmin);
	}
}