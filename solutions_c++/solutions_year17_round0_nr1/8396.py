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
  int convert_mask(const string &s) {
    int ret = 0;
    for (int i = 0; i < s.length(); ++i) {
      if (s[i] == '+') {
        ret += (1 << i);
      }
    }
    return ret;
  }

  int revert_mask(int mask, int start, int end) {
    for (int i = start; i <= end; ++i) {
      mask ^= (1 << i);
    }
    return mask;
  }

  void solve_impl() {
    string s; cin >> s;
    const int n = static_cast<int>(s.length());
    int k; cin >> k;

    vector<int> dist(1 << n, -1);
    queue<int> q;
    const int start_mask = convert_mask(s);
    q.emplace(start_mask);
    dist[start_mask] = 0;

    const int target_mask = (1 << n) - 1;

    while (!q.empty()) {
      const int v = q.front(); q.pop();

      if (v == target_mask) {
        break;
      }

      for (int i = 0; i + k - 1 < n; ++i) {
        const int to = revert_mask(v, i, i + k - 1);
        if (dist[to] == -1) {
          dist[to] = dist[v] + 1;
          q.emplace(to);
        }
      }
    }

    const int ret = dist[target_mask];
    if (ret == -1) {
      cout << "IMPOSSIBLE";
    } else {
      cout << ret;
    }
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
  freopen("a.txt", "r", stdin);
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
