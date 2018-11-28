#include <cstdio>
#include <ctime>
#include <iostream>
#include <vector>

using namespace std;

typedef long long int64;

#define DPRINT(x) cerr << __LINE__ << ": " << #x << " = " << x << endl;

template <class T1, class T2>
ostream& operator <<(ostream& os, const pair<T1, T2>& v);

template <class T>
ostream& operator <<(ostream& os, const vector<T>& v) {
    os << "[";
    for (typename vector<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
        if (ii != v.begin()) os << " ";
        os << *ii;
    }
    os << "]";
    return os;
}

template <class T1, class T2>
ostream& operator <<(ostream& os, const pair<T1, T2>& v) {
    os << "(" << v.first << " " << v.second << ")";
    return os;
}

struct Graph {
  int n;
  vector<vector<int>> g, gt;

  vector<bool> used;
  vector<int> order, comp;
  vector<bool> sat2_ans;

  void dfs1(int v) {
    used[v] = true;
    for (size_t i=0; i<g[v].size(); ++i) {
      int to = g[v][i];
      if (!used[to])
        dfs1(to);
    }
    order.push_back (v);
  }

  void dfs2(int v, int cl) {
    comp[v] = cl;
    for (size_t i=0; i<gt[v].size(); ++i) {
      int to = gt[v][i];
      if (comp[to] == -1)
        dfs2(to, cl);
    }
  }

  void resize(int new_n) {
    n = new_n;
    g.resize(n);
    gt.resize(n);
  }

  void add_edge(int u, int v) {
    g[u].push_back(v);
    gt[v].push_back(u);
  }

  bool sat2() {
    used.assign (n, false);
    for (int i=0; i<n; ++i)
      if (!used[i])
        dfs1(i);

    comp.assign(n, -1);
    for (int i=0, j=0; i<n; ++i) {
      int v = order[n-i-1];
      if (comp[v] == -1)
        dfs2(v, j++);
    }

    for (int i=0; i < n; i++)
      if (comp[i] == comp[i ^ 1])
        return false;

    sat2_ans.assign(n, false);
    for (int i=0; i < n; i++)
      sat2_ans[comp[i] > comp[i ^ 1] ? i : i ^ 1] = true;
    return true;
  }
};

const int kLeft = 0;
const int kRight = 1;
const int kUp = 2;
const int kDown = 3;

struct Test {
  int R, C;
  vector<string> plan;

  int num_empty, num_beams;
  vector<vector<int>> empty_ind;
  vector<pair<int,int>> list_empty, list_beams;
  vector<vector<pair<int, bool>>> cover;
  Graph graph;

  bool is_possible;

  void read() {
    cin >> R >> C;
    plan.resize(R);
    for (int i = 0; i < R; i++)
      cin >> plan[i];
  }

  bool trace(int r, int c, int dir, pair<int, bool> beam) {
    // cout << "trace(r=" << r << ", " << "c=" << c << ", dir=" << dir << ", beam=" << beam << ")" << endl;

    if (dir == kRight) c++;
    if (dir == kLeft) c--;
    if (dir == kUp) r--;
    if (dir == kDown) r++;


    if (r < 0 || r >= R || c < 0 || c >= C) return true;

    if (plan[r][c] == '|' || plan[r][c] == '-') return false;  // hit a beam

    if (plan[r][c] == '.') {
      cover[ empty_ind[r][c] ].push_back(beam);
      return trace(r, c, dir, beam);
    }

    if (plan[r][c] == '/') {
      if (dir == kRight) dir = kUp; else
        if (dir == kUp) dir = kRight; else
          if (dir == kDown) dir = kLeft; else
            if (dir == kLeft) dir = kDown;
      return trace(r, c, dir, beam);
    }

    if (plan[r][c] == '\\') {
      if (dir == kRight) dir = kDown; else
        if (dir == kUp) dir = kLeft; else
          if (dir == kDown) dir = kRight; else
            if (dir == kLeft) dir = kUp;
      return trace(r, c, dir, beam);
    }

    if (plan[r][c] == '#')
      return true;

    return true;
  }

  int vert(int beam, bool dir) {
    return beam * 2 + (dir ? 1 : 0);
  }

  void make_one(int beam, bool dir) {
    graph.add_edge(vert(beam, !dir), vert(beam, dir));
  }

  void make_either(int beam1, bool dir1, int beam2, bool dir2) {
    graph.add_edge(vert(beam1, !dir1), vert(beam2, dir2));
    graph.add_edge(vert(beam2, !dir2), vert(beam1, dir1));
  }

  void solve() {
    is_possible = true;
    empty_ind.assign(R, vector<int>(C, -1));

    for (int r = 0; r < R; r++)
      for (int c = 0; c < C; c++) {
        if (plan[r][c] == '.') {
          empty_ind[r][c] = list_empty.size();
          list_empty.push_back({r, c});
        }
        if (plan[r][c] == '|' || plan[r][c] == '-') {
          list_beams.push_back({r, c});
        }
      }

    num_empty = list_empty.size();
    cover.resize(num_empty);

    num_beams = list_beams.size();
    graph.resize(num_beams * 2);

    for (size_t i = 0; i < list_beams.size(); i++) {
      auto rc = list_beams[i];
      vector<bool> beam_options;
      if (trace(rc.first, rc.second, kRight, {i, true}) &&
          trace(rc.first, rc.second, kLeft, {i, true})) {
        beam_options.push_back(true);
      }

      if (trace(rc.first, rc.second, kUp, {i, false}) &&
          trace(rc.first, rc.second, kDown, {i, false})) {
        beam_options.push_back(false);
      }

      // cout << i << " " << rc << "  " << beam_options << endl;
      // cout << trace(rc.first, rc.second, kRight, {i, true}) << endl;
      // cout << trace(rc.first, rc.second, kLeft, {i, true}) << endl;
      // cout << trace(rc.first, rc.second, kUp, {i, false}) << endl;
      // cout << trace(rc.first, rc.second, kDown, {i, false}) << endl;

      if (beam_options.empty()) {
        is_possible = false;
        return;
      }
      if (beam_options.size() == 1) {
        make_one(i, beam_options[0]);
      }
    }

    for (const auto& bb : cover) {
      if (bb.empty()) {
        is_possible = false;
        return;
      }
      if (bb.size() == 1) {
        make_one(bb[0].first, bb[0].second);
        continue;
      }
      if (bb.size() == 2) {
        make_either(bb[0].first, bb[0].second,
                    bb[1].first, bb[1].second);
        continue;
      }
      cerr << "WTF?! " << bb << endl;
      return;
    }

    if (!graph.sat2()) {
      is_possible = false;
      return;
    }

    is_possible = true;
    for (int i = 0; i < graph.n; i++) {
      if (graph.sat2_ans[i]) {
        const auto& rc = list_beams[i / 2];
        plan[rc.first][rc.second] = (i % 2 == 0 ? '|' : '-');
      }
    }
  }

  void print(int num_test) {
    cout << "Case #" << num_test << ": ";
    if (is_possible) {
      cout << "POSSIBLE\n";
      for (int r = 0; r < R; r++)
        cout << plan[r] << "\n";
    } else {
      cout << "IMPOSSIBLE\n";
    }
  }
};


int main() {
  //freopen("input.txt", "rt", stdin);
  freopen("C-small-attempt0.in", "rt", stdin);
  freopen("C-small-attempt0.out", "wt", stdout);

  int T;
  cin >> T;
  vector<Test> tests(T);
  for (int i = 0; i < T; i++)
    tests[i].read();

  #pragma omp parallel for
  for (int i = 0; i < T; i++) {
    clock_t start = clock();
    tests[i].solve();
    fprintf(stderr, "Solved test %d in %.3fs\n", i+1, float(clock() - start) / CLOCKS_PER_SEC);
  }

  for (int i = 0; i < T; i++)
    tests[i].print(i+1);

  return 0;
}
