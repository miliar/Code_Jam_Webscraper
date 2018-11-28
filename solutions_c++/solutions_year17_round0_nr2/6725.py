#include<bits/stdc++.h>
using namespace std;

#define ll long long int
int main ()
{
	int t;
	scanf("%d",&t);
	for(int ct=1;ct<=t;ct++)
	{
		ll n,cnt=0,ar[25],ans,x;
		scanf("%lld",&n);
		x = n;
		while(x)
		{
			ar[cnt++] = x%10;
			x/=10;
		}
		int flg = 10;
		for(int i=cnt-1;i>=0;i--)
		{
			if(flg==20)ar[i]=9;
			else
			{
				if(ar[i]>ar[i-1])
				{
					ar[i]--;
					flg = 20;
				}
			}
		}
		for(int i=1;i<cnt;i++)
		{
			if(ar[i]>ar[i-1])
			{
				ar[i-1] = 9;
				ar[i]--;
			}
		}
		ll base = 1;
		ans = 0;
		for(int i=0;i<cnt;i++)
		{
			ans+=(base*ar[i]);
			base*=10;
		}
		printf("Case #%d: ",ct);
		printf("%lld",ans);
		if(ct!=t)printf("\n");
	}
}
