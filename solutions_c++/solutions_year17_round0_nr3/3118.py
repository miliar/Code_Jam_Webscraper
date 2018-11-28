#include <bits/stdc++.h>

using namespace std;
using ULL = unsigned long long;

ULL T, N, K;
ULL solve(ULL n, ULL k) {
  if (k == 1) return n - 1;
  else {
    if (k % 2 == 0) return solve(n / 2, k / 2);
    else return solve(n / 2 - (n % 2 == 0), k / 2);
  }
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> N >> K;
    ULL ret = solve(N, K);
    ULL a, b;
    if (ret % 2 == 0) {
      cout << "Case #" << t << ": " << ret/2 << " " << ret/2 << endl;
    } else {
      cout << "Case #" << t << ": " << (ret+1)/2 << " " << (ret-1)/2 << endl;
    }
  }
  return 0;
}
