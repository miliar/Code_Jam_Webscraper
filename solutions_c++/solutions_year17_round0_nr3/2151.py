#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int cas,T,i;
	long long n,k,sum,sum1,sum2,l1,l2,t;
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		scanf("%lld%lld",&n,&k);
		
		sum=sum2=0;
		sum1=1;
		l1=l2=n;
		while(sum+sum1+sum2<k)
		{
			sum+=sum1+sum2;
			if((l1&1) && (l2&1))
			{
				sum1<<=1;
				l1=(l2>>=1);
			}
			else if((l1&1) && !(l2&1))
			{
				sum1=(sum1<<1)+sum2;
				l1>>=1;
				l2-=l1+1;
			}
			else if(!(l1&1) && (l2&1))
			{
				sum2=(sum2<<1)+sum1;
				l1=(l1-1)>>1;
				l2>>=1;
			}
			else
			{
				sum1=(sum2+=sum1);
				l1=(l1-1)>>1;
				l2-=l1+1;
			}
		}
		if(sum+sum2<k)
		{
			l2=l1;
		}
		printf("Case #%d: %lld %lld\n",cas,l2>>1,max(l2-(l2>>1)-1,0LL));
	}
	return 0;
}
/*
5
4 2
5 2
6 2
1000 1000
1000 1
*/

