#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<ctime>
#include<climits>
#include<complex>
#include<cassert>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(x) (int)((x).size())
#define all(x) x.begin(),x.end()
#define clr(x) memset((x),0,sizeof(x))
#define cdp(x) memset((x),-1,sizeof(x))
#define rep(i,n) for (i=0;i<n;i++)
#define Rep(i,a,b) for (i=a;i<=b;i++)
#define ff(i,x) for (i=start[x];i!=-1;i=a[i].next)
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
using namespace std;
const double eps=1e-8;
const double pi=acos(-1.0);
int dblcmp(double d){if (fabs(d)<eps)return 0;return d>eps?1:-1;}
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
struct node 
{
	int u;
	double t;
	node(){}
	node(int vv,double tt)
	{
		u=vv;
		t=tt;
	}
	bool operator<(const node&gg)const 
	{
		return t>gg.t;
	}
};
int e[1111],s[1111];
ll g[333][333];
int main()
{
	freopen("C:\\competition\\gcj\\C-large (3).in","r",stdin);
	freopen("C:\\competition\\gcj\\Cout.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		int n,q;
		scanf("%d%d",&n,&q);
		for (i=1;i<=n;i++)scanf("%d%d",&e[i],&s[i]);
		for (i=1;i<=n;i++)
		{
			for (j=1;j<=n;j++)
			{
				scanf("%d",&k);
				g[i][j]=k;
			}
		}
		for (k=1;k<=n;k++)
		{
			for (i=1;i<=n;i++)if (g[i][k]!=-1)
			{
				for (j=1;j<=n;j++)if (g[k][j]!=-1)
				{
					if (g[i][j]==-1||g[i][j]>g[i][k]+g[k][j])
					{
						g[i][j]=g[i][k]+g[k][j];
					}
				}
			}
		}
		//printf("%d %d\n",g[1][3],g[2][3]);
		printf("Case #%d:",++cc);
		while (q--)
		{
			int u,v;
			scanf("%d%d",&u,&v);
			priority_queue<node>pq;
			pq.push(node(u,0));
			bool vis[111];
			double dis[111];
			for (i=0;i<111;i++)dis[i]=1e20;
			dis[u]=0;
			clr(vis);
			while (!pq.empty())
			{
				node t=pq.top();
				pq.pop();
				if (vis[t.u])continue;
				vis[t.u]=1;
				//printf("u %d %lf\n",t.u,dis[t.u]);
				for (i=1;i<=n;i++)if (!vis[i])
				{
					ll d=g[t.u][i];
					if (d!=-1&&d<=e[t.u])
					{
						//if (t.u==1)printf("nxt %d\n",i);
						if (dis[i]>dis[t.u]+d*1.0/s[t.u])
						{
							dis[i]=dis[t.u]+d*1.0/s[t.u];
							pq.push(node(i,dis[t.u]+d*1.0/s[t.u]));
						}
					}
				}
			}
			printf(" %.10lf",dis[v]);
		}
		puts("");
	}
	return 0;
}
