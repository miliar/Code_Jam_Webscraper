#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

using ll = long long;
using ld = long double;

template <typename T> T &chmin(T &a, const T &b) { return a = min(a, b); }
template <typename T> T &chmax(T &a, const T &b) { return a = max(a, b); }

template<typename T> T inf;
template<> constexpr int inf<int> = 1e9;
template<> constexpr ll inf<ll> = 1e18;
template<> constexpr ld inf<ld> = 1e30;

struct yes_no : numpunct<char> {
  string_type do_truename()  const { return "Yes"; }
  string_type do_falsename() const { return "No"; }
};

class UnionFind {
  vector<int> p;
public:
  UnionFind (int n) : p(n, -1) {}
  int root(int x) {
    return p[x] < 0 ? x : p[x] = root(p[x]);
  }
  bool same(int x, int y) {
    return root(x) == root(y);
  }
  bool unite(int x, int y) {
    x = root(x); y = root(y);
    if (x == y) return false;
    if (p[y] < p[x]) swap(x, y);
    if (p[x] == p[y]) --p[x];
    p[y] = x;
    return true;
  }
};

class SAT {
public:
  static const int MAX_V = 10010;
  vector<int> g[MAX_V], rg[MAX_V], vs;
  bool used[MAX_V];
  int cmp[MAX_V], V, N;

  SAT (int n) : V(2 * n), N(n) {;}

  //(X_2 | !X_5) -> add_closure(2, 1, 5, 0)
  void add_closure(int i, bool bi, int j, bool bj) {
    add_edge(i + N * !bi, j + N * bj);
    add_edge(j + N * !bj, i + N * bi);
  }
  
  void add_edge(int from, int to) {
    g[from].push_back(to);
    rg[to].push_back(from);
  }
  
  void dfs(int v) {
    used[v] = true;
    for (int i : g[v]) if (!used[i]) dfs(i);
    vs.push_back(v);
  }
  
  void rdfs(int v, int k) {
    used[v] = true; cmp[v] = k;
    for (int i : rg[v]) if (!used[i]) rdfs(i, k);
  }

  //no solution: {}, else {1, 0, 1,...}
  vector<bool> solve() {
    memset(used, 0, sizeof(used));
    vs.clear();
    REP(v, V) if (!used[v]) dfs(v);
    memset(used, 0, sizeof(used));
    reverse(ALL(vs));
    int k = 0;
    for (int i : vs) if (!used[i]) rdfs(i, k++);
    vector<bool> res;
    REP(i, N) if (cmp[i] == cmp[i + N]) return res;
    REP(i, N) {
      if (cmp[i] > cmp[N + i]) res.push_back(true);
      else res.push_back(false);
    }
    return res;
  }
};

int C, R;
string s[64];

void output(bool res) {
  static int case_num = 0;
  printf("Case #%d: ", ++case_num);
  printf(res ? "POSSIBLE\n" : "IMPOSSIBLE\n");
  if (res) {
    REP(i,C) printf("%s\n", s[i].c_str());
  }
}

int get_id(int i, int j, int dir) {
  return ((i * R) + j) * 4 + dir;
}

int main() {
  locale loc(locale(), new yes_no);
  cout << boolalpha;
  cout.imbue(loc);
  int Q_num;
  scanf("%d", &Q_num);
  while (Q_num--) {
    scanf("%d%d", &C, &R);
    REP(i,C) cin >> s[i];
    const int Nodes = C * R * 4;
    UnionFind uf(Nodes);
    vector<int> choice(Nodes, -1);
    vector<int> choice_dir(Nodes, -1);
    REP(i,C) REP(j,R) {
      switch (s[i][j]) {
      case '/':
        uf.unite(get_id(i, j, 0), get_id(i, j, 3));
        uf.unite(get_id(i, j, 1), get_id(i, j, 2));
        break;
      case '\\':
        uf.unite(get_id(i, j, 0), get_id(i, j, 1));
        uf.unite(get_id(i, j, 2), get_id(i, j, 3));
        break;
      case '#':
        break;
      default:
        uf.unite(get_id(i, j, 0), get_id(i, j, 2));
        uf.unite(get_id(i, j, 1), get_id(i, j, 3));
        break;
      }
    }
    REP(i,C) REP(j,R-1) uf.unite(get_id(i, j, 0), get_id(i, j + 1, 2));
    REP(i,C-1) REP(j,R) uf.unite(get_id(i, j, 3), get_id(i + 1, j, 1));
    vector<pair<int,int>> beams;
    REP(i,C) REP(j,R) {
      if (s[i][j] == '-' || s[i][j] == '|')
        beams.emplace_back(i, j);
    }
    sort(ALL(beams));
    REP(i,C) REP(j,R) {
      if (s[i][j] == '-' || s[i][j] == '|') {
        const int p = lower_bound(ALL(beams), make_pair(i, j)) - begin(beams);
        REP(dir,2) {
          const int r = uf.root(get_id(i, j, dir));
          // cout << i << " " << j << " " << dir << " " << r << endl;
          if (choice[r] == -1) { choice[r] = p; choice_dir[r] = dir; }
          else choice[r] = -2;
          // cout << i << " " << j << " " << dir << " " << choice[r] << endl;
        }
      }
    }
    const int beam_num = beams.size();
    SAT sat(beam_num);
    bool flag = true;
    REP(i,C) REP(j,R) {
      if (s[i][j] == '-' || s[i][j] == '|') {
        const int p = lower_bound(ALL(beams), make_pair(i, j)) - begin(beams);
        // cout << p << endl;
        REP(dir,2) {
          if (choice[uf.root(get_id(i, j, dir))] == -2) {
            // cout << p << " " << (dir ^ 1) << endl;
            // cout << p << " " << dir << endl;
            sat.add_closure(p, dir ^ 1, p, dir ^ 1);
          }
        }
      }
      else if (s[i][j] == '.') {
        vector<pair<int,int>> cand;
        REP(dir,2) {
          int r = uf.root(get_id(i, j, dir));
          if (choice[r] >= 0)
            cand.emplace_back(choice[r], choice_dir[r]);
        }
        if (cand.empty()) flag = false;
        else if (cand.size() == 1) {
          int a1, b1; tie(a1, b1) = cand[0];
          sat.add_closure(a1, b1, a1, b1);
        }
        else {
          int a1, b1; tie(a1, b1) = cand[0];
          int a2, b2; tie(a2, b2) = cand[1];
          sat.add_closure(a1, b1, a2, b2);
          // cout << a1 << " " << b1 << " " << a2 << " " << b2 << endl;
        }
      }
    }
    // cout << beams.size() << endl;
    // cout << "ok" << endl;
    vector<bool> res = sat.solve();
    if (!flag || res.empty()) { output(false); continue; }
    REP(i,beam_num) {
      int y, x; tie(y, x) = beams[i];
      s[y][x] = (res[i] ? '-' : '|');
    }
    output(true);
  }
  return 0;
}

