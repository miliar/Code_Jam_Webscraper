#include<bits/stdc++.h>
#define MI 1000000000
#define X first
#define Y second
#define MP make_pair
#define MT make_tuple
#define EB emplace_back
using namespace std;
int n;
char s[23];
long long jum[23][13][3];
long long dp(int idx,int bd,int st,long long num)
{
	if(idx>n)
		return num;
	int i;
	long long j;
	if(st==1)
	{
		if(s[idx]-'0'>=bd)
		{
			j=dp(idx+1,s[idx]-'0',1,num*10+s[idx]-'0');
			if(j)return jum[idx][bd][st]=j;
		}
		for(i=s[idx]-'0'-1;i>=bd;i--)
		{
			j=dp(idx+1,i,0,num*10+i);
			if(j)return jum[idx][bd][st]=j;
		}
	}
	else
	{
		for(i=9;i>=bd;i--)
		{
			j=dp(idx+1,i,0,num*10+i);
			if(j)return jum[idx][bd][st]=j;
		}
	}
	return jum[idx][bd][st]=0;
}
int main()
{
	freopen("out.txt","w",stdout);
	//freopen("in.txt","r",stdin);
	int t,T,i,j,k;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		memset(jum,-1,sizeof jum);
		memset(s,-1,sizeof s);
		scanf("%s",s+1);
		n=strlen(s+1);
		printf("Case #%d: %lld\n",t,dp(1,0,1,0ll));
	}
}