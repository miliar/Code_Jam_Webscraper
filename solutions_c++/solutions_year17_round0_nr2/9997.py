#include <cstdio>
#include <algorithm>
#define LL long long
using namespace std;
LL solve(LL x)
{
	LL a[20],len=0,ans=x;
	while(x)
	{
		a[++len]=x%10;
		x=x/10;
	}
	for(LL i=len;i>=2;i--)
	{
		if(a[i]>a[i-1])
		{
			ans=0;
			LL j=i;
			while(a[j]==a[j+1]) j++;
			if(a[j]==1)
			{
				for(LL i=1;i<len;i++)
					ans=ans*10+9;
			} 
			else
			{
				a[j]--;
				for(LL k=j-1;k;k--) a[k]=9;
				for(LL k=len;k;k--) ans=ans*10+a[k];
			}
			break;
		}
	}
	return ans;
}
int main()
{
	LL t;
	//freopen("test.in","r",stdin);
	//freopen("test.out","w",stdout);
	scanf("%lld",&t);
	for(LL k=1;k<=t;k++)
	{
		LL n;
		scanf("%lld",&n);
		printf("Case #%lld: ",k);
		printf("%lld\n",solve(n));
	}
	return 0;
}