#include<stdio.h>
long long int n, m;
long long int res;
long long int a, c;
long long int b[2];
long long int d[2];
int main()
{
//	freopen("C-small-2-attempt0.in", "rt", stdin);
//	freopen("C-small-2-attempt0.out", "wt", stdout);
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
	
	int t, tv = 0;
	int i, j, k, l;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%lld %lld", &n, &m);
		long long int tm = 1;
		a = n;
		b[0] = 1; b[1] = 0;
		while (m > tm) {
			//a * b[0] , a+1 * b[1]
			c = (a - 1) / 2;
			d[0] = d[1] = 0;
			d[0] += b[0];
			if (c == a / 2) { d[0] += b[0]; }
			else { d[1] += b[0]; }
			if (c == a / 2) { d[0] += b[1]; }
			else { d[1] += b[1]; }
			d[1] += b[1];

			a = c;
			b[0] = d[0];
			b[1] = d[1];
			m -= tm;
			tm *= 2;
		}
		if (m <= b[1])res = a + 1;
		else res = a;
		printf("Case #%d: %lld %lld\n", ++tv, res/2, (res-1)/2);
	}
}