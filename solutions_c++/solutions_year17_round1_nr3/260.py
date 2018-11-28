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


class Solution {
 public:  
  void solve_impl() {
    int health_dragon, attack_dragon;
    int health_knight, attack_knight;
    int buff, debuff;
    cin >> health_dragon >> attack_dragon >> health_knight >> attack_knight;
    cin >> buff >> debuff;

    const int INF = 1e9;
    vector<vector<vector<vector<int> > > > dist(110,
                 vector<vector<vector<int> > >(110,
                        vector<vector<int> >(110,
                               vector<int>(110, INF))));


    dist[health_dragon][attack_dragon][health_knight][attack_knight] = 0;
    queue<tuple<int, int, int, int> > q;

    auto try_emplace = [&](int h_d, int a_d, int h_k, int a_k, int d) {
      h_d = max(h_d, 0);
      a_d = max(a_d, 0);
      h_k = max(h_k, 0);
      a_k = max(a_k, 0);
      if (h_d == 0 || h_d >= dist.size()) return;
      if (a_d >= dist[0].size()) return;
      if (h_k >= dist[0][0].size()) return;
      if (a_k >= dist[0][0][0].size()) return;

      if (h_k > 0) {
        h_d -= a_k;
        if (h_d <= 0) {
          return;
        }
      }

      if (dist[h_d][a_d][h_k][a_k] > d) {
        dist[h_d][a_d][h_k][a_k] = d;
        q.emplace(h_d, a_d, h_k, a_k);
      }
    };

    q.emplace(health_dragon, attack_dragon, health_knight, attack_knight);

    int ITERS = 1e6;

    while (!q.empty() && ITERS-- > 0) {
      auto v = q.front(); q.pop();
      const int h_d = get<0>(v);
      const int a_d = get<1>(v);
      const int h_k = get<2>(v);
      const int a_k = get<3>(v);

      const int d = dist.at(h_d).at(a_d).at(h_k).at(a_k);

      if (h_k <= 0) {
        cout << d;
        return;
      }

      try_emplace(h_d, a_d, h_k - a_d, a_k, d + 1);
      try_emplace(h_d, a_d + buff, h_k, a_k, d + 1);
      try_emplace(health_dragon, a_d, h_k, a_k, d + 1);
      try_emplace(h_d, a_d, h_k, a_k - debuff, d + 1);
    }

    cout << "IMPOSSIBLE";
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
