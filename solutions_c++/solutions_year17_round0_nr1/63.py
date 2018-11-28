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
    string s;
    int k;
    cin >> s >> k;
    int flips = 0;
    for (int i = 0; i < int(s.size()) + 1 - k; ++i) {
      if (s[i] == '-') {
        ++flips;
        for (int j = i; j < i + k; ++j) {
          if (s[j] == '-') {
            s[j] = '+';
          } else {
            s[j] = '-';
          }
        }
      }
    }
    cout << "Case #" << ca << ": ";
    if (s == string(int(s.size()), '+')) {
      cout << flips;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }
}
