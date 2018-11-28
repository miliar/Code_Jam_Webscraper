#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <iomanip>
#include <stack>
#include <sstream>
#include <queue>
#include <set>
#include <functional>
#include <ctime>
#include <utility>

#define endl '\n'
#define eps 1e-9
#define ll long long int

using namespace std;

int main() {
  #ifndef TEST
  	ios_base::sync_with_stdio(false);
  	cin.tie(0);
  #endif
  int T;
  cin >> T;
  // Remember to handle 1 if necessary
  for (int Case = 1; Case <= T; Case++) {
    ll n, k;
    cin >> n >> k;
    // {number, value}
    pair<ll, ll> cur_low = {1, n};
    pair<ll, ll> cur_high = {0, -1};
    pair<ll, ll> next_low, next_high;
    ll cur_processed = 0;
    ll cur_power = 1;
    for (; cur_processed + cur_power <= k-1; cur_processed += cur_power, cur_power <<= 1) {
      cur_high.second--;
      cur_low.second--;
      next_low = {cur_low.first, cur_low.second/2};
      next_high = {0, -1};
      if (cur_low.second%2) {
        next_high = {cur_low.first, cur_low.second/2+1};
      }
      else {
        next_low.first <<= 1;
      }
      if (cur_high.first > 0) {
        if (cur_high.second%2) {
          next_low.first += cur_high.first;
          next_high = {cur_high.first, cur_high.second/2+1};
        }
        else {
          next_high.first += cur_high.first*2;
        }
      }
      cur_high = next_high;
      cur_low = next_low;
    }
    ll dif = k - cur_processed;
    ll small, high;
    cur_high.second--;
    cur_low.second--;
    if (dif <= cur_high.first) {
      small = cur_high.second/2;
      high = small + cur_high.second%2;
    }
    else {
      small = cur_low.second/2;
      high = small + cur_low.second%2;
    }
    cout << "Case #" << Case << ": " << high << ' ' << small << '\n';
  }
}
