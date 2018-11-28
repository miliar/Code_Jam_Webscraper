#include<bits/stdc++.h>

#define ll long long 

int main()
{
	ll t,i;
	scanf("%lld",&t);
	for(i=0;i<t;i++)
	{
		printf("Case #%lld: ",i+1);
		ll d,n;
		scanf("%lld%lld",&d,&n);
		ll i,k,s;
		double time,max=-1,ans;
		for(i=0;i<n;i++)
		{
			scanf("%lld%lld",&k,&s);
			time=(double)(d-k)/(double)s;
			if(time>max)
			{
				max=time;
			}
		}
		ans=(double)d/max;
		printf("%f\n",ans);
	}
	return 0;
}
