#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,cas,l,i,j;
	char n[20],ans[20];
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		scanf("%s",n);
		l=strlen(n);
		for(i=0;i<l;++i)
		{
			for(j=i+1;j<l;++j)
			{
				if(n[j]>n[i])
				{
					ans[i]=n[i];
					break;
				}
				if(n[j]<n[i])
				{
					ans[i]=n[i]-1;
					for(++i;i<l;++i)
					{
						ans[i]='9';
					}
					break;
				}
			}
			if(j==l)
			{
				ans[i]=n[i];
			}
		}
		ans[l]=0;
		for(i=0;ans[i]=='0';++i);
		printf("Case #%d: %s\n",cas,ans+i);
	}
	return 0;
}
/*
4
132
1000
7
111111111111111110
*/

