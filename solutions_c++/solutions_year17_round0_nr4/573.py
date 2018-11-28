#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <set>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

vector<vector<int>> E;
vector<bool> matched;
vector<int> dad;
vector<int> bio;
int cookie;
  
bool match(int x) {
  if (x == -1) return true;
  if (bio[x] == cookie) return false;
  bio[x] = cookie;
  for (int y: E[x])
    if (match(dad[y])) {
      dad[y] = x;
      return true;
    }
  return false;
}
  
  
vector<int> max_matching(vector<vector<bool>> adj, set<int> matched_left, set<int> matched_right) {
  int n = adj.size();
  int m = adj[0].size();
  E.resize(n);
  REP(i, n) {
    E[i].clear();
    if (matched_left.count(i)) continue;
    REP(j, m) if (adj[i][j] && !matched_right.count(j)) E[i].push_back(j);
  }
  
  dad = vector<int>(m, -1);
  bio = vector<int>(n, 0);
  matched = vector<bool>(n, false);

  REP(i, n) {
    cookie++;
    matched[i] = match(i);
  }    
  return dad;
}

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int N, M;
    scanf("%d %d", &N, &M);

    vector<vector<bool>> plus(N, vector<bool>(N, false));
    vector<vector<bool>> x(N, vector<bool>(N, false));

    vector<vector<char>> in(N, vector<char>(N, '.'));
    REP(i, M) {
      char s[10];
      int r, c;
      scanf("%s %d %d", s, &r, &c); --r, --c;
      in[r][c] = s[0];
      
      if (s[0] == '+' || s[0] == 'o') {
        plus[r][c] = true;
      }
      if (s[0] == 'x' || s[0] == 'o') {
        x[r][c] = true;
      }
    }

    // x
    vector<vector<bool>> adjx(N, vector<bool>(N, true));
    set<int> rows_x, cols_x;
    REP(i, N) REP(j, N) {
      if (x[i][j]) {
        rows_x.insert(i);
        cols_x.insert(j);
      }
    }
    vector<int> xs = max_matching(adjx, rows_x, cols_x);
    REP(j, N)
      if (dad[j] != -1) x[dad[j]][j] = true;
    
    // +
    vector<vector<bool>> adjplus(2*N, vector<bool>(2*N, false));
    REP(i, N) REP(j, N) adjplus[i+j][i-j+N] = true;
    set<int> first_diag_plus, second_diag_plus;
    REP(i, N) REP(j, N) {
      if (plus[i][j]) {
        first_diag_plus.insert(i+j);
        second_diag_plus.insert(i-j+N);
      }
    }
    vector<int> pluses = max_matching(adjplus, first_diag_plus, second_diag_plus);
    REP(j, 2*N)
      if (dad[j] != -1) {
        int r = (j-N+dad[j]) / 2;
        int c = dad[j] - r;
        assert(0 <= r && r < N);
        assert(0 <= c && c < N);
        plus[r][c] = true;
      }
    
    vector<vector<char>> out = in;
    int score = 0, models = 0;
    REP(i, N) REP(j, N) {
      if (x[i][j] && plus[i][j]) {
        out[i][j] = 'o';
        score += 2;
      } else if (x[i][j]) {
        out[i][j] = 'x';
        score++;
      } else if (plus[i][j]) {
        out[i][j] = '+';
        score++;
      }

      if (out[i][j] != in[i][j]) models++;
    }
    
    printf("Case #%d: ", tp);
    printf("%d %d\n", score, models);
    REP(i, N) REP(j, N) {
      if (out[i][j] != in[i][j]) {
        printf("%c %d %d\n", out[i][j], i+1, j+1);
      }
    }
  }
  return 0;
}

