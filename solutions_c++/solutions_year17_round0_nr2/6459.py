#include<cstdio>
#include<cstring>
#include<algorithm>
#define N 100005
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);  
    freopen("sample2_l.out", "w", stdout);  
	long long x,a[20],tmp;
	int i,j,t,n,k,tt=0;
	a[0]=1;
	for(i=1;i<=18;i++)
	{
		a[i]=a[i-1]*10;
	}
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lld",&x);
		tmp=x;
		k=0;
		for(i=0;;i++)
		{
			k++;
			tmp/=10;
			if(tmp==0)
				break;
		}
		printf("Case #%d: ",++tt);
		if(k==1)
		{
			printf("%lld\n",x);
			continue;
		}
		for(i=k-1;i>0;i--)
		{
	//		printf("&&& %d\n",d[i]);
			if((x/a[i]%10)>(x/a[i-1]%10))
			{
				x-=a[i];
				x/=a[i];
				x*=a[i];
				x+=a[i]-1;
				if(i<k-1)
				{
					i+=2;
				}
			}
		}
		printf("%lld\n",x);
	}
}
