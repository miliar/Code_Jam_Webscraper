#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>

#define REP(a,b) for(int a=0;a<(b);a++)
#define PER(a,b) for(int a=(b)-1;a>=0;a--)
#define ll long long

using namespace std;

int T;

int main() {
  cin >> T;
  assert(cin);

  REP(tcase, T) {
    ll N, K;
    assert(cin >> N);
    assert(cin >> K);
    ll max, min, a = 1, b = 0;
    ll val = N;
    ll lvl = 0;
    for (ll i = 1; (2 * i - 1) < K; i *= 2) {
      if (val % 2) {
        a *= 2;
        a += b;
      }
      else {
        b *= 2;
        b += a;
      }
      val /= 2;
      lvl = 2 * i - 1;
    }

    if ((K - lvl) <= a) {
      min = (val - 1) / 2;
      max = min + (val - 1) % 2;
    }
    else {
      min = (val - 2) / 2;
      max = min + (val - 2) % 2;
    }

    cout << "Case #" << tcase + 1 << ": " << max << " " << min << endl;
  }

  return 0;
}
