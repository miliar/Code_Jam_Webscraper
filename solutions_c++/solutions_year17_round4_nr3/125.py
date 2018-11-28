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
#define MAXN 1000005

// MAXN has to be greater than the number of conditions and TWICE the number of variables
int A, V; // Number of conditions (a or b) that have to be fulfilled, number of variables
bool condsig[MAXN][2]; // The sign of the part of the condition (false means not)
int condvar[MAXN][2]; // Number of the variable in the part of the condition
bool solution[MAXN]; // A possible assignment of variables; not necessary if the question is just WHETHER there is a solution

VI adj[MAXN], radj[MAXN], *cadj;
bool vis[MAXN];
VI order;
int comp[MAXN], compnr;
VI incomp[MAXN], adjcomp[MAXN]; // not necessary if the question is just WHETHER there is a solution
bool viscomp[MAXN], isset[MAXN]; // not necessary if the question is just WHETHER there is a solution

void visitcomp(int i) { // not necessary if the question is just WHETHER there is a solution
  if (viscomp[i]) return;
  viscomp[i] = true;
  REP(j,0,adjcomp[i].size()){
    int k = adjcomp[i][j];
    visitcomp(k);
  }
  isset[i] = true;
  REP(j,0,incomp[i].size()){
    int k = incomp[i][j];
    solution[k/2] = (isset[comp[incomp[i][j]^1]]+k)%2;
  }
}

void findsolution() { // not necessary if the question is just WHETHER there is a solution
  REP(i,0,compnr) {
    incomp[i].clear();
    adjcomp[i].clear();
    viscomp[i] = false;
    isset[i] = false;
  }
  REP(i,0,2*V) {
    incomp[comp[i]].push_back(i);
    REP(j,0,adj[i].size()){
      int k = adj[i][j];
      adjcomp[comp[i]].push_back(comp[k]);
    }
  }
  REP(i,0,compnr) visitcomp(i);
}

void dfs(int i) {
  if (vis[i]) return;
  vis[i] = true;
  comp[i] = compnr;
  REP(j,0,cadj[i].size()) dfs(cadj[i][j]);
  order.push_back(i);
}

bool solve() { // Returns whether all conditions are simultaneously satisfiable
  REP(i,0,2*V) {
    adj[i].clear();
    radj[i].clear();
  }
  REP(i,0,A) {
    int v0 = 2*condvar[i][0]+condsig[i][0];
    int v1 = 2*condvar[i][1]+condsig[i][1];
    adj[v0^1].push_back(v1);
    radj[v1].push_back(v0^1);
    adj[v1^1].push_back(v0);
    radj[v0].push_back(v1^1);
  }
  fill_n(vis, 2*V, false);
  order.clear();
  cadj = adj;
  REP(i,0,2*V) dfs(i);
  fill_n(vis, 2*V, false);
  compnr = 0;
  cadj = radj;
  for (int i = 2*V-1; i >= 0; i--)
    if (!vis[order[i]]) {
      dfs(order[i]);
      compnr++;
    }
  REP(i,0,V) if (comp[2*i] == comp[2*i+1]) return false;
  findsolution(); // not necessary if the question is just WHETHER there is a solution
  return true;
}

// Set A to 0 and V to the number of variables before running 2-SAT.
void add(int v1, bool s1, int v2, bool s2){
  condvar[A][0] = v1;
  condvar[A][1] = v2;
  condsig[A][0] = s1;
  condsig[A][1] = s2;
  A++;
}

char g[55][55];
int N, M, v[55][55], lbl[55][55];
int from[4] = {1,0,3,2}, touchf;
PII hit;
void dfs(int x, int y, int f) {
  if (x < 0 || y < 0 || x >= N || y >= M || v[x][y]) return;
  v[x][y] = 1;
  if (g[x][y] == '#') return;
  if (g[x][y] == '-') {
    hit = PII(x,y);
    touchf = f;
    return;
  }
  if (g[x][y] == '/') {
    if (f == 0) dfs(x, y-1, from[2]);
    else if (f == 2) dfs(x-1, y, from[0]);
    else if (f == 3) dfs(x+1, y, from[1]);
    else if (f == 1) dfs(x, y+1, from[3]);
  } else if (g[x][y] == '\\') {
    if (f == 0) dfs(x, y+1, from[3]);
    else if (f == 3) dfs(x-1, y, from[0]);
    else if (f == 2) dfs(x+1, y, from[1]);
    else if (f == 1) dfs(x, y-1, from[2]);
  } else if (g[x][y] == '.') {
    if (f == 0) dfs(x+1, y, f);
    else if (f == 1) dfs(x-1, y, f);
    else if (f == 2) dfs(x, y+1, f);
    else if (f == 3) dfs(x, y-1, f);
  }
}
pair<PII, int> seek(int x, int y, int d) {
  FILL(v, 0);
  hit = PII(-1,-1); touchf = -1;
  if (d == 0) dfs(x-1, y, from[d]);
  else if (d == 1) dfs(x+1, y, from[d]);
  else if (d == 2) dfs(x, y-1, from[d]);
  else if (d == 3) dfs(x, y+1, from[d]);
  return make_pair(hit, touchf);
}
PII grab(pair<PII, int> a, pair<PII,int> b) {
  if (a.second != -1 && b.second != -1 || a.first == b.first) {
    // beam conflict or shoot itself
    // handled by avoid
  } else if (a.second != -1 || b.second != -1) {
    pair<PII, int> pt = a.second != -1 ? a : b;
    int x = lbl[pt.first.first][pt.first.second], f = pt.second;
    if (f == 0 || f == 1) {
      return PII(x, true);
    } else {
      return PII(x, false);
    }
  }
  return PII(-1,-1);
}
int main() {
  freopen("input", "r", stdin);
  //freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    //cerr << csn << endl;
    cin >> N >> M;
    A = V = 0;
    REP(i,0,N) {
      scanf("%s", g[i]);
      REP(j,0,M) {
        if (g[i][j] == '|' || g[i][j] == '-') {
          g[i][j] = '-';
          lbl[i][j] = V++;
        }
      }
    }
    bool bad = 0;
    REP(i,0,N) {
      REP(j,0,M) {
        if (g[i][j] == '-') {
          pair<PII, int> up = seek(i,j,0);
          pair<PII, int> down = seek(i,j,1);
          pair<PII, int> left = seek(i,j,2);
          pair<PII, int> right = seek(i,j,3);
          int x = lbl[i][j];
          if (up.second != -1 || down.second != -1) {
            add(x, false, x, false);
          }
          if (left.second != -1 || right.second != -1) {
            add(x, true, x, true);
          }
        }
        if (g[i][j] == '.') {
          pair<PII, int> up = seek(i,j,0);
          pair<PII, int> down = seek(i,j,1);
          pair<PII, int> left = seek(i,j,2);
          pair<PII, int> right = seek(i,j,3);
          PII vert = grab(up, down);
          PII hori = grab(left, right);
          if (vert.first == -1 && hori.first == -1) {
            bad = 1;
          } else if (vert.first != -1 && hori.first != -1) { // two possible
            add(vert.first, vert.second, hori.first, hori.second);
          } else {
            PII got = vert.first != -1 ? vert : hori;
            add(got.first, got.second, got.first, got.second);
          }
        }
      }
    }
    if (bad) puts("IMPOSSIBLE");
    else {
      bool ok = solve();
      if (!ok) {
        puts("IMPOSSIBLE");
      } else {
        puts("POSSIBLE");
        REP(i,0,N) {
          REP(j,0,M) {
            if (g[i][j] == '-') {
              int x = lbl[i][j];
              if (solution[x] == false) printf("-");
              else printf("|");
            } else printf("%c", g[i][j]);
          }
          puts("");
        }
      }
    }
  }
  return 0;
}
