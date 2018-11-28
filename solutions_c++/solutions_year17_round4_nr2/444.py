#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	mp make_pair
#define	pb push_back
#define sz(a) int((a).size())
#define all(a)  a.begin(), a.end()
#define	debug(ccc)	cout << #ccc << " = " << ccc << endl;
#define present(c,x) ((c).find(x) != (c).end())
const double eps = 1e-8;
#define EQ(a,b) (fabs((a)-(b))<eps)
inline int max(int a,int b){return a<b?b:a;}
inline int min(int a,int b){return a>b?b:a;}
inline ll max(ll a,ll b){return a<b?b:a;}
inline ll min(ll a,ll b){return a>b?b:a;}
const int mod = 1e9+7;
const int N = 1e6+10;
const ll INF = mod;

ll power(ll a,ll n){
	if(n==0){
		return 1;
	}
	ll b = power(a,n/2);
	b = b*b%mod;
	if(n%2) b= b*a%mod;
	return b;
}

int add(int a,int b){ return (a+b)%mod;}
int mul(int a,int b){ return (ll)a*b%mod;}



vector < int > G[1010],A[1010];
vector <pii> R;
 typedef int Index; typedef int Flow; typedef int Cost;
const Flow InfCapacity = INF; const Cost InfCost = INF;

struct MinimumCostMaximumFlow {
  struct Edge {
    Index to; Index rev;
    Flow capacity; Cost cost;
  };
  vector<vector<Edge> > g;
  void init(Index n) { g.assign(n, vector<Edge>()); }
  // add directed edge
  void add(Index i, Index j, Flow capacity = InfCapacity, Cost cost = Cost()) {
    Edge e, f; e.to = j, f.to = i; e.capacity = capacity, f.capacity = 0; e.cost = cost, f.cost = -cost;
    g[i].push_back(e); g[j].push_back(f);
    g[i].back().rev = (Index)g[j].size() - 1; g[j].back().rev = (Index)g[i].size() - 1;
  }
  // add Bidirectional Edge
  void addB(Index i, Index j, Flow capacity = InfCapacity, Cost cost = Cost()) {
    add(i, j, capacity, cost);
    add(j, i, capacity, cost);
  }
  pair<Cost,Flow> minimumCostMaximumFlow(Index s, Index t, Flow f = InfCapacity, bool useSPFA = false) {
    int n = g.size();
    vector<Cost> dist(n); vector<Index> prev(n); vector<Index> prevEdge(n);
    pair<Cost,Flow> total = make_pair(0, 0);
    vector<Cost> potential(n);
    while(f > 0) {
      fill(dist.begin(), dist.end(), InfCost);
      if(useSPFA ) {
        deque<Index> q;
        q.push_back(s); dist[s] = 0; vector<bool> inqueue(n);
        while(!q.empty()) {
          Index i = q.front(); q.pop_front(); inqueue[i] = false;
          for(Index ei = 0; ei < g[i].size(); ei ++) {
            const Edge &e = g[i][ei]; Index j = e.to; Cost d = dist[i] + e.cost;
            if(e.capacity > 0 && d < dist[j]) {
              if(!inqueue[j]) {
                inqueue[j] = true;
                q.push_back(j);
              }
              dist[j] = d; prev[j] = i; prevEdge[j] = ei;
            }
          }
        }
      }else {
        vector<bool> vis(n);
        priority_queue<pair<Cost,Index> > q;
        q.push(make_pair(-0, s)); dist[s] = 0;
        while(!q.empty()) {
          Index i = q.top().second; q.pop();
          if(vis[i]) continue;
          vis[i] = true;
          for(Index ei = 0; ei < (Index)g[i].size(); ei ++) {
            const Edge &e = g[i][ei];
            if(e.capacity <= 0) continue;
            Index j = e.to; Cost d = dist[i] + e.cost + potential[i] - potential[j];
            if(dist[j] > d) {
              dist[j] = d; prev[j] = i; prevEdge[j] = ei;
              q.push(make_pair(-d, j));
            }
          }
        }
      }
      if(dist[t] == InfCost) break;
      if(!useSPFA) for(Index i = 0; i < n; i ++) potential[i] += dist[i];
       
      Flow d = f; Cost distt = 0;
      for(Index v = t; v != s; ) {
        Index u = prev[v]; const Edge &e = g[u][prevEdge[v]];
        d = min(d, e.capacity); distt += e.cost; v = u;
      }
      f -= d; total.first += d * distt; total.second += d;
      for(Index v = t; v != s; v = prev[v]) {
        Edge &e = g[prev[v]][prevEdge[v]];
        e.capacity -= d; g[e.to][e.rev].capacity += d;
      }
    }
    return total;
  }
};

int main(){
 // 	freopen("nice.in","r",stdin);
 // freopen("nice.out","w",stdout);
	int t; scanf("%d",&t);
	REP(tt,t){
		int n,c,m;
		scanf("%d %d %d",&n,&c,&m);
		REP(i,m){
			int b,p; scanf("%d %d",&p,&b); b--,p--;
			R.pb(mp(b,p));
			G[p].pb(b); A[b].pb(p);
		}
		int dy=0,sum=0;
		REP(i,1010){
			dy = max(dy,A[i].size());
			sum += G[i].size();
			dy = max(dy, (sum+i)/(i+1));
		}
		// printf("%d\n",dy);
		MinimumCostMaximumFlow *mc = new MinimumCostMaximumFlow();
		mc->init(m+3*n+2);
		int src = m+3*n, dst = src+1;
		REP(i,m){
			mc->add(i,m+R[i].Y,1,1);
			mc->add(i,m+n+R[i].Y,1,0);
			mc->add(src,i,1,0);
		}
		REPP(i,1,n) mc->add(m+i,m+i-1,mod,0);
		REP(i,n){
			mc->add(i+m,m+2*n+i,mod,0);
			mc->add(i+m+n,m+2*n+i,mod,0);
			mc->add(m+2*n+i,dst,dy,0);
		}
		pii a = mc->minimumCostMaximumFlow(src,dst);
		assert(a.Y==m);
		printf("Case #%d: %d %d\n",tt+1,dy,a.X);
		REP(i,1010) G[i].clear(),A[i].clear();
		R.clear();
	}
	return 0;
}


