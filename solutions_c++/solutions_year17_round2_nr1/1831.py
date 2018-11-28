#include<bits/stdc++.h>
using namespace std;

#define pii pair< int,int >
#define ll long long

int main()
{
	ll i,j,k,n,t,d,x,y;
	scanf("%lld",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%lld%lld",&d,&n);
		double tt,tm=INT_MIN;
		for(j=0;j<n;j++)
		{
			cin>>x>>y;
			tt=(double)(d-x)/(double)(y);
			if(tt>tm)
				tm=tt;
			
		}
		float ans=(double)(d)/tm;
			printf("Case #%lld: %f\n",i,ans);
	}
	return 0;
}
