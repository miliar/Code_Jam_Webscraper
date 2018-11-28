/* ***********************************************
Author        :axp
Created Time  :2017/4/30 17:30:31
TASK		  :B.cpp
LANG          :C++
************************************************ */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef long long ll;
const int inf = 1<<30;
const int md = 1e9+7;
const int lim = 1440;
const int N = lim+10;
int dp[2][N][N];
int c[N];
int n,m;
int T;
bool vis[2][N][N];

int f(bool k,int now,int all)
{
	all+=k;
	int &re=dp[k][now][all];
	if(vis[k][now][all])return re;
	vis[k][now][all]=1;
	if(all>lim/2)return re=inf;

	if(now==lim)
	{
		re=((all==lim/2)?0:inf);
		if(k)re++;
		return re;
	}
	if(c[now]==k+1)return re=inf;

	re=min(f(k,now+1,all),f(k^1,now+1,all)+1);
	return re;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		cerr<<kase<<endl;
		scanf("%d%d",&n,&m);
		memset(c,0,sizeof c);
		int l,r;
		for(int i=0;i<n;i++)
		{
			scanf("%d%d",&l,&r);
			for(int j=l;j<r;j++)
				c[j]=1;
		}
		for(int i=0;i<m;i++)
		{
			scanf("%d%d",&l,&r);
			for(int j=l;j<r;j++)
				c[j]=2;
		}
		memset(vis,0,sizeof vis);
		int ans=f(0,0,0);
		for(int i=0;i<N;i++)
			if(c[i])
				c[i]=3-c[i];
		memset(vis,0,sizeof vis);
		ans=min(ans,f(0,0,0));
		printf("Case #%d: %d\n",kase,ans);
	}
    return 0;
}
