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
  bool is_tidy(int n) {
    std::string s = to_string(n);
    sort(s.begin(), s.end());
    return n == stoi(s); // haha
  }

  int solve_impl() {
    int n; scanf("%d", &n);
    for (int i = n; i >= 0; --i){
      if (is_tidy(i)) {
        return i;
      }
    }
  }

  void solve(int n) {
    for (int i = 0; i < n; ++i) {
      printf("Case #%d: %d\n", i + 1, solve_impl());
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
