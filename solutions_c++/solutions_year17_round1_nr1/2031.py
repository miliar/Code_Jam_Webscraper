/* ***********************************************
Author        :yuanzhaolin
Created Time  :2017/4/15 9:16:10
File Name     :a.cpp
************************************************ */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <utility>
using namespace std;
#define repp(i,a,b) for(int i=a;i<=b;i++)
#define rep(i,a) for(int i=0;i<a;i++)
#define REP(i,a) for(int i=1;i<=a;i++)
#define per(i,a,b) for(int i=a-1;i>=b;i--)
#define foreach(i,a) for(int i=head[a];i>=0;i=ee[i].next)
#define Foreach(i,a) for(__typeof((a).begin())i=(a).begin();i!=(a).end();i++)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define m0(x) memset(x,0,sizeof(x))
#define mff(x) memset(x,0xff,sizeof(x))
#define fi first
#define se second
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define SZ(x) ((int)(x).size())
#define sqr(x) ((x)*(x))
#define C1(x) cout<<x<<endl
#define C2(x,y) cout<<x<<" "<<y<<endl
#define C3(x,y,z) cout<<x<<" "<<y<<" "<<z<<endl
typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< pair<int,int> > VPII;
const ll mod=(ll)1e9+7;
const ll maxn=(ll)1e5+7;
const ll maxe=(ll)1e6+7;
const ll INF=(ll)1e9+7;
const double PI=acos(-1);
int dx[4]={0,0,1,-1};
int dy[4]={-1,1,0,0};
char a[30][30];
string s;
int n,m;
bool vis[300];
int findR(int x,int y)
{
	for(int i=y+1;i<=m;i++)
	{
		if(a[x][i]!='?') return i-1;
	}
	return m;
}
int findL(int x,int y)
{
	for(int i=y-1;i>=1;i--)
	{
		if(a[x][i]!='?') return i+1;
	}
	return 1;
}
int findU(int row,int l,int r)
{
	for(int i=row-1;i>=1;i--)
	{
		for(int j=l;j<=r;j++) if(a[i][j]!='?') return i+1;
	}
	return 1;
}
int findD(int row,int l,int r)
{
	for(int i=row+1;i<=n;i++)
	{
		for(int j=l;j<=r;j++) if(a[i][j]!='?') return i-1;
	}
	return n;
}
void paint(int l,int r,int u,int d,char c)
{
	for(int i=u;i<=d;i++)
	{
		for(int j=l;j<=r;j++)
			a[i][j]=c;
	}
}
void solve()
{
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=m;j++)
		{
			if(a[i][j]!='?'&&!vis[a[i][j]])
			{
				int c=(int)a[i][j];
			//	cout<<c<<endl;
				vis[c]=true;
				int l=findL(i,j);
				int r=findR(i,j);
				int u=findU(i,l,r);
				int d=findD(i,l,r);
				paint(l,r,u,d,(char)c);
			}
		}
	}
}
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   	int T; 
   	cin>>T;
   	for(int ca=1;ca<=T;ca++)
	{
		cin>>n>>m;
		memset(vis,false,sizeof(vis));
		memset(a,0,sizeof(a));
		for(int i=1;i<=n;i++)
		{
			cin>>s;
			for(int j=1;j<=m;j++) a[i][j]=s[j-1];
		}
		solve();
		printf("Case #%d:\n",ca);
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
				printf("%c",a[i][j]);
			cout<<endl;
		}	
	}
    return 0;
}
