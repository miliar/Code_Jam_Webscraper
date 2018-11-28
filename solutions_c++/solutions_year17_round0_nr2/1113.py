#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 20;

int l;
char s[maxn];

int dp[maxn][10][2];

int sol(int p,int value,bool small)
{
	if(p>=l-1)
		return 1;
	if(dp[p][value][small]!=-1)
		return dp[p][value][small];
	int res = 0;
	if(small)
	{
		for(int i=value;i<=9;i++)
		{
			if(sol(p+1,i,1))
			{
				res = 1;
				break;
			}
		}
	}
	else
	{
		int x = s[p+1] - '0';
		for(int i=value;i<=x;i++)
		{
			if(sol(p+1,i,i<x?1:0))
			{
				res = 1;
				break;
			}
		}
	}
	dp[p][value][small] = res;
	return res;
}

int res[maxn];
int main()
{
	int t,cs=0;scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",++cs);
		scanf("%s",s);
		l = strlen(s);
		memset(dp,-1,sizeof(dp));
		int small = 0;
		for(int i=0;i<l;i++)
		{
			for(int j=small?9:s[i]-'0';j>=0;j--)
			{
				if(sol(i,j,small||(j<s[i]-'0')))
				{
					res[i] = j;
					break;
				}
			}
			if(small==0&&res[i]<s[i]-'0')
				small = 1;
		}
		bool f = 0;
		for(int i=0;i<l;i++)
		{
			if(res[i])
				f = 1;
			if(f||res[i])
				printf("%d",res[i]);
		}	
		puts("");
	}

}