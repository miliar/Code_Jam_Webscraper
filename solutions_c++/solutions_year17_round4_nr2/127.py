#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 100005


#define MAXFN 2005	// maximum number of nodes in the flow graph
#define MAXM (2005*2005)	// maximum number of edges in the graph
int FN, S, T; // set S,T,FN manually before run!
int L, adj[MAXFN];
int dst[MAXFN], gap[MAXFN];
struct llist{
  int id,next,c,f;
  llist(){}
  llist(int _id,int _c,int _next) {id=_id;c=_c;f=0;next=_next;}
} lists[2*MAXM];
inline void insertList(int &a, int b, int c){
  lists[L] = llist(b,c,adj[a]);
  adj[a] = L++;
}
inline void insertEdge(int a, int b, int c){
  //cerr << a << " " << b << " " << c << endl;
  insertList(a,b,c);
  insertList(b,a,0);
}
void bfs(){
  REP(i,0,FN) dst[i] = FN;
  dst[T] = 0; // bfs from T
  FILL(gap, 0);
  gap[0] = FN;	// FN nodes with gap 0
  queue<int> que; que.push(T);
  while(!que.empty()){
    int x = que.front(); que.pop();
    int t = adj[x];
    while(t!=-1){
      if(t&1){ // back edge
        int y = lists[t].id;
        if(dst[y]==FN){
          dst[y] = dst[x]+1;
          gap[dst[y]]++;
          que.push(y);
        }
      }
      t = lists[t].next;
    }
  }
}
int sendflow(int x, int inflow){
  if(x==T) return inflow;
  int outflow = inflow, delta = 0, minh = FN-1;
  int t = adj[x];
  while(t!=-1){
    int y = lists[t].id;
    if(lists[t].c != lists[t].f){
      if(dst[x]==dst[y]+1){
        delta = sendflow(y, min(outflow, lists[t].c-lists[t].f));
        lists[t].f += delta;
        lists[t^1].f -= delta;
        outflow -= delta;
        if(dst[S]==FN) return inflow-outflow; // no more flow, cannot advance
        if(outflow==0) break;
      }
      minh = min(minh, dst[y]);
    }
    t = lists[t].next;
  }
  if(inflow==outflow){ // no exit flow possible, relabel
    gap[dst[x]]--;
    if(gap[dst[x]]==0) dst[S] = FN; // exit immediately
    dst[x] = minh + 1;
    gap[dst[x]]++;
  }
  return inflow-outflow;
}
int sap(){ // initialize f=0 if rerun
  int maxflow = 0;
  bfs();
  while(dst[S]<FN) maxflow += sendflow(S, INF);
  return maxflow;
}

int cnt[3][1005];
int main() {
  freopen("input", "r", stdin);
  //freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    //cerr << csn << endl;
    int N, M, C;
    cin >> N >> C >> M;
    S = 0; T = 2*N + 1; FN = T + 1;
    L = 0; FILL(adj, -1);
    FILL(cnt, 0);
    REP(i,0,M) {
      int p,c;
      scanf("%d%d", &p, &c);
      cnt[c][p]++;
    }
    REP(p,1,N+1) {
      if (cnt[1][p]) insertEdge(S, p, cnt[1][p]);
      if (cnt[2][p]) insertEdge(p+N, T, cnt[2][p]);
      REP(q,1,N+1) {
        if (p != q) insertEdge(p, q+N, INF);
      }
    }
    int prs = sap();
    int ans = prs, promo = 0;
    int t = adj[S];
    int r1=-1, c1=0, r2=-1, c2=0;
    while(t!=-1){
      if(!(t&1)){ // fw
        int y = lists[t].id;
        int rem = lists[t].c - lists[t].f;
        if (rem > 0) {
          r1 = y;
          c1 = rem;
        }
      }
      t = lists[t].next;
    }
    REP(x,N+1,N+N+1) {
      int t = adj[x];
      while(t!=-1){
        if(!(t&1)){ // fw
          int y = lists[t].id;
          int rem = lists[t].c - lists[t].f;
          if (y == T && rem > 0) {
            r2 = x - N;
            c2 = rem;
          }
        }
        t = lists[t].next;
      }
    }
    if (c1 && c2) {
      assert(r1 == r2);
      if (r1 == 1) {
        ans += c1 + c2;
      } else {
        ans += max(c1, c2);
        promo = min(c1, c2);
      }
    } else if (c1 || c2) {
      ans += M - prs * 2;
    }
    cout << ans << " " << promo << endl;
  }
  return 0;
}
