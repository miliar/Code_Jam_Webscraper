#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
#define inf 100000000000000000
string str,ans;
int len,dp[30][11][3],vis[30][11][3],pp;
int go(int pos,int pre,int f)
{
	if(pos>=len)
	return dp[pos][pre][f]=1;
	
	if(vis[pos][pre][f]==pp)
	return dp[pos][pre][f];
	
	int end,i,r;
	r = 0;
	end = str[pos]-'0';
	for(i=0;i<=9;i++)
	{
		if(f and i>end)
		break;
		if(i>=pre)
		r|= go(pos+1,i,(i<end)?0:f);
	}
	
	vis[pos][pre][f] = pp;
	return dp[pos][pre][f] = r;
}
void solve(int pos,int pre,int f)
{
	if(pos>=len)
	return ;
	
	int end,i,r;
	r = 0;
	end = str[pos]-'0';
	for(i=0;i<=9;i++)
	{
		if(f and i>end)
		break;
		if(i>=pre)
		{
			if(dp[pos+1][i][(i<end)?0:f]==1)
			{
				r = max(r,i);
			}
		}
	}
	ans+=(r+'0');
	solve(pos+1,r,(r<end)?0:f);
	
}
int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
	int tcase,t,i,j,k;
	pp = 2;
	scanf("%d",&tcase);
	for(t=1;t<=tcase;t++)
	{
		cin>>str;
		len = str.size();
		for(i=0;i<30;i++)
		for(j=0;j<11;j++)
		for(k=0;k<3;k++)
		dp[i][j][k] = 0;
		pp++;
		go(0,0,1);
		ans = "";
		solve(0,0,1);
		len = ans.size();
		for(i=0;i<len;i++)
		if(ans[i]!='0')
		break;
		printf("Case #%d: ",t);
		for(;i<len;i++)
		cout<<ans[i];
		cout<<endl;
		
	}
}

