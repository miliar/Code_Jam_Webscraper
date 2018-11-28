#include <bits/stdc++.h>

#define rep(i,n) for(i=1;i<=n;i++)
#define Rep(i,n) for(i=0;i<n;i++)
#define For(i,a,b) for(i=a;i<=b;i++)

#define pb(x) push_back(x)
#define sz(x) x.size()

#define mem(ara,val) memset(ara,val,sizeof(ara))
#define eps 1e-7

#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define siii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define slll(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)
#define ss(ch) scanf("%s",ch)
#define pi(x) printf("%d",x)
#define pii(x,y) printf("%d %d",x,y)
#define piii(x,y,z) printf("%d %d %d",x,y,z)
#define pl(x) printf("%lld",x)
#define pll(x,y) printf("%lld %lld",x,y)
#define plll(x,y,z) printf("%lld %lld %lld",x,y,z)
#define ps(ch) printf("%s",ch)
#define Afridi 0
#define NL printf("\n")
#define debug(x) printf("wow  %d !!\n",x)
#define Max 100005
#define INF (LL)1e15
#define mod 100003
#define FI freopen("in.txt","r",stdin)
#define FO freopen("out.txt","w",stdout)
#define D(x) cout << #x << " = " << x << endl
#define DD(x,y) cout << #x << " = " << x << "   " << #y << " = " << y << endl
#define RTE __builtin_trap()
#define FI(str) freopen(str,"r",stdin)
#define FO(str) freopen(str,"w",stdout)

const double PI = acos( -1.0 );

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

LL bigmod(LL b,LL p)
{
    if(p == 0)return 1;
    LL my = bigmod(b,p/2);
    my*=my;
    my%=mod;
    if(p & 1)my*=b,my%=mod;
    return my;
}

	//freopen("","r",stdin);
	//freopen("","w",stdout);

int setb(int n,int pos){return n=n | (1 << pos);}
int resb(int n,int pos){return n=n & ~(1 << pos);}
bool checkb(int n,int pos){return (bool)(n & (1 << pos)); }

LL n,q,ara[105][2],d[105][105];
long double sand[105][105];
bool poss[105][105];

struct info
{
	LL u,w;
	info() {}
	info(LL _u,LL _w) { u = _u; w = _w; }
	bool operator < ( const info &p ) const
	{
		return w > p.w;
	}
};
priority_queue <info> pq;

void dijkstra(LL s)
{
    LL i,dis[105];
    rep(i,n)dis[i] = INF;
    dis[s] = 0;
    while( pq.empty() == 0 )pq.pop();
    pq.push( info(s,0) );
    while( pq.empty() == 0 )
    {
		info my = pq.top();
		pq.pop();

		LL u = my.u;
		LL w = my.w;
		rep(i,n)
		{
			LL v = i;
			if( d[u][v] == -1 )continue;
			if( w + d[u][v] < dis[v] )
			{
				dis[v] = w + d[u][v];
				pq.push( info(v,dis[v]) );
			}
		}
    }
    rep(i,n)
    {
		if( i == s )
		{
			poss[s][s] = 0;
			continue;
		}
		if(dis[i] == INF)
		{
			poss[s][i] = 0;
		}
		else
		{
			if( ara[s][0] < dis[i] )
			{
				poss[s][i] = 0;
			}
			else
			{
				poss[s][i] = 1;
				sand[s][i] = (long double)dis[i] / (long double)ara[s][1];
			}
		}
    }
}

vector <LL> g[105];
vector <long double> cost[105];
void build_graph()
{
	LL i,u,v;
	rep(i,n)g[i].clear(),cost[i].clear();
	rep(u,n)
	{
		rep(v,n)
		{
			if( poss[u][v] )
			{
				g[u].pb(v);
				cost[u].pb( sand[u][v] );
			}
		}
	}
}

struct node
{
	LL u;
	long double w;
	node() {}
	node(LL _u,long double _w) { u = _u; w = _w; }
	bool operator < ( const node &p ) const
	{
		return w > p.w;
	}
};
priority_queue <node> pqq;

double F(LL source,LL dest)
{
    while( pqq.empty() == 0 )pqq.pop();
    long double dis[105];
    LL i;
    rep(i,n)dis[i] = 1e15;
    dis[source] = 0.0;
    pqq.push( node(source,dis[source]) );
    while( pqq.empty() == 0 )
    {
		node my = pqq.top();
		pqq.pop();
		LL u = my.u;
		long double w = my.w;
		LL len = sz(g[u]);
		Rep(i,len)
		{
			LL v = g[u][i];
			if( w + cost[u][i] < dis[v] )
			{
                dis[v] = w + cost[u][i];
                pqq.push( node(v,dis[v]) );
			}
		}
    }
	return dis[dest];
}

long double dp[105];
LL visit[105],cs;
long double F(LL u)
{
	if(u == n)return 0.0;

	if( visit[u] == cs )return dp[u];

	LL i;
	long double ret = 1e15;
	rep(i,n)
	{
		if( poss[u][i] )
		{
			ret = min( ret, sand[u][i] + F(i) );
		}
	}


	visit[u] = cs;
	return dp[u] = ret;
}

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("cbal.txt","w",stdout);

	LL t,T,i,j,st,ed;
	sl(T);
	rep(t,T)
	{
		sll(n,q);
		rep(i,n)
		{
			sll(ara[i][0],ara[i][1]);
		}
		rep(i,n)
		{
			rep(j,n)
			{
				sl(d[i][j]);
			}
		}
		rep(i,n)dijkstra(i);
		build_graph();
		printf("Case #%lld:",t);
		rep(i,q)
		{
			sll(st,ed);
			//cs++;
			//double ret = (double)F(st);
			double again = (double)F(st,ed);
			//assert( fabs(ret-again) < eps );
			//printf("Case #%lld: %.10f\n",t,ret);
			printf(" %.10f",again);
		}
		NL;
	}
	return 0;
}
