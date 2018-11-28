#include <bits/stdc++.h>
using namespace std;

long long t,d,n,caso;
double k,s,a;


int main()
{
	scanf("%lld",&t);
	while(caso<t)
	{
		scanf("%lld%lld",&d,&n);
		for(int i=0;i<n;i++)
		{
			scanf("%lf%lf",&k,&s);
			a=max(a,(d-k)/s);
		}
		printf("Case #%lld: %.6lf\n",caso+1,d/a);
		caso++;
		a=0;
	}
}