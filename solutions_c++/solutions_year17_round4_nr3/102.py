#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <stack>

#define r first
#define c second
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR (i, 0, n)
#define _ << " _ " <<
#define TRACE(x) cerr << #x << " = " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define debug
#define TRACE(x)

using namespace std;
using pii = pair<int, int>;

typedef long long llint;


/*
- postavit MAXN na 2*broj_varijabli
- pozvat init(broj_varijabli)
- add_impl dodaje implikaciju v(i)=vi -> v(j)=vj
- add_must postavlja vrijednost v(i) = vi
- add_or dodaje v(i)=vi ili v(j)=vj
- solve() rijesava sustav, vraca true ako je nasao rjesenje, false inace,
nakon toga, niz val[i] = v(i)
*/

namespace sat {
  const int MAXN = 10500;

  vector<int> E[MAXN];

  bool ans[MAXN];
  bool stk[MAXN];
  int val[MAXN];
  int disc[MAXN];
  int n, t;
  bool consistent;

  stack<int> S;
  
  int tarjan(int x) {
    int lw = disc[x] = ++t;
    
    stk[x] = true;
    S.push(x);

    for (int y: E[x])
      if (disc[y] == 0) lw = min(lw, tarjan(y)); else
        if (stk[y]) lw = min(lw, disc[y]);
    
    if (lw == disc[x]) {
      vector<int> comp;
      bool ok = true;
      while (!S.empty()) {
        int y = S.top(); S.pop();
        comp.push_back(y);
        ok &= val[y/2] == -1;
        stk[y] = false;
        if (y == x) break;
      }

      if (ok) {
        for (int y: comp)
          val[y/2] = y&1;
        for (int y: comp)
          if (val[y/2] != (y&1)) consistent = false;
      }
    }
    return lw;
  }

  bool solve() {
    consistent = true;
    REP(i, 2*n)
      if (!disc[i]) tarjan(i);
    return consistent;
  }
  
  void add_impl(int i, bool vi, int j, bool vj) {
    E[2*i + vi].push_back(2*j + vj);
    E[2*j + !vj].push_back(2*i + !vi);
  }

  void add_or(int i, bool vi, int j, bool vj) {
    add_impl(i, !vi, j, vj);
    add_impl(j, !vj, i, vi);
  }

  void add_val(int i, bool vi) {
    add_impl(i, !vi, i, vi);
  }
  
  void init(int _n) {
    n = _n, t = 0;
    REP(i, 2*n) {
      disc[i] = 0;
      stk[i] = false;
      E[i].clear();
    }
    REP(i, n) val[i] = -1;
  }
};
const int MAXN = 55;
const int DR[] = {-1, 1, 0, 0};
const int DC[] = {0, 0, 1, -1};

int R, C;
char a[MAXN][MAXN];
vector<pii> shoot;
vector<int> dirs;

bool shooter(char c){ return c == '|' || c == '-'; }
bool in(int r, int c) { return r >= 0 && c >= 0 && r < R && c < C; }
int id(pii x) { return x.r * C + x.c; }

void dfs(int r, int c, int dir) {
  TRACE(r _ c _ dir);
  if (!in(r,c)) return;
  if (a[r][c] == '#') return;
  
  if (a[r][c] == '/') {
    if (dir == 0) dir = 2;
    else if (dir == 2) dir = 0;
    else if (dir == 1) dir = 3;
    else if (dir == 3) dir = 1;
  } else if (a[r][c] == '\\') {
    if (dir == 0) dir = 3;
    else if (dir == 3) dir = 0;
    else if (dir == 1) dir = 2;
    else if (dir == 2) dir = 1;
  } else if (shooter(a[r][c])) {
    TRACE("s " _ r _ c);
    shoot.push_back({r, c});
    dirs.push_back(dir);
    return;
  } 
  dfs(r + DR[dir], c + DC[dir], dir);
}

void solve(int tc) {
  scanf("%d %d",&R,&C);
  REP(r, R) scanf("%s",a[r]);

  sat::init(R*C);

  REP(r, R) REP(c, C) {
    TRACE(r _ c);
    if (a[r][c] == '-' || a[r][c] == '|') {
      int i = r * C + c;
      REP(t, 2) {
	shoot.clear();
	dirs.clear();
	
	dfs(r + DR[2*t], c + DC[2*t], 2*t);
	dfs(r + DR[2*t+1], c + DC[2*t+1], 2*t+1);
	
	if (!shoot.empty())
	  sat::add_impl(i, t, i, t^1);
      }
    } else if (a[r][c] == '.'){
      int i[2], v[2];

      REP(t, 2) {
	i[t] = v[t] = -1;
	
	shoot.clear();
	dirs.clear();
	
	dfs(r + DR[2*t], c + DC[2*t], 2*t);
	dfs(r + DR[2*t+1], c + DC[2*t+1], 2*t+1);
	
	if ((int)shoot.size() != 1) continue;
	i[t] = id(shoot[0]);
	v[t] = dirs[0] / 2;
      }

      if (i[0] == -1 && i[1] == -1) {
	debug("Polje %d %d nema laser ili ima previse\n",r,c);
	printf("Case #%d: IMPOSSIBLE\n",tc);
	return;
      }
      if (i[0] != -1 && i[1] != -1) {
	sat::add_or(i[0], v[0], i[1], v[1]);
      } else if (i[0] != -1) {
	sat::add_val(i[0], v[0]);
      } else {
	sat::add_val(i[1], v[1]);
      }
    }
  }

  debug("ide 2 sat\n");
  
  bool ok = sat::solve();
  if (!ok) {
    printf("Case #%d: IMPOSSIBLE\n",tc);
    return;
  }
  
  printf("Case #%d: POSSIBLE\n",tc);
  REP(r, R) {
    REP(c, C) {
      if (a[r][c] == '-' || a[r][c] == '|') {
	int x = sat::val[r*C + c];
	printf(x == 0 ? "|" : "-");
      } else {
	printf("%c",a[r][c]);
      }
    }
    printf("\n");
  }
}

int main(void) {
  int t;
  scanf("%d",&t);
  REP(it, t) 
    solve(it+1);
  return 0;
}
