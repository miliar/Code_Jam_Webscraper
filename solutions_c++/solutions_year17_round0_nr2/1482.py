#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
typedef long long LL;
int a[30];
LL n;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	cin>>T;
	for(int ii=1;ii<=T;++ii)
	{
		a[0]=0;
		scanf("%I64d",&n);
		while(n)
		{
			a[++a[0]]=n%10;
			n/=10;
		}
		while(true)
		{
			bool flag=true;
			for(int i=a[0];i>=2;--i)
			{
				if(a[i-1]<a[i])
				{
					a[i]--;
					if(i==a[0]&&a[i]==0) a[0]--;
					for(int j=i-1;j>=1;--j) a[j]=9;
					flag=false;
					break;
				}
			}
			if(flag) break;
		}
		printf("Case #%d: ",ii);
		for(int i=a[0];i>=1;--i)
			printf("%d",a[i]);
		printf("\n");
	}
	return 0;
}