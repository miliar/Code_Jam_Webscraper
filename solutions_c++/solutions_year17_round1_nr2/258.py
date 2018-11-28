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
  bool check_quantity(int quantity, int req) {
    int left = 90 * req, right = 110 * req;
    quantity *= 100;
    return quantity >= left && quantity <= right;
  }



  void solve_impl() {
    int n, p; scanf("%d%d", &n, &p);
    vector<int> r(n);
    for (int i = 0; i < n; ++i) {
      scanf("%d", &r[i]);
    }
    vector<vector<int> > q(n, vector<int>(p));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        scanf("%d", &q[i][j]);
      }
      sort(q[i].begin(), q[i].end());
    }

    int max_count = 2e6;
    for (int i = 0; i < n; ++i) {
//      max_count = min(max_count, 2 * (q[i].back() / r[i]));
    }

    int ret = 0;
    for (long long count = max_count; count > 0; --count) {
      bool good = true;
      for (int i = 0; i < n; ++i) {
        long long left = r[i] * 90ll * count, right = r[i] * 110ll * count;
        while (!q[i].empty()) {
          const int g = 100ll * q[i].back();
          if (g > right) {
            q[i].pop_back();
          } else {
            break;
          }
        }
        if (q[i].empty() || 100ll * q[i].back() < left) {
          good = false;
          break;
        }
      }

      if (!good) {
        continue;
      }

      ++ret;
      for (int i = 0; i < n; ++i) {
        q[i].pop_back();
      }
      ++count;
    }

    cout << ret;
  }

  void solve(int n) {
    for (int i = 0; i < n; ++i) {
      printf("Case #%d: ", i + 1);
      solve_impl();
      printf("\n");
      fflush(stdout);
    }
  }
};

int main() {
#ifdef LOCAL_COMP
  freopen("b.txt", "r", stdin);
#endif

#if 0
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  for (int n; cin >> n;) {
    // cout << solve(n) << endl;
    Solution solution;
    solution.solve(n);
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
    Solution solution;
    solution.solve(n);
  }
#endif

  return 0;
}
