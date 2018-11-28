#include <stdio.h>
#include <queue>
using namespace std;

int main()
{
	long long t,n,l,num,now,k,x=0;
	scanf("%lld",&t);
	while(t--)
	{
		scanf("%lld%lld",&n,&k);
		num=now=1,l=1;
		while(num<k)
		{
			if(n%2) l+=now;
			now*=2;
			num+=now;
			n/=2;
		}
		n--;
		if(now+l<=k) n--;
		//printf("%lld %lld\n",now,l);
		printf("Case #%lld: %lld %lld\n",++x,n-n/2,n/2);
	}
} 
