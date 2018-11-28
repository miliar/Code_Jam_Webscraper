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
const int MAXN = 5000;
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

void add_edge (int a, int b, int cap) {
	edge e1 = edge( a, b, cap, 0 );
	edge e2 = edge( b, a, 0, 0 );
	g[a].push_back ((int) e.size());
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
    }
};

int seat[1005],cus[1005],X[1005],Y[1005];

int solve(int n,int m,int k,int cap)
{
    int i,s,d;
    dinic_maxflow dm=dinic_maxflow(n+m+10,0,n+m+5);
             s=0;d=n+m+5;
             for(i=1;i<=n;i++)
             {
                 dm.add_edge(i,d,cap);
             }
             for(i=2;i<=n;i++)
             {
                 dm.add_edge(i,i-1,INF);
             }
             //customer
             for(i=0;i<k;i++)
             {
                int  u=X[i];//seat no.
                 int v=Y[i];
                 dm.add_edge(v+n,u,1);
             }
             for(i=1;i<=m;i++)
             {
                 dm.add_edge(s,i+n,INF);
             }
        return dm.dinic();
}

int main()
{
    int i,j,k,l,t,cs=1,r=1,s,m,n,a,b,c,d,e,f,g,h,u,v;

     sn("%d",&t);
     while(t--)
     {
         sn("%d %d %d",&n,&m,&k);
         memset(seat,0,sizeof(seat));
         memset(cus,0,sizeof(cus));
         int mx=0;
         for(i=0;i<k;i++)
         {
             sn("%d %d",&X[i],&Y[i]);
             cus[Y[i]]++;
             seat[X[i]]++;
             mx=max(cus[Y[i]],mx);
         }
         int lw=mx,hi=k,mid;
         while(lw<=hi)
         {
             mid=(lw+hi)/2;
             int cap=mid;
             if(solve(n,m,k,cap)==k)
             {
                 if(mid-1>=mx&&solve(n,m,k,mid-1)==k)
                 {
                     hi=mid-1;
                 }
                 else
                    break;
             }
             else
             {
                 lw=mid+1;
             }
         }
         int pro=0;
         for(i=1;i<=n;i++)
         {
             if(seat[i]>mid)
             {
                 pro=pro+seat[i]-mid;
             }
         }
         pf("Case #%d: %d %d\n",cs++,mid,pro);
     }
    return 0;

}

/*
#include <bits/stdc++.h>
  #define _ ios_base::sync_with_stdio(0);cin.tie(0);
*/

