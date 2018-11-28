#include <bits/stdc++.h>

#ifdef LOCAL_COMP
#define VA_NUM_ARGS(...) VA_NUM_ARGS_IMPL(0, __VA_ARGS__, 5, 4, 3, 2, 1)
#define VA_NUM_ARGS_IMPL(_0, _1, _2, _3, _4, _5, N, ...) N

#define macro_dispatcher(macro, ...) \
  macro_dispatcher_(macro, VA_NUM_ARGS(__VA_ARGS__))
#define macro_dispatcher_(macro, nargs) macro_dispatcher__(macro, nargs)
#define macro_dispatcher__(macro, nargs) macro##nargs

#define debug(...) macro_dispatcher(debug, __VA_ARGS__)(__VA_ARGS__)

#define debug1(a) cout << #a << " = " << (a) << endl
#define debug2(a, b) \
  cout << #a << " = " << (a) << "  " << #b << " = " << (b) << endl
#define debug3(a, b, c)                                                  \
  cout << #a << " = " << (a) << "  " << #b << " = " << (b) << "  " << #c \
       << " = " << (c) << endl
#define debug4(a, b, c, d)                                               \
  cout << #a << " = " << (a) << "  " << #b << " = " << (b) << "  " << #c \
       << " = " << (c) << "  " << #d << " = " << (d) << endl
#else
#define debug(...)
#endif

using namespace std;

typedef long long T;

class Solution {
 public:

  void solve_impl() {
    int n, p; scanf("%d%d", &n, &p);
    vector<int> a(n), c(p, 0);
    for (int i = 0; i < n; ++i) {
      scanf("%d", &a[i]);
      a[i] %= p;
      c[a[i]]++;
    }

    int ret = 0;
    ret += c[0];

    if (p == 2) {
      ret += (c[1] + 1) / 2;
    } else if (p == 3) {
      while (c[1] && c[2]) {
        ++ret;
        --c[1]; --c[2];
      }

      int mod = 0;
      while (c[1] || c[2]) {
        if (mod == 0) {
          ++ret;
        }
        if (c[1]) {
          mod = (mod + 3 - 1) % 3;
          --c[1];
        } else {
          mod = (mod + 3 - 2) % 3;
          --c[2];
        }
      }
    } else if (p == 4) {
      while (c[2] >= 2) {
        ++ret;
        c[2] -= 2;
      }

      while (c[1] && c[3]) {
        ++ret;
        --c[1]; --c[3];
      }

      int mod = 0;
      if (c[2]) {
        mod = 2;
        ++ret;
      }

      while (c[1]) {
        if (mod == 0) {
          ++ret;
        }
        mod = (mod + 4 - 1) % 4;
        --c[1];
      }

      while (c[3]) {
        if (mod == 0) {
          ++ret;
        }
        mod = (mod + 4 - 3) % 4;
        --c[3];
      }
    } else {
      assert(false);
    }

    printf("%d", ret);
  }

  void solve_codejam(int t) {
    printf("Case #%d: ", t + 1);
    solve_impl();
    printf("\n");
    fflush(stdout);
  }
};

int main() {
#ifdef LOCAL_COMP
  freopen("a.txt", "r", stdin);
#endif

#if 0
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  for (int n; cin >> n;) {
    // cout << solve(n) << endl;
    Solution solution;
    solution.solve_codejam(n);
//    cout << solution.solve(n) << endl;
    //    while(n--) {
    //      solve(n);
    //    }
    //    if (solve(n)) {
    //      cout << "YES" << endl;
    //    } else {
    //      cout << "NO" << endl;
    //    }
  }
  cout.flush();
#else
  int n;
  while (scanf("%d", &n) == 1) {
    for (int t = 0; t < n; ++t) {
      Solution solution;
      solution.solve_codejam(t);
    }
  }
#endif
  return 0;
}
