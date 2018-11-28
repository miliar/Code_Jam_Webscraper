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

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    ll n, k;
    cin >> n >> k;
    ll ss = n;
    ll sc = 1, bc = 0;
    ll last_size = -1;
    while (true) {
      if (k <= bc) {
        last_size = ss + 1;
        break;
      }
      k -= bc;
      if (k <= sc) {
        last_size = ss;
        break;
      }
      k -= sc;
      --ss;
      if (ss % 2 == 0) {
        sc = 2 * sc + bc;
      } else {
        bc = sc + 2 * bc;
      }
      ss /= 2;
    }
    ll left = (last_size - 1) / 2;
    ll right = (last_size - 1) - left;
    cout << "Case #" << ca << ": " << max(left, right) << " " << min(left, right) << endl;
  }
}
