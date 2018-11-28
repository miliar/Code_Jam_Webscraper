#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

bool is_tidy(ll N) {
  ll last = 9;
  for (ll x = N; x; x /= 10) {
    if (x % 10 > last)
      return false;
    last = x % 10;
  }
  return true;
}

ll solve2(ll N, int digit) {
  if (N < 10) {
    return min(N, (ll)digit);
  }
  if (is_tidy(N)) {
    return N;
  }
  return solve2(N/10-1, 9) * 10 + 9;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    ll N;
    cin >> N;
    ll ans = solve2(N, 9);
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
}
