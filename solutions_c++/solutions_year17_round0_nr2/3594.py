#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  ll t;
  cin >> t;
  vector<ll> pow10(19);
  pow10[0] = 1;
  for (int i = 1; i < 19; ++i) {
    pow10[i] = pow10[i - 1] * 10;
  }
  for (int q = 0; q < t; ++q) {
    ll n;
    cin >> n;
    cout << "Case #" << q + 1 << ": ";
    ll mypos = 0;
    for (int i = 0; i < 18; ++i) {
      if (n / pow10[i] % 10 < n / pow10[i + 1] % 10) {
        n -= pow10[i + 1];
        while (mypos <= i) {
          n -= pow10[mypos] * (n / pow10[mypos] % 10);
          n += pow10[mypos] * 9;
          mypos++;
        }
      }
    }
    cout << n << endl;
  }
  return 0;
}