#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define DEBUG(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long double ld;
typedef long long ll;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
};

int num_digits(ll n) {
  if (n < 10) return 1;
  return 1 + num_digits(n / 10);
}

int main() {
  vector<ll> p10(19);
  p10[0] = 1;
  for (int i = 1; i < int(p10.size()); ++i) {
    p10[i] = 10 * p10[i - 1];
  }
  vector<ll> all1(20);
  all1[0] = 0;
  for (int i = 1; i < int(all1.size()); ++i) {
    all1[i] = 10 * all1[i - 1] + 1;
  }

  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    ll n;
    cin >> n;
    ll y = 0;
    for (int i = num_digits(n) - 1; i >= 0; --i) {
      ll dig = 0;
      while (dig < 9 && y + (dig + 1) * all1[i + 1] <= n) {
        ++dig;
      }
      y += dig * p10[i];
    }
    cout << "Case #" << ca << ": " << y << endl;
  }
}
