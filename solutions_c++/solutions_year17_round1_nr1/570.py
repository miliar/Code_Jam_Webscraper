#include <bits/stdc++.h>
using namespace std;

const int MAXN=30;

char a[MAXN][MAXN];
bool flag[MAXN];

void solve()
{
	int r,c;
	scanf("%d%d",&r,&c);
	for (int i=1;i<=r;i++)
		scanf("%s",a[i]);
	for (int i=0;i<c;i++)
	{
		flag[i]=false;
		for (int j=1;j<=r;j++)
			if (a[j][i]!='?')
			{
				flag[i]=true;
				for (int k=j-1;k>=1&&a[k][i]=='?';k--)
					a[k][i]=a[j][i];
				for (int k=j+1;k<=r&&a[k][i]=='?';k--)
					a[k][i]=a[j][i];
			}
	}
	for (int i=0;i<c;i++)
		if (flag[i])
		{
			for (int j=i-1;j>=0&&!flag[j];j--)
			{
				flag[j]=true;
				for (int k=1;k<=r;k++)
					a[k][j]=a[k][i];
			}
			for (int j=i+1;j<c&&!flag[j];j--)
			{
				flag[j]=true;
				for (int k=1;k<=r;k++)
					a[k][j]=a[k][i];
			}
		}
	for (int i=1;i<=r;i++)
		puts(a[i]);
}

int main()
{
	freopen("read.txt","r",stdin);
	freopen("write.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d:\n",i);
		solve();
	}
	return 0;
}
