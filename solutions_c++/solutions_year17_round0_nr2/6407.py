#include<cstdio>
#define ___ freopen("d:\\acm\\input.txt","r",stdin);
typedef long long ll;
int dig[30],ed;
int cas;
int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		long long a;
		scanf("%lld",&a);
		for(ed=0;a;a/=10)dig[++ed]=a%10;
		for(int i=1;i<ed;i++)
		{
			if(dig[i]<0)
			{
				dig[i]=9,dig[i+1]--;
				for(int j=i-1;j>=1;j--)dig[j]=9;
			}
			if(dig[i]<dig[i+1])
			{
				dig[i]=9;
				dig[i+1]--;
				for(int j=i-1;j>=1;j--)dig[j]=9;
			}
		}
		ll ans=0;
		for(int i=ed;i>=1;i--)ans=ans*10+dig[i];
		printf("Case #%d: %lld\n",++cas,ans);
	}
	return 0;
}