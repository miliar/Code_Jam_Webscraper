/* ***********************************************
Author        :axp
Created Time  :2017/5/13 22:09:07
TASK		  :1.cpp
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
int md;
const int N = 105;
const int M = 4;
int n,m;
int T;
bool vis[M][N][N][N];
int dp[M][N][N][N];
int c[M];

int f(int now,int a,int b,int c)
{
	int &re=dp[now][a][b][c];
	if(vis[now][a][b][c])return re;
	vis[now][a][b][c]=1;

	int tmp[3]={a,b,c};
	re=0;
	if(a+b+c==0)return re=0;
	int t=0;
	if(now==0)t=1;

	for(int i=0;i<3;i++)
		if(tmp[i])
		{
			tmp[i]--;
			int v=(now+i+1)%md;
			re=max(re, f(v,tmp[0],tmp[1],tmp[2]));
			tmp[i]++;
		}
	return re+=t;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%d%d",&n,&md);
		memset(c,0,sizeof c);
		memset(vis,0,sizeof vis);

		int x;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&x);
			c[x%md]++;
		}
		int ans=c[0]+f(0,c[1],c[2],c[3]);
		printf("Case #%d: %d\n",kase,ans);
	}
    return 0;
}
