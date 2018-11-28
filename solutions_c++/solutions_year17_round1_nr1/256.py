#include <bits/stdc++.h>

using namespace std;

const int N=1<<5;

char s[N][N];
int T,n,m,lt,cas;

int main()
{
	for(cin>>T;T--;)
	{
		cin>>n>>m;
		for(int i=0;i<n;i++)
			scanf("%s",s[i]);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				if(s[i][j]!='?') lt=i;

		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				if(s[i][j]!='?')
				{
					int l=j,r=j,x=i;
					for(l--;l>=0 && s[i][l]=='?';l--);l++;
					for(r++;r<m && s[i][r]=='?';r++);r--;
					for(x--;x>=0 && s[x][j]=='?';x--);x++;
					for(int u=x;u<=(i==lt?n-1:i);u++)
						for(int v=l;v<=r;v++)
							s[u][v]=s[i][j];
				}
		printf("Case #%d:\n",++cas);
		for(int i=0;i<n;i++)
			puts(s[i]);
	}
}