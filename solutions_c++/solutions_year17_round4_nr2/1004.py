#include <iostream>
#include <algorithm>

#ifdef ALGO_DEBUG
#include "../test/debug.cpp"
#else

#define TRACE(message)
#define TRACE_LINE(message)
#define ASSERT(expr)
#define UNIT_TESTS()

#endif

void unit_tests() {
}

void solve(int t) {
  int N, C, M;
  std::cin >> N >> C >> M;
  int tickets[C][N];
  for(int i = 0; i < C; ++i)
    for(int j = 0; j < N; ++j) tickets[i][j] = 0;
  for(int i = 0; i < M; ++i) {
    int p, c;
    std::cin >> p >> c;
    tickets[c - 1][p - 1]++;
  }
  int rides = 0, promotions = 0;
  for(int i = 0; i < N; ++i) {
    if(tickets[0][i] > 0) {
      for(int j = 0; j < N; ++j) {
        if(i == j) continue;
        if(tickets[0][j] == 0) continue;
        if(tickets[1][j] == 0) continue;
        int match = std::min(tickets[0][i], tickets[1][j]);
        tickets[0][i] -= match;
        tickets[1][j] -= match;
        rides += match;
        if(tickets[0][i] == 0) break;
      }
    }
    if(tickets[0][i] > 0) {
      for(int j = 0; j < N; ++j) {
        if(i == j) continue;
        if(tickets[1][j] == 0) continue;
        int match = std::min(tickets[0][i], tickets[1][j]);
        tickets[0][i] -= match;
        tickets[1][j] -= match;
        rides += match;
        if(tickets[0][i] == 0) break;
      }
    }
  }
  rides += tickets[0][0] + tickets[1][0];
  for(int i = 1; i < N; ++i) {
    if(tickets[0][i] > 0 || tickets[1][i] > 0) {
      rides += std::max(tickets[0][i], tickets[1][i]);
      promotions += std::min(tickets[0][i], tickets[1][i]);
    }
  }
  std::cout << "Case #" << t << ": " << rides << " " << promotions << "\n";
}

int main() {
  UNIT_TESTS();
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) solve(t);
  return 0;
}
