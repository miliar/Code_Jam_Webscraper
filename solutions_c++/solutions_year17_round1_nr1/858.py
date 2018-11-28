#include <algorithm>
#include <cassert>
#include <cfloat>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#define FOR(i,k,n) for (int (i)=(k); (i)<(n); ++(i))
#define rep(i,n) FOR(i,0,n)
#define all(v) begin(v), end(v)
#define debug(x) cerr<< #x <<": "<<x<<endl
#define debug2(x,y) cerr<< #x <<": "<< x <<", "<< #y <<": "<< y <<endl

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<ll> vll;
typedef vector<vector<ll> > vvll;
typedef deque<bool> db;
template<class T> using vv=vector<vector< T > >;

int testcase;
vector<vector<string> > ans;
void output_ans() {
  rep (i, testcase) {
    cout << "Case #" << i+1 << ":\n";

    int r = ans[i].size();
    rep (j, r) {
      cout << ans[i][j] << "\n";
    }
  }
  exit(0);
}

int r, c;
vector<string> board;

void get_input() {
  // Do not forget initialization or clear
  cin >> r >> c;
  board.resize(r);
  rep (i, r) {
    cin >> board[i];
  }
}

int INF = 1e9;

void solve(int index_testcase) {
  int start = INF;
  rep (i, r) {
    char last_char = '$';
    rep (j, c) {
      if (board[i][j] =='?') {
        start = min(start, j);
        continue;
      }
      last_char = board[i][j];
      FOR (k, start, j) {
        board[i][k] = last_char;
      }
      start = INF;
    }
    if (last_char != '$') {
      FOR (k, start, c) {
        board[i][k] = last_char;
      }
    }
  }

  for (int i = 1; i < r; ++i) {
    if (board[i][0] == '?') {
      rep (j, c) {
        board[i][j] = board[i-1][j];
      }
    }
  }
  for (int i = r-2; i >= 0; --i) {
    if (board[i][0] == '?') {
      rep (j, c) {
        board[i][j] = board[i+1][j];
      }
    }
  }
  ans[index_testcase] = board;
}

int main() {
  cin >> testcase;
  ans.resize(testcase);

  rep (i, testcase) {
    get_input();
    //ans[i] = solve();
    solve(i);
  }

  output_ans();

  return 0;
}
