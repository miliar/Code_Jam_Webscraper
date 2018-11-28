#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<set>
#include<map>
#include<queue>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

#define rep(i,k,n) for(int i=(k);i<=(n);i++)
#define rep0(i,n) for(int i=0;i<(n);i++)
#define red(i,k,n) for(int i=(k);i>=(n);i--)
#define sqr(x) ((x)*(x))
#define clr(x,y) memset((x),(y),sizeof(x))
#define pb push_back
#define mod 1000000007
int n;
char s[30];

void dfs(int x)
{
	if(x==n)return;
	if(s[x]>s[x+1])
	{
		s[x]--;
		rep(i,x+1,n)s[i]='9';
	}
	else dfs(x+1);
	if(s[x]>s[x+1])
	{
		s[x]--;
		rep(i,x+1,n)s[i]='9';
	}
}

int main()
{
	freopen("C:\\tmpcode\\gcj\\2017\\qround\\b\\B-large.in", "r", stdin);
	freopen("C:\\tmpcode\\gcj\\2017\\qround\\b\\mylargeoutput.txt", "w", stdout);
	int T;scanf("%d",&T);
	rep(ii,1,T)
	{
		
		scanf("%s",s+1);
		n=strlen(s+1);
		dfs(1);
		
		int t=1;
		while(s[t]=='0')t++;
		printf("Case #%d: %s\n",ii,s+t);
	}
	
	
	return 0;
}
