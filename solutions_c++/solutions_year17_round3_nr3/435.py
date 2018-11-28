#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#define EPS 0.0000000000001L
using namespace std;
long double p[51];
int main()
{
	int t;
	scanf("%d", &t);
	for (int c=0; c<t; c++)
	{
		printf("Case #%d: ", c+1);
		int n, k;
		scanf("%d%d", &n, &k);
		long double u;
		scanf("%Lf", &u);
		for (int i=0; i<n; i++)
		{
			scanf("%Lf", &p[i]);
		}
		long double l=0.0, r=1.0;
		while (fabs(r-l)>EPS)
		{
			long double m=(l+r)/2;
			long double sum=0.0;
			for (int j=0; j<n; j++)
			{
				if (p[j]<m) sum+=m-p[j];
			}
			if (sum>u) r=m; else l=m;
		}
		//printf("%Lf\n", l);
		long double ans=1.0;
		for (int i=0; i<n; i++)
		{
			if (p[i]<l) ans*=l;
			else ans*=p[i];
		}
		printf("%.10Lf\n", ans);
	}
	return 0;
}