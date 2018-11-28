//Rsv
#include <stdio.h>
int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	long long int n,t,i,sum,lol,k,s,d;
	double time,rsv;
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf("%lld%lld",&d,&n);
		scanf("%lld%lld",&k,&s);
		time=((d-k)*1.0000000)/(s*1.0000000);
//		printf(%)
		for(int i=1;i<n;i++)
		{
			scanf("%lld%lld",&k,&s);
			double temp=((d-k)*1.0000000)/(s*1.0000000);
			if(temp>time)
			time=temp;
		}
		rsv=(d*1.0000000)/time;
		printf("Case #%lld: %.7f\n",lol,rsv);
	}
	return 0;
}
		
