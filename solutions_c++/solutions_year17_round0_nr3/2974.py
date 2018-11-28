#include <iostream>
#include <stdio.h>
using namespace std;

long long dp(long long n, long long k, bool is_max)
{
  if (k == 1) {
    if (is_max)
      return n / 2;
    else
      return (n - 1) / 2;
  } else {
    if (n % 2 == 1) return dp((n - 1) / 2, k / 2, is_max);
    if (k % 2 == 0) return dp(n / 2, k / 2, is_max);
    return dp(n / 2 - 1, k / 2, is_max);
  }
}

int main()
{
  int numTests;
  cin >> numTests;
  for (int test = 0; test < numTests; test++) {
    long long N, K;
    cin >> N >> K;
    cout << "Case #" << test + 1 << ": " << dp(N, K, true) << " " << dp(N, K, false) << endl;
  }
}
