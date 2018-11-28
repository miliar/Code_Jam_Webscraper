#include <bits/stdc++.h>
#define vec vector
#define sz(c) int(c.size())
#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define DOWN(i, a, b) for(int i = (a) - 1; i >= (b); --i)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vec<int> vi;

void solve_testcase(int testcase) {
  cout << "Case #" << testcase << ":\n";
  int R, C;
  cin >> R >> C;
  vec<string> a(R);
  FOR(i, 0, R) {
    cin >> a[i];
  }
  FOR(j, 0, C) {
    FOR(i, 1, R) {
      if (a[i][j] == '?') {
        a[i][j] = a[i - 1][j];
      }
    }
    DOWN(i, R - 1, 0) {
      if (a[i][j] == '?') {
        a[i][j] = a[i + 1][j];
      }
    }
  }
  FOR(i, 0, R) {
    FOR(j, 1, C) {
      if (a[i][j] == '?') {
        a[i][j] = a[i][j - 1];
      }
    }
    DOWN(j, C - 1, 0) {
      if (a[i][j] == '?') {
        a[i][j] = a[i][j + 1];
      }
    }
  }
  FOR(i, 0, R) {
    cout << a[i] << "\n";
  }
  flush(cout);
  FOR(i, 0, R) {
    FOR(j, 0, C) {
      assert(a[i][j] != '?');
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int testcases;
  cin >> testcases;
  FOR(testcase, 1, testcases + 1) {
    cerr << "Case " << testcase << "/" << testcases << endl;
    solve_testcase(testcase);
  }

  return 0;
}
