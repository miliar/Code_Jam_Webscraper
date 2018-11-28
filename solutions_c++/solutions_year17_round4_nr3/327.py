#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define ROF(i, n) for (int i = (n) - 1; i >= 0; --i)
#define REP(i, n) for (int i = 1; i <= (n); ++i)
#define REP3(i, s, n) for (int i = (s); i <= (n); ++i)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int dk[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
inline int turn(char mir, int dir) {
  if (mir == '/') return dir ^ 1;
  return 3 - dir;
}

int T, R, C, hist[64 * 64];
char b[64][64];
char lol[64][64];
int si[64 * 64], sj[64 * 64], pred[64 * 64];
vector<int> shooters;
set<int> opt[64*64][2];

inline int id(int i, int j) { return i * C + j; }

set<int> simulate(int si, int sj, char x) {
  set<int> hit;
  hit.insert(id(si, sj));
  /* memset(lol, 0, sizeof lol); */
  FOR (i, R) FOR (j, C) lol[i][j] = '.';
  FOR (k, 2) {
    int i = si, j = sj;
    int dir = (x == '-') ? (1 + 2 * k) : (2 * k);
    /* lol[i][j] = '0'; */
    set<int> vis;
    vis.insert(id(i, j));
    while (true) {
      i += dk[dir][0];
      j += dk[dir][1];
      if (!(i >= 0 && i < R && j >= 0 && j < C)) break;
      if (b[i][j] == '#') break;
      if (b[i][j] == '|' || b[i][j] == '-') return set<int>();
      if (b[i][j] == '/' || b[i][j] == '\\')
        dir = turn(b[i][j], dir);
      if (vis.find(id(i, j)) != vis.end()) break;
      vis.insert(id(i, j));
      hit.insert(id(i, j));
      /* lol[i][j] = '0'; */
    }
  }
  /* cout << si << " " << sj << " " << x <<endl; */
  /* FOR (i, R) cout << lol[i] << endl; */
  return move(hit);
}

set<int> remain;
bool dfs(int u) {
  if (u == shooters.size()) {
    return remain.empty();
  }

  FOR (k, 2) {
    if (opt[u][k].size() == 0) continue;
    for (auto c : opt[u][k]) {
      if (hist[c] == 0) remain.erase(c);
      ++hist[c];
    }
    bool res = dfs(u + 1);
    for (auto c : opt[u][k]) {
      --hist[c];
      if (hist[c] == 0) remain.insert(c);
    }
    if (res) {
      pred[u] = k;
      return true;
    }
  }
  return false;
}

int main() {
  cin >> T;
  REP (tc, T) {
    cin >> R >> C;
    FOR (i, R) cin >> b[i];
    shooters.clear();

    memset(hist, 0, sizeof(hist));
    bool ok = true;
    FOR (i, R) {
      FOR (j, C) if (b[i][j] == '-' || b[i][j] == '|') {
        int idx = shooters.size();
        si[idx] = i;
        sj[idx] = j;
        shooters.push_back(id(i, j));
        opt[idx][0].clear(), opt[idx][1].clear();

        opt[idx][0] = simulate(i, j, '-');
        opt[idx][1] = simulate(i, j, '|');
        if (opt[idx][0].size() == 0 && opt[idx][1].size() == 0)
          ok = false;

        set<int> same;
        for (auto c: opt[idx][0])
          if (opt[idx][1].find(c) != opt[idx][1].end())
            same.insert(c);
        for (auto c: same)
          opt[idx][0].erase(c), opt[idx][1].erase(c), ++hist[c];

        if (opt[idx][0].size() == 0 && opt[idx][1].size() == 0) {
          shooters.pop_back();
        } else if (opt[idx][0].size() == 0 || opt[idx][1].size() == 0) {
          for (auto c: opt[idx][0]) ++hist[c];
          for (auto c: opt[idx][1]) ++hist[c];
          char which = (opt[idx][0].size() == 0) ? '|' : '-';
          b[i][j] = which;
          shooters.pop_back();
        }
      }
    }

    remain.clear();
    FOR (i, R) FOR (j, C) if (b[i][j] != '#' && hist[id(i, j)] == 0)
      remain.insert(id(i, j));
    if (ok) ok = dfs(0);

    cout << "Case #" << tc << ": ";
    cout << (ok ? "POSSIBLE" : "IMPOSSIBLE") << endl;
    if (ok) {
      FOR (u, (int) shooters.size()) {
        char x = "-|"[pred[u]];
        b[si[u]][sj[u]] = x;
      }
      FOR (i, R) cout << b[i] << endl;
    }
  }
  return 0;
}
