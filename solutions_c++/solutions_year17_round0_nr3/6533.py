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

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;

typedef long long T;

template<typename T>
using ordered_set = __gnu_pbds::tree<
  T,
  __gnu_pbds::null_type,
  less<T>,
  __gnu_pbds::rb_tree_tag,
  __gnu_pbds::tree_order_statistics_node_update>;


struct Segment {
  int left = -1, right = -1;
  Segment(int l, int r) : left(l), right(r) {}

  int center() const {
    return (left + right) / 2;
  }

  int min_diff() const {
    return min(center() - left - 1, right - center() - 1);
  }

  int max_diff() const {
    return max(center() - left - 1, right - center() - 1);
  }
};

bool operator<(const Segment &a, const Segment &b) {
  return std::make_tuple(a.min_diff(), a.max_diff(), a.center()) <
         std::make_tuple(b.min_diff(), b.max_diff(), b.center());
}

class Solution {
 public:  
  void solve_impl() {
    int n, k; scanf("%d%d", &n, &k);

    priority_queue<Segment> q;
    auto try_emplace = [&q](int left, int right) {
      Segment s(left, right);
      if (right - left > 1) {
        q.push(s);
      }
    };

    q.emplace(0, n + 1);

    for (int iter = 0; iter < k - 1; ++iter) {
      Segment s = q.top(); q.pop();

      try_emplace(s.left, s.center());
      try_emplace(s.center(), s.right);
    }

    const Segment &last = q.top();
    cout << last.max_diff() << " " << last.min_diff();
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
  freopen("c.txt", "r", stdin);
#endif

#if 0
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  for (T n; cin >> n;) {
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
