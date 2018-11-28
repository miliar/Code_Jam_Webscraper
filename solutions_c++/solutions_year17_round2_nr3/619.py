#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<iostream>
typedef long long LL;
#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define PII pair<LL,LL>
using namespace std;
int Te;
int n,K;
PII p[110];
bool vis[110];
double dis[110];
queue<int> h;
LL g[110][110];
int x,y;
template<class T>
void read(T&x)
{
	char ch=getchar();int mk=1;x=0;for(;ch!='-'&&(ch<'0'||ch>'9');ch=getchar());
	if (ch=='-') mk=-1,ch=getchar();for(;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-48;x*=mk;
}
double spfa(int st,int en)
{
	for(int i=1;i<=n;i++) vis[i]=0,dis[i]=1e20;
	dis[st]=0;
	vis[st]=1;
	h.push(st);
	while (h.size())
	{
		int u=h.front();
		for(int v=1;v<=n;v++)
			if (g[u][v]!=-1&&p[u].fi>=g[u][v])
			{
				double tmp=dis[u]+(double)g[u][v]/p[u].se;
				if (tmp<dis[v])
				{
					dis[v]=tmp;
					if (!vis[v])
					{
						vis[v]=1;
						h.push(v);
					}
				}
			}
		h.pop();
		vis[u]=0;
	}
	return dis[en];
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&Te);
	for(int _=1;_<=Te;_++)
	{
		printf("Case #%d:",_);
		read(n);read(K);
		for(int i=1;i<=n;i++) read(p[i].fi),read(p[i].se);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++) read(g[i][j]);
		for(int k=1;k<=n;k++)
			for(int i=1;i<=n;i++)
				if (g[i][k]!=-1)
					for(int j=1;j<=n;j++)
						if (g[k][j]!=-1&&(g[i][j]==-1||g[i][j]>g[i][k]+g[k][j])) g[i][j]=g[i][k]+g[k][j];
		for(int i=1;i<=K;i++)
		{
			read(x);read(y);
			printf(" %.7lf",spfa(x,y));
		}
		printf("\n");
	}
}


