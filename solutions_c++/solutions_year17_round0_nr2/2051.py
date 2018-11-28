#include <bits/stdc++.h>

using namespace std;

unsigned long long pow10(unsigned long long n) {
  return n == 0 ? 1 : 10 * pow10(n - 1);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  unsigned long long N, n, curr, p;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> N;
    n = N;
    curr = n % 10, p = 1;
    n /= 10;
    while (n) {
      if (n % 10 > curr) {
        N = N - N % pow10(p) - 1;
        n = N / pow10(p);
      }
      curr = n % 10;
      n /= 10;
      ++p;
    }
    cout << N << '\n';
  }
}