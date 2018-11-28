#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long double ld;
typedef long long ll;
typedef vector<int> Vi;
typedef vector<Vi> Mi;

int main() {
  cout.setf(ios::fixed);
  cout.precision(9);
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    ld d;
    int n;
    cin >> d >> n;
    ld t_max = 0;
    for (int i = 0; i < n; ++i) {
      ld k, s;
      cin >> k >> s;
      ld t = (d - k)/s;
      t_max = max(t_max, t);
    }
    ld v = d/t_max;
    cout << "Case #" << cas << ": " << v << endl;
  }
}
