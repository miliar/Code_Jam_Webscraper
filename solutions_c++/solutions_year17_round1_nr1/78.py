#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
int n,m;
char s[50][50];
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int qi=1;qi<=T;qi++)
	{
		printf("Case #%d:\n",qi);
		scanf("%d%d",&n,&m);
		memset(s,0,sizeof(s));
		for(int i=1;i<=n;i++)
			scanf("%s",s[i]+1);
		for(int i=1;i<=n;i++)
		{
			char t='?';
			for(int j=1;j<=m;j++)
				if(s[i][j]!='?')t=s[i][j];
			if(t!='?')
			{
				for(int j=m;j;j--)
					if(s[i][j]=='?')s[i][j]=t;
					else t=s[i][j];
			}
		}
		for(int i=1;i<=m;i++)
		{
			char t='?';
			for(int j=1;j<=n;j++)
				if(s[j][i]!='?')t=s[j][i];
			if(t!='?')
			{
				for(int j=n;j;j--)
					if(s[j][i]=='?')s[j][i]=t;
					else t=s[j][i];
			}
		}
		for(int i=1;i<=n;i++)
			puts(s[i]+1);
	}
	return 0;
}

