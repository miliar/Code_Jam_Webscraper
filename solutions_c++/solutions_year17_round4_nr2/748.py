#include <bits/stdc++.h>
using namespace std;

using VI = vector<int>;
using VVI = vector<VI>;
using PII = pair<int, int>;
using LL = long long;
using VL = vector<LL>;
using VVL = vector<VL>;
using PLL = pair<LL, LL>;
using VS = vector<string>;

#define ALL(a)  begin((a)),end((a))
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define EB emplace_back
#define MP make_pair
#define SZ(a) int((a).size())
#define SORT(c) sort(ALL((c)))
#define RSORT(c) sort(RALL((c)))
#define UNIQ(c) (c).erase(unique(ALL((c))), end((c)))

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define FF first
#define SS second
template<class S, class T>
istream& operator>>(istream& is, pair<S,T>& p){
  return is >> p.FF >> p.SS;
}
template<class S, class T>
ostream& operator<<(ostream& os, const pair<S,T>& p){
  return os << p.FF << " " << p.SS;
}
template<class T>
void maxi(T& x, T y){
  if(x < y) x = y;
}
template<class T>
void mini(T& x, T y){
  if(x > y) x = y;
}


const double EPS = 1e-10;
const double PI  = acos(-1.0);
const LL MOD = 1e9+7;
const int INF = 1e8;

struct Edge{
  int to, cap, cost, rev;
  Edge(int to_=0, int cap_ = 0, int cost_ = 0, int rev_ = 0)
	:to(to_), cap(cap_), cost(cost_), rev(rev_){}
};

int V;
const int MAX_V = 3000;
vector<Edge> G[MAX_V];
int dist[MAX_V];
int prevv[MAX_V], preve[MAX_V]; //直前の頂点と辺

void add_edge(int from, int to, int cap, int cost){
  G[from].push_back(Edge(to, cap, cost, G[to].size()));
  G[to].push_back(Edge(from, 0, -cost, G[from].size()-1));
}
int min_cost_flow(int s, int t, int f){
  int res = 0;
  while(f > 0){
	fill(dist, dist+V, INF);
	dist[s] = 0;
	bool update = true;
	while(update){
	  update = false;
	  for(int v=0;v<V;++v){
		if(dist[v] == INF) continue;
		for(int i=0;i<G[v].size();++i){
		  Edge& e = G[v][i];
		  if(e.cap > 0 && dist[v] + e.cost < dist[e.to]){
			dist[e.to] = dist[v] + e.cost;
			prevv[e.to] = v;
			preve[e.to] = i;
			update = true;
		  }
		}
	  }
	}

	if(dist[t] == INF) return -1;

	int d = f;
	for(int v=t;v!=s;v=prevv[v])
	  d = min(d, G[prevv[v]][preve[v]].cap);

	f -= d;
	res += d * dist[t];
	for(int v=t;v!=s;v=prevv[v]){
	  Edge& e = G[prevv[v]][preve[v]];
	  e.cap -= d;
	  G[v][e.rev].cap += d;
	}
  }
  
  return res;
}

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  FOR(t,1,T+1){
	int N, C, M;
	cin >> N >> C >> M;
	vector<PII> xs(M);
	VI xs1, xs2;
	REP(i,M){
	  cin >> xs[i];
	  xs[i].FF--;
	  xs[i].SS--;
	  if(xs[i].SS == 0){
		xs1.PB(xs[i].FF);
	  }
	  else{
		xs2.PB(xs[i].FF);
	  }
	}

	if(SZ(xs1) < SZ(xs2))
	  swap(xs1, xs2);
	if(SZ(xs2) == 0){
	  int ans1 = SZ(xs1), ans2 = SZ(xs2);
	  cout << "Case #" << t << ": " << ans1 << " " << ans2 << endl;
	  continue;
	}
	
	int ans1, ans2;
	int m = SZ(xs1);
	for(;;++m){
	  int S = m*2+1;
	  int T = S+1;
	  V = T+1;
	  REP(i,V) G[i].clear();
	  
	  REP(k,SZ(xs2)){
		add_edge(S, k, 1, 0);
		for(int i=0;i<SZ(xs1);++i){
		  if(xs2[k] != xs1[i]){
			add_edge(k, m+i, 1, 0);
		  }
		  if(xs2[k] >= 2 || (xs2[k] == 1 && (xs1[i] != 0)))
			add_edge(k, m+i, 1, 1);
		}
		for(int i=SZ(xs1);i<m;++i){
		  add_edge(k, m+i, 1, 0);
		}
	  }
	  REP(i,m)
		add_edge(m+i, T, 1, 0);
	  int c = min_cost_flow(S, T, SZ(xs2));
	  if(c >= 0){
		ans1 = m;
		ans2 = c;
		break;
	  }
	}

	cout << "Case #" << t << ": " << ans1 << " " << ans2 << endl;
  }

  return 0;
}
