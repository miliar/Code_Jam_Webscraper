#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <array>
#include <set>
#include <queue>
#include <cstring>

#define all(x) x.begin(), x.end()
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define debug(x) std::cerr << "DEBUG: " << #x << " = " << x << std::endl

template<typename T>
inline void mn(T& x, const T& y) { x = std::min(x, y); }
template<typename T>
inline void mx(T& x, const T& y) { x = std::max(x, y); }
template<typename T>
inline int sz(const T& t) { return static_cast<int>(t.size()); }

int div_round_down(int x, int y) { return x / y; }
int div_round_up(int x, int y) { return (x + y - 1) / y; }

struct State {
  int hd;
  int hk;
  int ad;
  int ak;

  std::array<State, 4> next(int initial, int b, int d) const {
    std::array<State, 4> result;
    forn (i, 4) {
      State s = *this;
      switch (i) {
        case 0: s.hk = std::max(0, s.hk - s.ad); break;
        case 1: s.ad = std::min(s.ad + b, s.hk); break;
        case 2: s.hd = initial; break;
        case 3: s.ak = std::max(s.ak - d, 0); break;
      };
      if (s.hk > 0) {
        s.hd = std::max(0, s.hd - s.ak);
      }
      result[i] = s;
    }
    return result;
  }
};

bool operator<(const State& a, const State& b) {
  return memcmp(&a, &b, sizeof(State)) < 0;
}

void solve() {
  int hd, ad, hk, ak, b, d;
  std::cin >> hd >> ad >> hk >> ak >> b >> d;


  State initial = {hd, hk, ad, ak};
  std::map<State, int> dist;
  std::queue<State> queue;

  dist[initial] = 0;
  queue.push(initial);

  int ans = -1;
  while (ans == -1 && !queue.empty()) {
    State state = queue.front();
    queue.pop();
    int d_state = dist[state];
    for (State next : state.next(hd, b, d)) {
      if (next.hd == 0) {
        continue;
      }
      if (next.hk == 0) {
        ans = d_state + 1;
        break;
      }
      if (dist.emplace(std::pair<State, int>{next, d_state + 1}).second) {
        queue.push(next);
      }
    }
  }
  if (ans == -1) {
    std::cout << "IMPOSSIBLE" << std::endl;
  } else {
    std::cout << ans << std::endl;
  }

}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int t;
  std::cin >> t;
//  debug(t);
  for (int i = 0; i < t; ++i) {
    std::cout << "Case #" << (i + 1) << ": ";
    solve();
  }
  std::cout.flush();
  return 0;
}
