#include <stdio.h>
int main()
{
	freopen( "C-large.in", "r", stdin );
	freopen( "output1.txt", "w", stdout );
	long long int n,t,i,sum,rsv,lol,a,b,c,d,k;
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf("%lld%lld",&n,&k);
		i=1;sum=1;
		long long int A,B,C,D;
		a=n/2;b=a-1;c=1;d=1;
		if(n%2==1)
		{
			c=2;d=0;
		}
		while(true)
		{
			i*=2;
			sum+=i;
			if(sum>=k)
			{
				sum-=i;
				break;
			}
			A=a/2;B=A-1;
			if(a%2==1)
			{
				C=(2*c)+d;
				D=d;
			}
			else
			{
				C=c;
				D=(2*d)+c;
			}
			a=A;b=B;c=C;d=D;
		}
		sum=k-sum;
		if(c>=sum)rsv=a;
		else rsv=b;
		if(k==1)rsv=n;
		printf("Case #%lld: %lld %lld\n",lol,rsv/2,(rsv-1)/2);
	}
	return 0;
}
		
