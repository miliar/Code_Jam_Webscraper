#include <iostream>
#include <math.h> 
using namespace std;

#define ll long long

ll ceil_log2(ll x) {
  x -= 1;
  for(ll i = 0;; i++) {
    x >>= 1;
    if(x == 0) {
      return(i+1);
    }
  }
}

void ans(ll n, ll k, ll& max, ll& min) {
  if(k == 1) {
    max = (n-1)/2 + (n-1)%2;
    min = (n-1)/2;
    return;
  }
  ll x = 1ll << int(ceil_log2(k+1));
  ll total = n - (x - 1);
  ll small = total / x;
  ll n_big = total - small * x;
  ll y = (1ll << (int(ceil_log2(k+1))-1)) - 1;
  ll idx = k - y;
  max = (idx <= n_big)? (small+1) : small;
  min = (((x/2) + idx) <= n_big)? (small+1) : small;
  //cout << "===============" << endl;
  //cout << "x : " << x << endl;
  //cout << "total : " << total << endl;
  //cout << "small : " << small << endl;
  //cout << "n_big : " << n_big << endl;
  //cout << "y : " << y << endl;
  //cout << "idx : " << idx << endl;
  //cout << "===============" << endl;
}

int main() {
  int nc;
  cin >> nc;
  for(int i = 0; i < nc; i++) {
    ll n, k;
    ll max, min;
    cin >> n >> k;
    ans(n, k, max, min);
    cout << "Case #" << (i+1) << ": " << max << " " << min << endl;
  }

  return 0;
}
