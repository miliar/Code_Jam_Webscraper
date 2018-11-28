//BISMILLAHIR RAHMANIR RAHIM
//LIGHTOJ 1262
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<queue>
#include<set>
#include <iostream>
#include<stack>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#define N 1000000
#define sn scanf
#define pf printf
#define pb push_back

typedef long long int ll;
using namespace std;
struct T{
int a;
};
int trac[3][405][405];
const int MAXN = 2000;
const int INF = 1000000000;
struct dinic_maxflow{


struct edge {
	int a, b, cap, flow;
	edge(int _a,int _b,int _cap,int _flow)
	{
	    a=_a,b=_b,cap=_cap,flow=_flow;
	}
};

int n, s, t, d[MAXN], ptr[MAXN], q[MAXN];
vector<edge> e;
vector<int> g[MAXN];
//int trac[205][405];
void add_edge (int a, int b, int cap,int idd) {
	edge e1 = edge( a, b, cap, 0 );
	edge e2 = edge( b, a, 0, 0 );
	g[a].push_back ((int) e.size());
	trac[idd][a][b]=e.size();
	e.push_back (e1);
	g[b].push_back ((int) e.size());
	e.push_back (e2);
}

bool bfs() {
	int qh=0, qt=0;
	q[qt++] = s;
	memset (d, -1, n * sizeof d[0]);
	d[s] = 0;
	while (qh < qt && d[t] == -1) {
		int v = q[qh++];
		for (size_t i=0; i<g[v].size(); ++i) {
			int id = g[v][i],
				to = e[id].b;
			if (d[to] == -1 && e[id].flow < e[id].cap) {
				q[qt++] = to;
				d[to] = d[v] + 1;
			}
		}
	}
	return d[t] != -1;
}

int dfs (int v, int flow) {
	if (!flow)  return 0;
	if (v == t)  return flow;
	for (; ptr[v]<(int)g[v].size(); ++ptr[v]) {
		int id = g[v][ptr[v]],
			to = e[id].b;
		if (d[to] != d[v] + 1)  continue;
		int pushed = dfs (to, min (flow, e[id].cap - e[id].flow));
		if (pushed) {
			e[id].flow += pushed;
			e[id^1].flow -= pushed;
			return pushed;
		}
	}
	return 0;
}

int dinic( ) {
	int flow = 0;
	for (;;) {
		if (!bfs())  break;
		memset (ptr, 0, n * sizeof ptr[0]);
		while (int pushed = dfs (s, INF))
			flow += pushed;
	}
	return flow;
}
    dinic_maxflow( int _n, int _s, int _t ){
        n = _n; s = _s; t = _t;
       // memset(trac,-1,sizeof(trac));
    }
};
int inp[105][105],vis[3][1006],ar[105][105];
char mm[4];
int main()
{
    int i,j,k,l,t,cs=1,r=1,s,m,n,a,b,c,d,e,f,g,h,u,v;
    //freopen("D.in","r",stdin);
    //freopen("out.txt","w",stdout);
    sn("%d",&t);
    while(t--)
    {
        sn("%d %d",&n,&m);
        memset(inp,-1,sizeof(inp));
        memset(ar,-1,sizeof(ar));
        for(i=0;i<m;i++)
        {
            sn("%s %d %d",&mm,&u,&v);
            if(mm[0]=='+')
            inp[u][v]=1;
            if(mm[0]=='x')
            inp[u][v]=2;
            if(mm[0]=='o')
            inp[u][v]=3;
            ar[u][v]=inp[u][v];
        }

        dinic_maxflow dm1=dinic_maxflow(4*n+5,0,4*n+1);
        dinic_maxflow dm2=dinic_maxflow(2*n+5,0,2*n+1);
        memset(vis,0,sizeof(vis));
        memset(trac,-1,sizeof(trac));
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                a=i+j;
                b=2*n+n+i-j;
                dm1.add_edge(a,b,1,0);
                dm2.add_edge(i,n+j,1,1);
                if(inp[i][j]==1)
                {
                    a=i+j;
                    b=2*n+n+i-j;
                    vis[0][a]=1;
                    vis[0][b]=1;
                }
                else if(inp[i][j]==2)
                {
                    vis[1][i]=1;
                    vis[1][n+j]=1;
                }
                else if(inp[i][j]==3)
                {
                    a=i+j;
                    b=2*n+n+i-j;
                    vis[0][a]=1;
                    vis[0][b]=1;
                    vis[1][i]=1;
                    vis[1][n+j]=1;
                }
            }
        }

        for(i=1;i<=4*n;i++)
        {
            if(vis[0][i]==0)
            {
                if(i<=2*n)
                {
                    dm1.add_edge(0,i,1,0);
                }
                else
                {
                    dm1.add_edge(i,4*n+1,1,0);
                }
            }
        }
        for(i=1;i<=n+n;i++)
        {
            if(vis[1][i]==0)
            {
                if(i<=n)
                dm2.add_edge(0,i,1,1);
                else
                dm2.add_edge(i,2*n+1,1,1);
            }
        }
        int ans=0;
        h=dm1.dinic();
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                a=i+j;
                b=2*n+n+i-j;
                if(trac[0][a][b]>=0&&dm1.e[trac[0][a][b]].flow>0)
                {
                    if(ar[i][j]==-1)
                        ar[i][j]=1;
                    else if(ar[i][j]==2)
                    {
                        ar[i][j]=3;
                    }
                    else if(ar[i][j]==3)
                    {
                        ar[i][j]=3;
                    }
                }
            }
        }

        //pf("%d\n",h);

        h=h+dm2.dinic();
       // pf("---%d\n",h);

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                a=i;
                b=n+j;
                if(trac[1][a][b]>=0&&dm2.e[trac[1][a][b]].flow>0)
                {
                    if(ar[i][j]==-1)
                        ar[i][j]=2;
                    else if(ar[i][j]==1)
                        ar[i][j]=3;
                    else if(ar[i][j]==3)
                    ar[i][j]=3;
                }
            }
        }
        vector<int>anx,any,anz;
        int change=0;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(ar[i][j]!=inp[i][j])
                {
                    anx.pb(i);
                    any.pb(j);
                    anz.pb(ar[i][j]);
                    change++;
                }
                if(ar[i][j]==1)
                    ans++;
                else if(ar[i][j]==2)
                    ans++;
                else if(ar[i][j]==3) ans+=2;
            }
        }
        pf("Case #%d: %d %d\n",cs++,ans,change);
        for(i=0;i<anx.size();i++)
        {
            if(anz[i]==1)
                pf("+");
            else if(anz[i]==2)
                pf("x");
            else
                pf("o");
            pf(" %d %d\n",anx[i],any[i]);
        }
    }
    return 0;

}

/*
#include <bits/stdc++.h>
  #define _ ios_base::sync_with_stdio(0);cin.tie(0);
*/

