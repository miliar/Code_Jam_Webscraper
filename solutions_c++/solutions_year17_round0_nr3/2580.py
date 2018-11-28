#include <iostream>
#include <string>
#include <vector>
#include <map>
#define ll long long
using namespace std;

int main() {
  int tk;
  cin >> tk;
  for (int tk1 = 1; tk1 <= tk; tk1++) {
    ll n, k;
    cin >> n >> k;
    k--;
    map<ll, ll> mp;
    mp[n] = 1;
    while (k) {
      // cout << "k = " << k << endl;
      ll val = mp.rbegin()->first;
      ll cnt = mp.rbegin()->second;
      if (k >= cnt) {
        mp[(val - 1) / 2] += cnt;
        mp[val / 2] += cnt;
        mp.erase(val);
        k -= cnt;
      } else {
        break;
      }
    }
    cout << "Case #" << tk1 << ": ";
    ll val = mp.rbegin()->first;
    cout << val / 2 << " " << (val - 1) / 2 << endl;
  }
  return 0;
}
