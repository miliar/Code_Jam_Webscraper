#include<cstdio>
int main()
{
	int T;
	long long k,n,b1,b2,c1,c2,v;
	scanf("%d",&T);
	for(int I=1;I<=T;I++)
	{
		c1=1;	c2=0;
		scanf("%lld%lld",&n,&k);
		while(c1+c2<k)
		{
			b1=c1;	b2=c2;
			k-=c1+c2;
			if(n%2)
			{
				c1=2*b1+b2;
				c2=b2;
			}
			else
			{
				c1=b1;
				c2=b1+2*b2;
			}
			n/=2;
			//printf("= %lld -> %lld %lld\n",n,c1,c2);
		}
		if(k<=c1)
			printf("Case #%d: %lld %lld\n",I,n/2,(n-1)/2);
		else
			printf("Case #%d: %lld %lld\n",I,(n-1)/2,n/2-1);
	}
}