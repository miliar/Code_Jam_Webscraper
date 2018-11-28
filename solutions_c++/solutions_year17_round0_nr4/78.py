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

const int N=205;

int n,m,ok1l[N],ok2l[N],ok1r[N],ok2r[N],changed[N][N],Now[N][N],vis[N],mr[N],ml[N];

bool dfs(int x)
{
	if(vis[x])
		return 0;
	vis[x]=1;
	for(int y=1;y<2*n;y++)
	{
		if(!ok1r[y]&&(x+y-n+1)/2>=1&&(x+y-n+1)/2<=n&&(x-y+n+1)/2>=1&&(x-y+n+1)/2<=n&&(x+y-n+1)%2==0&&(!mr[y]||dfs(mr[y])))
		{
			mr[y]=x;ml[x]=y;
			return 1;
		}
	}
	return 0;
}

void solve()
{
	scanf("%d %d\n",&n,&m);
	memset(ok1l,0,sizeof ok1l);
	memset(ok1r,0,sizeof ok1r);
	memset(ok2l,0,sizeof ok2l);
	memset(ok2r,0,sizeof ok2r);
	memset(changed,0,sizeof changed);
	memset(Now,0,sizeof Now);
	memset(ml,0,sizeof ml);
	memset(mr,0,sizeof mr);
	for(int i=1;i<=m;i++)
	{
		char type;int x,y;
		scanf("%c %d %d\n",&type,&x,&y);
	//	cout<<type<<" "<<x<<" "<<y<<endl;
		if(type=='o')
			ok1l[x+y-1]=ok1r[x-y+n]=ok2l[x]=ok2r[y]=1,Now[x][y]=3;
		if(type=='+')
			ok1l[x+y-1]=ok1r[x-y+n]=1,Now[x][y]=1;
		if(type=='x')
			ok2l[x]=ok2r[y]=1,Now[x][y]=2;
	}
	for(int i=1;i<2*n;i++)
		if(!ok1l[i]&&!ml[i])
		{
			memset(vis,0,sizeof vis);
			dfs(i);
		}
	for(int i=1;i<2*n;i++)
		if(!ok1l[i]&&ml[i])
			changed[(i+ml[i]-n+1)/2][(i-ml[i]+n+1)/2]++;//,cout<<(i+ml[i]-n+1)/2<<" "<<(i-ml[i]+n+1)/2<<endl;
	//for(int i=1;i<2*n;i++)
	//	cout<<ml[i]<<" "<<mr[i]<<endl;
	for(int i=1;i<=n;i++)
		if(!ok2l[i])
		{
			int flag=0;
			for(int j=1;j<=n;j++)
				if(!ok2r[j])
				{
					ok2l[i]=ok2r[j]=1;
					changed[i][j]+=2;
					flag=1;break;
				}
			if(!flag)
				break;
		}
	m=0;
	int Ans=0;
	for(int i=1;i<=n;i++)//,cout<<endl)
		for(int j=1;j<=n;j++)
		{
			changed[i][j]+=Now[i][j];
			if(Now[i][j]!=changed[i][j])
			{
				m++;//cout<<Now[i][j]<<" "<<changed[i][j]<<endl;
			}
			//cout<<changed[i][j]<<" ";
			if(changed[i][j]==1)
				Ans++;
			if(changed[i][j]==2)
				Ans++;
			if(changed[i][j]==3)
				Ans+=2;
		}
	cout<<Ans<<" "<<m<<endl;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			if(Now[i][j]!=changed[i][j])
			{
				if(changed[i][j]==1)
					printf("+ %d %d\n",i,j);
				if(changed[i][j]==2)
					printf("x %d %d\n",i,j);
				if(changed[i][j]==3)
					printf("o %d %d\n",i,j);
			}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
#endif
	int T;cin>>T;
	for(int i=1;i<=T;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}

