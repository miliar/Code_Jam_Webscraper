#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
    freopen("Cout7.out","w",stdout);
	lli t,n,x,y,i;
	scanf("%lld",&t);
	for(lli z=1;z<=t;++z)
	{
		printf("Case #%lld: ",z);
		bool flag=false;
		scanf("%lld",&n);
		for(i=n;i>=0 && !flag;--i)
		{
			x=i;
			y=9;
			flag=true;
			while(x>0)
			{
				if(x%10<=y)
				{
					y=x%10;
				}
				else
				{
					flag=false;
					break;
				}
				x/=10;
			}
		}
		printf("%lld\n",i+1);
	}
}
