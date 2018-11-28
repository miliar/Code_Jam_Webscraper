#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	ll t;
	scanf("%lld",&t);
	for(ll i=1;i<=t;i++)
	{
		ll d,n;
		scanf("%lld %lld",&d,&n);
		double time=0.0;
		for(ll j=0;j<n;j++)
		{
			ll k,s;
			scanf("%lld %lld",&k,&s);
			ll left=d-k;
			double tt=(double)left/(double)s;
			time=max(time,tt);
		}
		printf("Case #%lld: %lf\n",i,(double)d/time);
	}
	return 0;
}