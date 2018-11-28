#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    ll n;
    cin >> n;
    vi a;
    while (n) {
      a.push_back(n % 10);
      n /= 10;
    }
    for (int i = 1; i < a.size(); ++i) {
      if (a[i] > a[i-1]) {
        --a[i];
        for (int j = 0; j < i; ++j) a[j] = 9;
      }
    }
    ll res = 0;
    for (int i = a.size() - 1; i >= 0; --i) res = res * 10 + a[i];
    cout << res << endl;
  }
  return 0;
}
