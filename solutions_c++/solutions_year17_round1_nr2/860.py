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
#define debug(x) //cerr<< #x <<": "<<x<<endl
#define debug2(x,y) //cerr<< #x <<": "<< x <<", "<< #y <<": "<< y <<endl

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
vi ans;
void output_ans() {
  rep (i, testcase) {
    printf("Case #%d: ", i+1);
    printf("%d", ans[i]);

    // output ans
    // e.g.) printf("%d\n", ans[i]);

    printf("\n");
  }
  exit(0);
}

int n, p;
vi r;
vvi q;

void get_input() {
  // Do not forget initialization or clear
  cin >> n >> p;
  r.resize(n);
  rep (i, n) {
    cin >> r[i];
  }
  q.assign(n, vi(p, 0));
  rep (i, n) {
    rep (j, p) {
      cin >> q[i][j];
    }
    sort(all(q[i]));
  }
}

int INF = 1e9;

bool match(vi &a, vi &b) {
  if (a[0] > a[1] || b[0] > b[1]) {
    return false;
  }
  if (a[1] < b[0] || b[1] < a[0]) {
    return false;
  }
  debug2(a[0], a[1]);
  debug2(b[0], b[1]);
  return true;
}

void solve(int index_testcase) {
  vv<vi> possible_minmax(n, vvi(p, vi(2, 0)));
  rep (i, n) {
    int def = r[i];
    rep (j, p) {
      possible_minmax[i][j][0] = ((q[i][j] * 10 + 10) / 11 + def - 1) / def;
      possible_minmax[i][j][1] = ((q[i][j] * 10) / 9) / def;
      debug2(possible_minmax[i][j][0], possible_minmax[i][j][1]);
    }
  }

  int pans = 0;
  vi used_max(n, p);
  for (int j = p-1; j >= 0; --j) {
    vi new_used_max = used_max;
    bool flag = true;
    if (n == 1) {
      vi b = {-1, 1000005};
      if (match(possible_minmax[0][j], b)) {
        pans += 1;
      }
      continue;
    }
    FOR (i, 1, n) {
      if (used_max[i] == 0) {
        flag = false;
        break;
      }
      for (int k = used_max[i] - 1; k >= 0; --k) {
        if (match(possible_minmax[i][k], possible_minmax[0][j])) {
          new_used_max[i] = k;
          break;
        } else if (k == 0) {
          flag = false;
          i = n;
          break;
        }
      }
    }
    if (flag) {
      swap(used_max, new_used_max);
      pans += 1;
    }
    debug(used_max[1]);
  }
  ans[index_testcase] = pans;
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
