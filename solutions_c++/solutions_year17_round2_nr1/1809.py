#include<stdio.h>

void solve(void)
{
	int d, n;
	double hours = -1;
	double tmp;
	
	scanf("%d %d", &d, &n);
	
	int s, v;

	for(int i=0; i<n; i++)
	{
		scanf("%d %d", &s, &v);
		tmp = (double) (d - s) / v;
		if(tmp > hours) hours = tmp;
	}
	
	printf("%lf\n", d/hours);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	
	for(int i=1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}
