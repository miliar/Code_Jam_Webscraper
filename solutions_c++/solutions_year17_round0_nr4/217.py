#include<bits/stdc++.h>
using namespace std;
#define FOR(i,n,...) for (int i = 1 , ##__VA_ARGS__ ; i <= n ; ++i)
#define REP(i,s,n,...) for (int i = s , ##__VA_ARGS__ ; i <= n ; ++i)
#define ll long long
#define LL long long

int meow[102][102] ;
int meow2[102][102] ;
bool qinding[1003] , visit[1003] ;
int pat[1003] ;
char c;

int edge[46666][2] , head[1003] , maxe = 1;
void add_edge (int u , int v) {
  edge[maxe][0] = u;
  edge[maxe][1] = head[v] ;
  head[v] = maxe++;
  edge[maxe][0] = v;
  edge[maxe][1] = head[u];
  head[u] = maxe++;
}

bool Gao (int p) {
  if (visit[p]) return false;
  visit[p] = true;
  for (int i = head[p] ; i ; i = edge[i][1]) {
    if (pat[edge[i][0]] == 0 || Gao(pat[edge[i][0]])) {
      pat[p] = edge[i][0];
      pat[edge[i][0]] = p;
      return true;
    }
  }
  return false;
}

int main (void) {
  int T ; cin >> T ; FOR(Cas,T) {
    printf("Case #%d: ",Cas);
    maxe = 1;
    memset(head,0,sizeof(head));
    memset(meow,0,sizeof(meow));
    memset(meow2,0,sizeof(meow));
    memset(qinding,0,sizeof(qinding));
    memset(pat,0,sizeof(pat));
    int n , m;
    cin >> n >> m;
    FOR(i,m,x,y) {
      cin >> c >> x >> y;
      meow[x][y] = c;
      if (c != '+') {
        pat[x] = y+n ; pat[y+n] = x;qinding[x] = qinding[y+n] = true;
      }
      if (c != 'x') {
        pat[x+y+n+n] = n-x+y+n+n+n+n;
        pat[n-x+y+n+n+n+n] = x+y+n+n;
        qinding[x+y+n+n] = qinding[n-x+y+n+n+n+n] = true;
      }
    }
    FOR(x,n) FOR(y,n) {
      if (!qinding[x] && !qinding[y+n]) add_edge(x,y+n);
      if (!qinding[x+y+n+n] && !qinding[n-x+y+n+n+n+n]) add_edge(x+y+n+n,n-x+y+n+n+n+n);
    }
    
    FOR(i,n) {
      memset(visit,0,sizeof(visit));
      if (!qinding[i] && !pat[i]) Gao(i);
    }
    FOR(x,n) FOR(y,n) {
      memset(visit,0,sizeof(visit));
      if (!qinding[x+y+n+n] && !pat[x+y+n+n]) Gao(x+y+n+n);
    }
    
    FOR(x,n) FOR(y,n) {
      if (pat[x] == y+n) {
        if (pat[x+y+n+n] == n-x+y+n*4) meow2[x][y] = 'o';
        else meow2[x][y] = 'x';
      }
      else if (pat[x+y+n+n] == n-x+y+n*4) meow2[x][y] = '+';
    }
    int ans1 = 0 , ans2 = 0;
    FOR(x,n) FOR(y,n) {
      if (meow2[x][y]) ans1 += 1 + (meow2[x][y] == 'o');
      ans2 += meow2[x][y] != meow[x][y];
    }
    cout << ans1 << ' ' << ans2 << endl;
    FOR(x,n) FOR(y,n) if (meow2[x][y] != meow[x][y]) {
      cout << (char)meow2[x][y] << ' ' << x << ' ' << y << endl;
    }
  }
  return 0;
}
