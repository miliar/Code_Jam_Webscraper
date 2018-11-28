#include <iostream>
#include <stack>
using namespace std;
long long n, k;
int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    printf("Case #%d: ", t);
    cin >> n >> k;
    while (k != 1) {
      if (k & 1) n = n - 1 - (n >> 1);
      else n >>= 1;
      k >>= 1;
    }
    printf("%lld %lld\n", (n >> 1), n - 1 - (n >> 1));
  }
  return 0;
}
