#include <bits/stdc++.h>
using namespace std;
#define maxn 50

int a[maxn][maxn];
int n,m;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%d%d",&n,&m);
		char c;
		memset(a, -1, sizeof(a));
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++){
				scanf(" %c",&c);
				if (c=='?')
					a[i][j]=0;
				else
					a[i][j]=c-'A'+1;
			}
			
		for (int i=2;i<=n;i++){
			int flag=0;
			for (int j=1;j<=m;j++)
				if (a[i][j]!=0)
					flag=1;
			if (!flag)
				for (int j=1;j<=m;j++)
					a[i][j]=a[i-1][j];
		}
		for (int i=n-1;i>=1;i--){
			int flag=0;
			for (int j=1;j<=m;j++)
				if (a[i][j]!=0)
					flag=1;
			if (!flag)
				for (int j=1;j<=m;j++)
					a[i][j]=a[i+1][j];
		}

		for (int i=1;i<=n;i++){
			for (int j=2;j<=m;j++)	
				if (a[i][j-1]!=0 && a[i][j]==0)
					a[i][j]=a[i][j-1];
			for (int j=m-1;j>=1;j--)
				if (a[i][j+1]!=0 && a[i][j]==0)
					a[i][j]=a[i][j+1];
		}
		printf("Case #%d:\n", o);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
				printf(j==m?"%c\n":"%c",'A'+a[i][j]-1);
	}
	return 0;
}