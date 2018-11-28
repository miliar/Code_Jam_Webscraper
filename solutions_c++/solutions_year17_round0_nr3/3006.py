#include<bits/stdtr1c++.h>
using namespace std;

typedef long long ll;

int T;
ll N, K;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N >> K;
    ll a, b;
    ll ca, cb;
    a = N;
    b = N+1;
    ca = 1;
    cb = 0;
    while (K > ca + cb) {
      K -= ca + cb;
      a--;
      b--;
      if (a % 2) {
        a = a/2;
        b = b/2;
        cb += ca + cb;
      } else {
        a = a/2;
        b = b/2+1;
        ca += ca + cb;
      }
    }
    cout << "Case #" << t << ": ";
    if (K > cb) {
      a--;
      cout << (a - a/2) << " " << a/2 << endl;
    } else {
      b--;
      cout << (b - b/2) << " " << b/2 << endl;
    }
  }

  return 0;
}
