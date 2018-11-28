#include <iostream>
#include <string>
#include <cassert>
#include <set>
#include <map>

// FIXME: Too low for large!

using namespace std;
typedef long long ll;

int main() {
  ll T;
  cin >> T;
  for(ll cas=1; cas<=T; cas++) {
    ll n, k;
    cin >> n >> k;
    map<ll, ll> I;
    I[n] = 1;
    ll i = 0;
    ll a = 0;
    ll b = 0;
    while(i<k) {
      /*cout << i << " [";
      for(auto& kv : I) {
        cout << kv.first << ":" << kv.second << " ";
      }
      cout << "]" << endl;*/
      assert(I.size() >= 1);
      auto it = I.end();
      it--;
      ll len = it->first;
      assert(len >= 1);
      assert(it->second >= 1);
      a = (len-1)/2;
      b = len-1-a;
      ll amt = min(it->second, k-i);
      if(a >= 1) {
        I[a] += amt;
      }
      if(b >= 1) {
        I[b] += amt;
      }
      if(I[len] == amt) {
        I.erase(it);
      } else {
        I[len] -= amt;
      }
      i += amt;
    }
    cout << "Case #" << cas << ": " << max(a,b) << " " << min(a,b) << endl;
  }
}
