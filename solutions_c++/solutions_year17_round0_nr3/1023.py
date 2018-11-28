#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

const string PROGRAM_NAME = "google";

int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    ll n, k;
    cin >> n >> k;

    priority_queue<ll> holes;
    map<ll, ll> multiplier;
    multiplier[n] = 1;
    holes.push(n);
    while (!holes.empty()) {
      ll hole = holes.top();
      holes.pop();
      ll l = hole / 2LL;
      ll r = (hole - 1LL) / 2LL;
      ll mul = multiplier[hole];
      map<ll, ll>::iterator it;
      if (l > 0) {
        it = multiplier.find(l);
        if (it == multiplier.end()) {
          multiplier[l] = mul;
          holes.push(l);
        } else {
          it->second += mul;
        }
      }

      if (r > 0) {
        it = multiplier.find(r);
        if (it == multiplier.end()) {
          multiplier[r] = mul;
          holes.push(r);
        } else {
          it->second += mul;
        }
      }
    }

    ll answer = 1;
    for (map<ll, ll>::reverse_iterator it = multiplier.rbegin();
        it != multiplier.rend(); ++it) {
      if (it->second >= k) {
        answer = it->first;
        break;
      }
      k -= it->second;
    }
    cout << "Case #" << it << ": " << answer / 2LL << " " << (answer - 1LL) / 2LL << endl;
//    for (map<ll, ll>::reverse_iterator it = multiplier.rbegin();
//        it != multiplier.rend(); ++it) {
//      printf("(%Ld, %Ld): %Ld\n", it->first / 2LL, (it->first - 1LL) / 2LL, it->second);
//    }
  }
  return 0;
}
