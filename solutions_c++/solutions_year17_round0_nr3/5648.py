#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
	long long int n,i,j,k,t,p,p1,p2,a[1000005];
	scanf("%lld",&t);
	for(i=0;i<t;i++)
	{
		scanf("%lld",&n);
		scanf("%lld",&k);
		a[0]=n;
		p=1;
		for(j=0;j<k-1;j++)
		{
			if(a[p-1]%2!=0)
			{
				a[p-1]=a[p-1]/2;
				a[p]=a[p-1];
			}
			else
			{
				a[p-1]=a[p-1]/2 - 1;
				a[p]=a[p-1]+1;
			}
			p++;
			sort(a,a+p);
		}
		if(a[p-1]%2!=0)
		{
			p1=a[p-1]/2;
			p2=p1;
		}
		else
		{
			p1=a[p-1]/2;
			p2=p1-1;
		}
		printf("Case #%lld: %lld %lld\n",i+1,p1,p2);
	}
	return 0;
}
