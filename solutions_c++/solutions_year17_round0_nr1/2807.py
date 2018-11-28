#include <iostream>
#include <cstring>

void solve(int test_id) {
  std::string S;
  int K;
  std::cin >> S >> K;
  int a[S.size()];
  memset(a, 0, sizeof(a));
  int impossible = 0;
  int res = 0;

  for (int i = 0; i < (int)S.size(); ++i) {
    int flipped = 0;
    for (int j = std::max(0, i - K + 1); j < i; ++j)
      flipped ^= a[j];
    if (flipped) {
      if (S[i] == '+')
        S[i] = '-';
      else
        S[i] = '+';
    }
    if (S[i] == '-') {
      if (i + K <= (int)S.size()) {
        a[i] = 1;
        res += 1;
      }
      else {
        impossible = 1;
        break;
      }
    }
  }
  std::cout << "Case #" << test_id <<": ";
  if (impossible) {
    std::cout << "IMPOSSIBLE\n";
  }
  else {
    std::cout << res << "\n";
  }
}

int main() {
  int tests;
  std::cin >> tests;

  for (int i = 1; i <= tests; ++i) {
    solve(i);
  }
}
