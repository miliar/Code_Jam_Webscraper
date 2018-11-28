#include <bits/stdc++.h>

using namespace std;

int main() {
  int test, n, p, a[10], x;
  cin >> test;
  for (int ca = 1; ca <= test; ++ca) {
    cin >> n >> p;
    memset(a, 0, sizeof a);
    for (int i = 0; i < n; ++i) {
      cin >> x;
      ++a[x % p];
    }
    cout << "Case #" << ca << ": ";
    if (p == 2) {
      cout << a[0] + (a[1] + 1) / 2 << endl;
    } else if (p == 3) {
      if (a[1] == a[2]) {
        cout << a[0] + a[1] << endl;
      } else {
        cout << a[0] + min(a[1], a[2]) + (abs(a[1] - a[2]) + 2) / 3 << endl;
      }
    } else {
      cout << a[0] + a[2] / 2 + min(a[1], a[3]) + (abs(a[1] - a[3]) + 3 + a[2] % 2 * 2) / 4 << endl;
    }
  }
  return 0;
}
