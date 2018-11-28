#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <set>
using namespace std;

typedef long long ll;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<Mi> MMi;
typedef vector<string> Vs;
typedef pair<int, int> P;
typedef pair<P, int> PP;
typedef vector<P> Vp;

const int diri[4] = {-1, 0, 1, 0};
const int dirj[4] = {0, 1, 0, -1};
const int map_forward[4] = {1, 0, 3, 2};
const int map_backwards[4] = {3, 2, 1, 0};


int R, C;
Vs mat;

Vp positions;
Vi solution;
Vi coverage;
MMi coverages;

int cell_to_id(int r, int c) {
  return r*C + c;
}

// void print_coverage(const Vi& v) {
//   for (int i = 0; i < R; ++i) {
//     for (int j = 0; j < C; ++j) {
//       if (v[cell_to_id(i, j)]) {
//         cerr << "x";
//       } else {
//         cerr << ".";
//       }
//     }
//     cerr << endl;
//   }
// }

// void print_vector(const Vi& v) {
//   cout << v.size() << ": ";
//   for (int i = 0; i < int(v.size()); ++i) {
//     cout << " " << v[i];
//   }
//   cout << endl;
// }

bool all_covered(const Vi& v) {
  // cerr << "ALL COVERED?" <<endl;
  // print_coverage(v);
  // print_vector(v);
  // print_coverage(v);
  for (int i = 0; i < R*C; ++i) {
    if (v[i] == 0) {
      // cerr << "NO " << i << " ()"<< endl;
      return false;
    }
  }
  return true;
}


bool possible(int k) {
  // cerr << "POSSIBLE? k=" << k << endl;
  // print_coverage(coverage);
  Vi potential_coverage = coverage;
  for (int p = k; p < int(positions.size()); ++p) {
    for (int hor = 0; hor < 2; ++hor) {
      if (coverages[p][hor].size()) {
        for (int i = 0; i < R*C; ++i) {
          potential_coverage[i] += coverages[p][hor][i];
        }
      }
    }
  }
  // cerr << "POTENTIAL COVERAGE:" << endl;
  // print_coverage(potential_coverage);
  return all_covered(potential_coverage);
}

bool bt(int k) {
  // cerr << "BT k=" << k << endl;
  if (k == int(positions.size())) {
    return all_covered(coverage);
  }
  if (!possible(k)) {
    // cerr << "NOT POSSIBLE" << endl;
    return false;
  }
  for (int hor = 0; hor < 2; ++hor) {
    if (coverages[k][hor].size() == 0) {
      continue;
    }
    solution[k] = hor;
    for (int i = 0; i < R*C; ++i) {
      coverage[i] += coverages[k][hor][i];
    }
    if (bt(k + 1)) {
      return true;
    }
    for (int i = 0; i < R*C; ++i) {
      coverage[i] -= coverages[k][hor][i];
    }
  }
  return false;
}

int next_dir(char x, int d) {
  if (x == '/') {
    return map_forward[d];
  }
  if (x == '\\') {
    return map_backwards[d];
  }
  return d;
}

Vp get_positions(const set<PP>& vist) {
  set<P> pos;
  for (set<PP>::iterator it = vist.begin(); it != vist.end(); ++it) {
    pos.insert(it->first);
  }
  return Vp(pos.begin(), pos.end());
}

Vp path(int r, int c, int d) {
  set<PP> vist;
  while (true) {
    if (r < 0 || r >= R || c < 0 || c >= C || mat[r][c] == '#') {
      break;
    }
    PP p(P(r, c), d);
    if (vist.count(p)) {
      break;
    }
    vist.insert(p);
    d = next_dir(mat[r][c], d);
    r += diri[d];
    c += dirj[d];
  }
  return get_positions(vist);
}

Vi path_to_coverage(const Vp& v) {
  Vi res(R*C, 0);
  for (int i = 0; i < int(v.size()); ++i) {
    res[cell_to_id(v[i].first, v[i].second)] = 1;
  }
  return res;
}

bool check_path(const Vp& v) {
  for (int i = 0; i < int(v.size()); ++i) {
    if (mat[v[i].first][v[i].second] == '|' ||
        mat[v[i].first][v[i].second] == '-') {
      return false;
    }
  }
  return true;
}

Vi coverage_union(const Vi& v1, const Vi& v2) {
  Vi res(R*C, 0);
  for (int i = 0; i < R*C; ++i) {
    res[i] = v1[i] || v2[i] ? 1 : 0;
  }
  return res;
}

Vi initial_coverage() {
  Vi res(R*C, 0);
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      if (mat[i][j] == '#' || mat[i][j] == '|' || mat[i][j] == '-' ||
          mat[i][j] == '/' || mat[i][j] == '\\') {
        res[cell_to_id(i, j)] = 1;
      }
    }
  }
  return res;
}

Mi get_coverage(int r, int c) {
  Mi res(2);
  for (int hor = 0; hor < 2; ++hor) {
    Vp p1, p2;
    if (hor == 0) {
      p1 = path(r - 1, c, 0);
      p2 = path(r + 1, c, 2);
    } else {
      p1 = path(r, c - 1, 3);
      p2 = path(r, c + 1, 1);
    }
    if (!check_path(p1) || !check_path(p2)) {
      continue;
    }
    res[hor] = coverage_union(path_to_coverage(p1),
                              path_to_coverage(p2));
  }
  return res;
}

bool is_laser(char x) {
  return x == '|' || x == '-';
}

Vs fun() {
  positions.clear();
  coverages.clear();
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      if (is_laser(mat[i][j])) {
        positions.push_back(P(i, j));
        Mi cov = get_coverage(i, j);
        if (cov[0].size() == 0 && cov[1].size() == 0) {
          return Vs();
        }
        if (cov[0] == cov[1]) {
          cov[1] = Vi();
        }
        coverages.push_back(cov);
      }
    }
  }

  // cerr << "COVERAGES:" << endl;
  // for (int i = 0; i < coverages.size(); ++i) {
  //   for (int hor = 0; hor < 2; ++hor) {
  //     if (coverages[i][hor].size()) {
  //       cerr << "i=" << i << " hor=" << hor << endl;
  //       print_coverage(coverages[i][hor]);
  //     }
  //   }
  // }
  // cerr << "initial:" << endl;
  // print_coverage(initial_coverage());

  coverage = initial_coverage();
  solution = Vi(positions.size());
  if (!bt(0)) {
    return Vs();
  }
  Vs res = mat;
  for (int i = 0; i < int(positions.size()); ++i) {
    if (solution[i] == 0) {
      res[positions[i].first][positions[i].second] = '|';
    } else {
      res[positions[i].first][positions[i].second] = '-';
    }
  }
  return res;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cin >> R >> C;
    mat = Vs(R);
    for (int i = 0; i < R; ++i) {
      cin >> mat[i];
    }
    Vs res = fun();
    cout << "Case #" << cas << ": ";
    if (res.size() == 0) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << "POSSIBLE" << endl;
      for (int i = 0; i < R; ++i) {
        cout << res[i] << endl;
      }
    }
  }
}
