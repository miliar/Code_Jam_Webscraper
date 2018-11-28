#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long li;
typedef long double ld;

const int N = 100500;

li n;
ld d;
ld k[N], s[N];

bool check(ld v) {
  for (int i = 0; i < n; ++i) {
    if(s[i] >= v)
      continue;
    ld rv = v - s[i];
    ld ct = k[i] / rv;
    ld cp = v * ct;
    if (cp < d)
      return false;
  }
  return true;
}

int main() {
  int tests;
  cin >> tests;

  cout.precision(10);
  cout << fixed;

  for (int test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";

    cin >> d >> n;
    for (int i = 0; i < n; ++i)
      cin >> k[i] >> s[i];

    ld lf = 0, rg = static_cast<ld>(1e15);
    for (int i = 0; i < 100; ++i) {
      ld mid = (lf + rg) / 2;
      if (check(mid)) {
        lf = mid;
      } else {
        rg = mid;
      }
    }

    cout << lf << endl;
  }
  return 0;
}