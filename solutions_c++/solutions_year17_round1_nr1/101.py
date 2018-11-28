#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char a[30][30],b[30][30];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		int n,m;scanf("%d%d",&n,&m);
		int k=0;
		for (int i=1;i<=n;i++) scanf("%s",a[i]+1);
		for (int i=1;i<=n;i++)
		{
			bool ok=0;
			for (int j=1;j<=m;j++) if (a[i][j]!='?') ok=1;
			if (ok)
			{
				int x=0;
				for (int j=1;j<=m;j++)
					if (a[i][j]!='?')
					{
						for (int p=j;p>x;p--) b[i][p]=a[i][j];
						x=j;
					}
				for (int j=x+1;j<=m;j++) b[i][j]=b[i][x];
				for (int j=k+1;j<i;j++)
					for (int p=1;p<=m;p++)
						b[j][p]=b[i][p];
			    k=i;
			}
		}
		for (int i=n;i>k;i--)
			for (int j=1;j<=m;j++)
				b[i][j]=b[k][j];
		printf("Case #%d:\n",T);
		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=m;j++) putchar(b[i][j]);
			puts("");
		}
	}
	return 0;
}
			
