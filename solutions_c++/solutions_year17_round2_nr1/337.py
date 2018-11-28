#include<stdio.h>
int n;
double m;
double a[100009];
double v[100009];
bool able(double x) {
	int i, j, k;
	for (i = n - 1; i >= 0; i--) {
		if ((m - a[i]) > x * v[i])
			return false;
	}
	return true;
}
int main() {
//	freopen("A-small-attempt0.in", "rt", stdin);
//	freopen("A-small-attempt0.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int t=1, tv = 0;
	int i, j, k, l;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%lf %d", &m, &n);
		for (i = 0; i < n; i++) {
			scanf("%lf %lf", &a[i], &v[i]);
		}
		double l, r, mid;
		l = 0; r = m + 1;
		int ccnt = 200;
		while(ccnt--)
		{
			mid = (l + r) / 2;
			if (able(mid))
				r = mid;
			else
				l = mid;
		}
		printf("Case #%d: %lf\n", ++tv, m/l);
	}
}