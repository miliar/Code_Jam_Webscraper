#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int kk;
	for(kk=1;kk<=t;kk++)
	{
		long long n;
		scanf("%lld",&n);
		printf("Case #%d: ",kk);
		int flag=0;
		long long num=n;
		int lastd=9;
		while(num)
		{
			int dig=num%10;
			if(dig>lastd)
			{
				flag=1;
				break;
			}
			num=num/10;
			lastd=dig;
		}
		if(flag==0)
		{
			printf("%lld\n",n);
			continue;
		}
		num=n;
		while(1)
		{
			num=num/10;
			num=num*10;
			num--;
			long long num1=num;
			lastd=9;
			flag=1;
			while(num1)
			{
				int dig=num1%10;
				if(dig>lastd)
				{
					flag=0;
					break;
				}
				num1=num1/10;
				lastd=dig;
			}
			if(flag==1)
			{
				//printf("%lld\n",n);
				break;
			}
			//if(num>100)
			//printf("%lld\n",num);
		}
		printf("%lld\n",num);
	}
	return 0;
}
