/* ***********************************************
Author        :axp
Created Time  :2017/4/30 17:04:26
TASK		  :A.cpp
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
const int N = 1e3+10;
const double pi = acos(-1.0);
int n,m;
int T;
ll dp[N][N];
int r[N],h[N];
int p[N];

bool cmp(int x,int y)
{
	return r[x]>r[y];
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		cerr<<kase<<endl;
		scanf("%d%d",&n,&m);
		ll ans=0;
		memset(dp,0,sizeof dp);
		for(int i=0;i<n;i++)scanf("%d%d",&r[i],&h[i]),p[i]=i;
		sort(p,p+n,cmp);
		for(int i=0;i<n;i++)
		{
			int id=p[i];
			dp[1][i]=max(dp[1][i],1ll*r[id]*r[id]+2ll*r[id]*h[id]);
			for(int j=i+1;j<n;j++)
			{
				int t=p[j];
				for(int l=2;l<=m;l++)
					dp[l][j]=max(dp[l][j],dp[l-1][i]+2ll*r[t]*h[t]);
			}
		}
		for(int i=0;i<n;i++)ans=max(ans,dp[m][i]);
		printf("Case #%d: %.9lf\n",kase,pi*ans);
	}
    return 0;
}
