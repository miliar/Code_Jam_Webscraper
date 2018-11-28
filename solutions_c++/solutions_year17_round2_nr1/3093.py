#include <stdio.h>
#define MAXN 1004
#define MAXX 10004
#define ll long long
int t,n,dest;
double low, mid, hi,p;
int pos[MAXN], speed[MAXN];
int main() {
	freopen("c:\\A-large.in", "r", stdin);
	freopen("c:\\output.txt", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d%d", &dest, &n);
		low = MAXX;
		for (int i = 1; i <= n; i++) {
			scanf("%d%d", pos + i, speed + i);
			if (speed[i] < low) low = speed[i];
		}
		hi = 1e14;
		int cnt = 0;
		while (hi-low>=1e-6) {
			if (cnt++ == 100) break;
			mid = (low + hi) / 2;
			p = (double)dest / mid;
			for (int i = 1; i <= n; i++) {
				if ((double)(dest - pos[i])*mid > (double)dest*(double)speed[i]) goto loop;
			}
			low = mid;
			continue;
		loop:;
			hi = mid;
		}
		printf("Case #%d: %.7lf\n",tc, mid);
	}
}