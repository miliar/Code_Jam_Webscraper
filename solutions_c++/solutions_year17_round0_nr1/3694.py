#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int p=1;
	while(t--)
	{
		char a[100010];
		int b[100010];
		scanf("%s",a);
		int l;
		l=strlen(a);
		for(int i=0;i<l;i++)
		{
			if(a[i]=='+')
				b[i]=1;
			else
				b[i]=0;
		}
		int m,f=0;
		scanf("%d",&m);
		for(int i=0;i<l-m+1;i++)
		{
			if(b[i]!=1)
			{
				f++;
				for(int j=i;j<i+m;j++)
				{
					b[j]=(1-b[j]);
				}
			}
		}
		int g=0;
		for(int i=0;i<l;i++)
		{
			if(b[i]==0)
			{
				g=1;
				break;
			}
		}
		printf("Case #%d: ",p);
		if(g==1)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n",f);
		}
		p++;
	}
}