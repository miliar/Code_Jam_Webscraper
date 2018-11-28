#include <bits/stdc++.h>
#define vec vector
#define sz(c) int(c.size())
#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define DOWN(i, a, b) for(int i = (a) - 1; i >= (b); --i)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vec<int> vi;

int solve(int N, int P, vec<vec<pii>> s) {
  int result = 0;
  FOR(i, 0, P) {
    FOR(j, 0, N) {
      if (s[j].empty()) {
        return result;
      }
    }
    int t = (int)1e9;
    FOR(j, 0, N) {
      int l, r;
      tie(l, r) = s[j][sz(s[j]) - 1];
      t = min(t, r);
    }
    //cerr << t << endl;
    bool good = true;
    FOR(j, 0, N) {
      int l, r;
      tie(l, r) = s[j][sz(s[j]) - 1];
      if (l > t) {
        good = false;
        break;
      }
    }
    if (good) {
      result += 1;
      FOR(j, 0, N) {
        s[j].pop_back();
      }
    } else {
      FOR(j, 0, N) {
        int l, r;
        tie(l, r) = s[j][sz(s[j]) - 1];
        if (r == t) {
          s[j].pop_back();
        }
      }
    }
  }
  return result;
}

void solve_testcase(int testcase) {
  cout << "Case #" << testcase << ": ";
  int N, P;
  cin >> N >> P;
  vec<int> R(N);
  FOR(i, 0, N) {
    cin >> R[i];
  }
  vec<vi> Q(N, vi(P));
  FOR(i, 0, N) {
    FOR(j, 0, P) {
      cin >> Q[i][j];
    }
    sort(Q[i].rbegin(), Q[i].rend());
  }
  vec<vec<pii>> s(N);
  FOR(i, 0, N) {
    FOR(j, 0, P) {
      int l = (10 * Q[i][j] + 11 * R[i] - 1) / (11 * R[i]);
      int r = (10 * Q[i][j]) / (9 * R[i]);
      //cerr << i << " " << j << " " << l << " " << r << endl;
      if (l <= r) {
        s[i].emplace_back(l, r);
      }
    }
  }
  cout << solve(N, P, s) << endl;
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
