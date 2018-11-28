#include <bits/stdc++.h>

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define x first
#define y second

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

int r, c;
string mat[55];
bool ud[55][55], lr[55][55];

bool spread(int x, int y, int dx, int dy){
  while (true){
    if (x < 0 || y < 0 || x >= r || y >= c) return true;
    if (mat[x][y] == '#') return true;
    if (mat[x][y] != '.') return false;
    x += dx, y += dy;
  }
}

vector<int> nxt(int y, vector<int> st){
  string s;
  REP(x,r) s.pb(mat[x][y]);
  REP(x,r){
    if (s[x] == '#') continue;
    if (s[x] == '.') continue;
    if (s[x] == '-'){
      st[x] = 1;
    }
    if (s[x] == '|'){
      int nx = x-1;
      while (nx >= 0 && s[nx] == '.') s[nx] = '#', --nx;
      nx = x+1;
      while (nx < r && s[nx] == '.') s[nx] = '#', ++nx;
    }
  }
  REP(x,r) if (s[x] == '.' && st[x] != 1) st[x] = 2;
  return st;
}

map<vector<int>, bool> M[55];

// 0 == bmk
// 1 == imam odozada
// 2 == trebam naprijed
bool dp(int id, vector<int> st){
  if (id == c){
    for (auto t : st) if (t == 2) return false;
    return true;
  }
  if (M[id].count(st)) return M[id][st];
  bool &rr = M[id][st];
  vector<int> all;
  REP(x,r){
    if (mat[x][id] == '#'){
      if (st[x] == 2) return rr = false;
      if (st[x] == 1) st[x] = 0;
    }
    if (mat[x][id] == '-' || mat[x][id] == '|'){
      if (st[x] == 1) return rr = false;
      all.pb(x);
    }
  }
  REP(bit,1<<all.size()){
    bool check = true;
    REP(i,all.size()){
      if ((bit>>i)&1) check &= ud[all[i]][id], mat[all[i]][id] = '|';
      else check &= lr[all[i]][id], mat[all[i]][id] = '-';
    }
    if (!check) continue;
    if (dp(id+1, nxt(id, st))) return rr = true;
  } return rr = false;
}

void rek(int id, vector<int> st){
  if (id == c){
    for (auto t : st) if (t == 2) assert(false);
    return;
  }
  vector<int> all;
  REP(x,r){
    if (mat[x][id] == '#'){
      if (st[x] == 2) assert(false);
      if (st[x] == 1) st[x] = 0;
    }
    if (mat[x][id] == '-' || mat[x][id] == '|'){
      if (st[x] == 1) assert(false);
      all.pb(x);
    }
  }
  REP(bit,1<<all.size()){
    bool check = true;
    REP(i,all.size()){
      if ((bit>>i)&1) check &= ud[all[i]][id], mat[all[i]][id] = '|';
      else check &= lr[all[i]][id], mat[all[i]][id] = '-';
    }
    if (!check) continue;
    if (dp(id+1, nxt(id, st))){rek(id+1, nxt(id, st)); return;}
  } assert(false);
}

void solve(){
  cin >> r >> c;
  REP(i,r) cin >> mat[i];
  REP(i,c) M[i].clear();
  REP(x,r) REP(y,c) if (mat[x][y] == '-' || mat[x][y] == '|'){
    ud[x][y] = spread(x+1, y, +1, 0) && spread(x-1, y, -1, 0);
    lr[x][y] = spread(x, y+1, 0, +1) && spread(x, y-1, 0, -1);
  }
  if (dp(0, vector<int>(r, 0))){
    cout << "POSSIBLE" << endl;
    rek(0, vector<int>(r, 0));
    REP(i,r) cout << mat[i] << endl;
  } else cout << "IMPOSSIBLE" << endl;
}

int main(){
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  TRACE(t);
  REP(i,t) TRACE(i+1), cout << "Case #" << i+1 << ": ", solve();

  return 0;
}
