#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <map>

using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define PATH "C:\\Users\\Valentin\\Desktop\\cpp\\"

template<typename T>
int sz(const T& t) {
  return static_cast<int>(t.size());
}


vector<vector<bool>> solve_lines(int n, vector<vector<bool>> used) {
  vector<bool> used_row(n, false);
  vector<bool> used_col(n, false);
  forn (i, n) {
    forn (j, n) {
      if (used[i][j]) {
        used_row[i] = true;
        used_col[j] = true;
      }
    }
  }
  
  int row = 0;
  int col = 0;

  while (true) {
    while (row < n && used_row[row]) row++;
    while (col < n && used_col[col]) col++;
    if (row >= n || col >= n) break;
    used[row][col] = true;
    row++;
    col++;
  }
  
  return used;
}


//  (0,n-1)             (n-1,n-1)
//
//
//
//   
//         /
//       /
//  (0,0)               (n-1,0)
//
// 0 <= y + (n - 1 - x) < 2 * n - 1
// 0 <= y + x           < 2 * n - 1

vector<vector<int>> g;
vector<int> mt;
vector<int> last_iter;
int iter;

bool dfs(int u) {
  if (last_iter[u] == iter) {
    return false;
  }
  last_iter[u] = iter;
  for (int v : g[u]) {
    if (mt[v] == -1) {
      mt[v] = u;
      return true;
    }
  }
  for (int v : g[u]) {
    if (dfs(mt[v])) {
      mt[v] = u;
      return true;
    }
  }
  
  return false;
}

vector<vector<bool>> solve_diagonals(int n, vector<vector<bool>> used) {
  vector<bool> used_pos(2 * n - 1, false);
  vector<bool> used_neg(2 * n - 1, false);
  
  forn (x, n) {
    forn (y, n) {
      if (used[x][y]) {
        used_pos[y + x] = true;
        used_neg[y + (n - 1 - x)] = true;        
      }
    }
  }
  
  g.assign(2 * n - 1, vector<int>());
  mt.assign(2 * n - 1, -1);
  last_iter.assign(2 * n - 1, -1);
  
  forn (pos, 2 * n - 1) {
    if (used_pos[pos]) {
      continue;
    }
    forn (neg, 2 * n - 1) {
      if (used_neg[neg]) {
        continue;
      }
      int y2 = pos + neg - (n - 1);
      int x2 = pos - neg + (n - 1);
      if (y2 % 2 != 0 || x2 % 2 != 0) {
        continue;
      }
      int y = y2 / 2;
      int x = x2 / 2;
      if (0 <= min(x, y) && max(x, y) < n) {
        g[pos].push_back(neg);
      }      
    }
  }
  
  for (iter = 0; iter < 2 * n - 1; ++iter) {
    dfs(iter);
  }
  
  forn (neg, 2 * n - 1) {
    int pos = mt[neg];
    if (pos == -1) {
      continue;
    }
    int y2 = pos + neg - (n - 1);
    int x2 = pos - neg + (n - 1);
    used[x2 / 2][y2 / 2] = true;
  }
  
  return used;
}
  
void solve() {
  int n, m;
  cin >> n >> m;
  vector<vector<bool>> cross(n, vector<bool>(n, false));
  vector<vector<bool>> plus(n, vector<bool>(n, false));
  
  while (m--) {
    char c;
    int x, y;
    cin >> c >> x >> y;
    --x, --y;
    if (c == 'x' || c == 'o') cross[x][y] = true;
    if (c == '+' || c == 'o') plus[x][y] = true;
  }
  
  auto ans_cross = solve_lines(n, cross);
  auto ans_plus = solve_diagonals(n, plus);
  
  
  int score = 0;
  vector<pair<char, pair<int, int>>> ans;
  
  auto pair_to_char = [](bool cross, bool plus) {
    if (cross && plus) return 'o';
    if (cross) return 'x';
    if (plus) return '+';
    return '.';
  };
  
  forn (i, n) {
    forn (j, n) {
      score += ans_cross[i][j];
      score += ans_plus[i][j];
      char old_char = pair_to_char(cross[i][j], plus[i][j]);
      char new_char = pair_to_char(ans_cross[i][j], ans_plus[i][j]);
      if (old_char != new_char) {
        ans.push_back({new_char, {i + 1, j + 1}});
      }
    }
  }
  
  cout << score << ' ' << sz(ans) << endl;
  for (auto e : ans) {
    cout << e.first << ' ' << e.second.first << ' ' << e.second.second << endl;
  }
}

int main() {
  freopen(PATH"in.txt", "r", stdin);
  freopen(PATH"out.txt", "w", stdout);

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;
  forn (i, t) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }  
  
  cout.flush();
  return 0;
}