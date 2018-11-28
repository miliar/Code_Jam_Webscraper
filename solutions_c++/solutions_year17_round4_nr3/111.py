#include<algorithm>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include  <stdio.h>
#include   <math.h>
#include   <time.h>
#include   <vector>
#include   <bitset>
#include    <queue>
#include      <set>
#include      <map>
using namespace std;

const int N=505;

char s[N][N];
int n,m,tot,px[N],py[N],vis[N],las[N][N],Cant[N];
vector<int> G[N],Num[N];

void Adde(int t,int x,int y,int dx,int dy)
{
	if(x<1||y<1||x>n||y>m)
		return;
//	cout<<t<<" "<<x<<" "<<y<<" "<<s[x][y]<<endl;
	if(s[x][y]=='-'||s[x][y]=='|')
	{
		G[t].push_back(t^1);Cant[t]=1;
		return;
	}
	if(s[x][y]=='#')
		return;
	if(s[x][y]=='.')
	{
		if(las[x][y])
		{
			G[t^1].push_back(las[x][y]);
			G[las[x][y]^1].push_back(t);
			las[x][y]=-1;
		}
		else
			las[x][y]=t;
	}
	else if(s[x][y]=='/')
	{
		swap(dx,dy);dx*=-1;dy*=-1;
	}
	else
		swap(dx,dy);
	x+=dx;y+=dy;
	Adde(t,x,y,dx,dy);
}

int haha[N],ttt;

bool dfs(int x)
{
	if(vis[x^1])
		return 0;
	if(vis[x])
		return 1;
	vis[x]=1;haha[++ttt]=x;
	for(int i=0;i<G[x].size();i++)
		if(!dfs(G[x][i]))
		{
			vis[x]=0;return 0;
		}
	return 1;
}

void solve()
{
	scanf("%d%d\n",&n,&m);tot=0;
	memset(las,0,sizeof las);
	memset(Cant,0,sizeof Cant);
	for(int i=1;i<N;i++)
		G[i].clear(),vis[i]=0;
	for(int i=1;i<=n;i++)
	{
		scanf("%s",s[i]+1);
		for(int j=1;j<=m;j++)
			if(s[i][j]=='|'||s[i][j]=='-')
				tot++,px[tot]=i,py[tot]=j;
	}
	for(int i=1;i<=tot;i++)
	{
		Adde(i*2,px[i]-1,py[i],-1,0);
		Adde(i*2,px[i]+1,py[i],1,0);
		Adde(i*2+1,px[i],py[i]-1,0,-1);
		Adde(i*2+1,px[i],py[i]+1,0,1);
	//	cout<<i<<" "<<Cant[i*2]<<" "<<Cant[i*2+1]<<endl;
		if(Cant[i*2]&&Cant[i*2+1])
		{
			puts("IMPOSSIBLE");return;
		}
	}
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
		{
			if(s[i][j]=='.'&&!las[i][j])
			{
				puts("IMPOSSIBLE");return;
			}
			if(las[i][j]!=-1)
			{
				G[las[i][j]^1].push_back(las[i][j]);
			}
		}
	for(int i=1;i<=tot;i++)
		if(!vis[i*2]&&!vis[i*2+1])
		{
			ttt=0;
			if(!dfs(i*2))
			{
				while(ttt)
					vis[haha[ttt]]=0,ttt--;
				if(!dfs(i*2+1))
				{
					puts("IMPOSSIBLE");return;
				}
			}
		}
	puts("POSSIBLE");
	for(int i=1;i<=tot;i++)
	{
		if(vis[i*2])
			s[px[i]][py[i]]='|';
		else
			s[px[i]][py[i]]='-';
	}
	for(int i=1;i<=n;i++)
		printf("%s\n",s[i]+1);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
#endif
	int t;cin>>t;
	for(int i=1;i<=t;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}

