#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int T;

int main () {

  cin >> T;

  for(int tc=1;tc<=T;tc++) {
    printf("Case #%d: ",tc);

    ll n, k;
    cin >> n >> k;
    ll b = 1;
    while((b * 2) <= k) {
      b = b * 2;
    }

    ll x = (n - b + 1) / b;
    ll y = x + 1;
    ll yc = (n - b + 1) % b;

    ll d;
    if (k - b + 1 <= yc) d = y;
    else d = x;
    cout << d / 2 << ' ' << (d-1)/2 << endl;

  }

  return 0;
}