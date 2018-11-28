#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n;

void read() {
  cin >> n;
}

ll fun(ll n) {
  ll mem = n;
  ll b = n % 10;
  n /= 10;
  ll pw = 10;
  while (n) {
    ll a = n % 10;
    if (a > b) {
      return fun(n * pw - 1);
    }
    b = a;
    pw *= 10;
    n /= 10;
  }
  return mem;
}

void kill() {
  cout << fun(n) << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    kill();
    cerr << "Case #" << i << " done.\n";
  }
  return 0;
}
