#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <functional>
#include <utility>
#include <set>
#include <map>
#include <complex>
#include <queue>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string.h>
#include <unordered_set>
#include <unordered_map>
#include <mmintrin.h>
#include <xmmintrin.h>
#include <emmintrin.h>
#include <cassert>

using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned short ushort;
typedef unsigned char uchar;
typedef pair<int, int> ipair;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
#define SIZE(A) ((int)(A.size()))
#define LENGTH(A) ((int)(A.length()))
#define MP(A, B) make_pair(A,B)
const double pi = acos(-1.0);
#define FOR(i, a, b) for(int i=(a);i<(b);++i)
#define REP(i, a) for(int i=0;i<(a);++i)
#define ALL(a) (a).begin(),(a).end()

template<class T>
T sqr(const T& x) { return x * x; }

template<class T>
T lowbit(const T& x) { return (x ^ (x - 1)) & x; }

template<class T>
int countbit(const T& n) { return (n == 0) ? 0 : (1 + countbit(n & (n - 1))); }

template<class T>
void ckmin(T& a, const T& b) { if (b < a) a = b; }

template<class T>
void ckmax(T& a, const T& b) { if (b > a) a = b; }

const int maxn=1000000+5;
const int maxm=1000000+5;
const int oo=1000000000;

int node,nedge,src,dest;
int head[maxn],point[maxm],nextp[maxm],flow[maxm],capa[maxm],cost[maxm];
int dist[maxn],expand[maxn],prevp[maxn],edge[maxn];
bool changed[maxn];

void init(int _node,int _src,int _dest)
{
	node=_node;
	src=_src;
	dest=_dest;
	nedge=0;
	for (int i=0;i<node;i++) head[i]=-1;
}
void addedge(int u,int v,int c,int w)
{
	//printf("%d %d %d %d\n",u,v,c,w);
	point[nedge]=v,capa[nedge]=c,cost[nedge]=+w,flow[nedge]=0,nextp[nedge]=head[u],head[u]=(nedge++);
	point[nedge]=u,capa[nedge]=0,cost[nedge]=-w,flow[nedge]=0,nextp[nedge]=head[v],head[v]=(nedge++);
}
void ford(int &mflow,int &mcost)
{
	mflow=mcost=0;
	while (1)
	{
		for (int i=0;i<node;i++) dist[i]=oo,prevp[i]=-1,changed[i]=false;
		dist[src]=0;
		changed[src]=true;
		expand[src]=oo;
		while (1)
		{
			bool ok=true;
			for (int i=0;i<node;i++) if (changed[i])
			{
				changed[i]=false;
				for (int k=head[i];k>=0;k=nextp[k])
					if (flow[k]<capa[k] && dist[i]+cost[k]<dist[point[k]])
					{
						dist[point[k]]=dist[i]+cost[k];
						changed[point[k]]=true;
						prevp[point[k]]=i;
						edge[point[k]]=k;
						expand[point[k]]=min(expand[i],capa[k]-flow[k]);
						ok=false;
					}
			}
			if (ok) break;
		}
		if (prevp[dest]<0) break;
		int d=expand[dest];
		mflow+=d;
		mcost+=d*dist[dest];
		for (int k=dest;k!=src;k=prevp[k])
		{
			//printf("%d ",k);
			flow[edge[k]]+=d;
			flow[edge[k]^1]-=d;
		}
		//printf("\n");
	}
}

const int maxsize=2048;

int length;
int n;
int ntickets;
int p[maxn],b[maxn];
int deg[maxn];

int solve(int width)
{
	init(length*2+ntickets+2,length*2+ntickets,length*2+ntickets+1);
	REP(i,ntickets) addedge(src,i,1,0);
	REP(i,ntickets) addedge(i,ntickets+p[i],1,0);
	REP(i,length) addedge(ntickets+i,dest,width,0);
	REP(i,length) addedge(ntickets+i,ntickets+length+i,100000000,1);
	FOR(i,1,length) addedge(ntickets+length+i,ntickets+i-1,100000000,0);
	FOR(i,1,length) addedge(ntickets+length+i,ntickets+length+i-1,100000000,0);
	int flow,cost;
	ford(flow,cost);
	if (flow!=ntickets) return -1;
	return cost;
}
ipair solve()
{
	int r1=0;
	REP(i,n) ckmax(r1,deg[i]);
	for (;;r1++)
	{
		int r2=solve(r1);
		if (r2>=0) return MP(r1,r2);
	}
}
int main()
{
  //freopen("B.in","r",stdin);
  //freopen("B-small-attempt0.in","r",stdin); freopen("B-small-attempt0.out","w",stdout);
  //freopen("B-small-attempt1.in","r",stdin); freopen("B-small-attempt1.out","w",stdout);
  //freopen("B-small-attempt2.in","r",stdin); freopen("B-small-attempt2.out","w",stdout);
  freopen("B-large.in","r",stdin); freopen("B-large.out","w",stdout);

  // std::ios_base::sync_with_stdio(false);
  int ntestcase;
  cin >> ntestcase;
  for (int case_id = 1; case_id <= ntestcase; ++case_id) {
	cin>>length>>n>>ntickets;
	memset(deg,0,sizeof(deg));
	REP(i,ntickets)
	{
		cin>>p[i]>>b[i];
		--p[i];
		--b[i];
		++deg[b[i]];
	}
	ipair r=solve();
    printf("Case #%d: %d %d\n", case_id,r.first,r.second);
	fflush(stdout);
  }

  return 0;
}