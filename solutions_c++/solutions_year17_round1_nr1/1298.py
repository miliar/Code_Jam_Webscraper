#include <bits/stdc++.h>

using namespace std;

int n,m;
int a[50][50];

inline char read()
{
	char c=getchar();

	while((c<'A'||c>'Z')&&c!='?')c=getchar();

	return c;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				a[i][j]=read();

		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
			{
				if(a[i][j]=='?')
					for(int k=j+1;k<=m;k++)
						if(a[i][k]!='?')
						{
							a[i][j]=a[i][k];
							break;
						}
				if(a[i][j]=='?')
					for(int k=j-1;k;k--)
						if(a[i][k]!='?')
						{
							a[i][j]=a[i][k];
							break;
						}
			}
		}

		for(int i=1;i<=n;i++)
		{
			if(a[i][1]=='?')
				for(int k=i-1;k;k--)
					if(a[k][1]!='?')
					{
						for(int LL=1;LL<=m;LL++)
							a[i][LL]=a[k][LL];
						break;
					}
			if(a[i][1]=='?')
				for(int k=i+1;k<=n;k++)
					if(a[k][1]!='?')
					{
						for(int LL=1;LL<=m;LL++)
							a[i][LL]=a[k][LL];
						break;
					}
		}

		printf("Case #%d:\n",tt);

		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
				printf("%c",a[i][j]);
			printf("\n");
		}
	}

	return 0;
}