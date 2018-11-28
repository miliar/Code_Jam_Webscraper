#include<bits/stdc++.h>

using namespace std;

// Shortcuts for "common" data types in contests
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define s(i) scanf("%d",&i)
#define sl(i) scanf("%ld",&i)
#define sll(i) scanf("%lld",&i)
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000 // 2 billion

const int maxnodes = 100009;

int nodes = maxnodes, src, dest;
int dist[maxnodes],work[maxnodes];

struct Edge {
  int to, rev;
  int f, cap;
};

vector <Edge> g[maxnodes];

// Adds bidirectional edge
void addEdge(int s, int t, int cap ,int revcap){
  Edge a = {t, g[t].size(), 0, cap};
  Edge b = {s, g[s].size(), 0, revcap};
  g[s].push_back(a);
  g[t].push_back(b);
}

bool dinic_bfs() {
  fill(dist, dist + nodes, -1);
  dist[src] = 0;
  queue <int> qu;qu.push(src);
  while( !qu.empty() )
  {
      int u = qu.front();qu.pop();
      for(int j = 0;j < g[u].size() ;j++)
      {
          Edge &e = g[u][j];
          int v = e.to;
          if(dist[v] == -1 && e.f < e.cap)
          {
              dist[v] = dist[u] + 1;
              qu.push(v);
          }
      }
  }
  return dist[dest] >= 0;
}

int dinic_dfs(int u, int f) {
  if (u == dest)
    return f;
  for (int &i = work[u]; i < (int) g[u].size(); i++) {
    Edge &e = g[u][i];
    if (e.cap <= e.f) continue;
    int v = e.to;
    if (dist[v] == dist[u] + 1) {
      int df = dinic_dfs(v, min(f, e.cap - e.f));
      if (df > 0) {
        e.f += df;
        g[v][e.rev].f -= df;
        return df;
      }
    }
  }
  return 0;
}

int maxFlow(int _src, int _dest) {
  src = _src;
  dest = _dest;
  int result = 0;
  while (dinic_bfs()) {
    fill(work, work + nodes, 0);
    while (int delta = dinic_dfs(src, INF))
      result += delta;
  }
  return result;
}

int ingrediants[59] , packages[59][59];

bool check( int ingrediant1 , int ingrediant2 ) {
  REP( s , 1 , 2000000 ){
    ll percent1 = (ingrediant1 * 100) / ( s * 1ll * ingrediants[0] ) ;
    ll percent2 = (ingrediant2 * 100) / ( s * 1ll * ingrediants[1] ) ;
    if( percent1 > 110 || ( percent1 == 110 && ( (( ingrediant1 * 100 ) % ( s * 1ll * ingrediants[0]) ) != 0 ) ) ){
      continue;
    }
    if( percent2 > 110 || ( percent2 == 110 && ( ( ( ingrediant2 * 100 ) % ( s * 1ll * ingrediants[1]) ) != 0 ) ) ){
      continue;
    }
    if( percent1 >= 90 && percent2 >= 90 )
      return true;
  }
  return false;
}

bool check(int ingrediant1){
  REP( s , 1 , 2000000 ){
        ll percent1 = (ingrediant1 * 100) / ( s * 1ll * ingrediants[0] ) ;
        if( percent1 > 110 || ( percent1 == 110 && ( (( ingrediant1 * 100 ) % ( s * 1ll * ingrediants[0]) ) != 0 ) ) )
          continue;
        if( percent1 >= 90 )
          return true;
  }
  return false;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    s(t);
    REP( T , 1 , t ){
      REP( i , 0 , 1000 ){
        g[i].clear();
      }
      int n , p ; 
      s(n) ; s(p) ; 
      REP( i , 0 , n - 1 ){
          s(ingrediants[i]);
      }
      REP( i , 0 , n - 1 ){
          REP( j , 0  , p - 1 ){
              s(packages[i][j]);
          }
      }
      if( n == 1 ){
        int ans = 0 ;
          REP( i , 0 , p - 1 ){
            if( check(packages[0][i]) )
              ans++;
          }
          printf("Case #%d: %d\n",T,ans);
          continue;
      }
      REP( i , 1 , p ){
        addEdge( 0 , i , 1 , 0 );
        addEdge( p + i , 2 * p + 1 , 1 , 0 ) ; 
      }
      REP( i , 0 , p - 1) {
        REP( j , 0 , p - 1 ){
            if( check( packages[0][i] , packages[1][j] ) ){
                addEdge(i + 1, j + 1 + p,1000,0);
            }
        }
      }
      printf("Case #%d: %d\n",T,maxFlow(0 , 2 * p + 1));
    } 
    return 0;
}
