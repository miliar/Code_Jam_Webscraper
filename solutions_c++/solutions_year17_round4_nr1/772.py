#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <cstring>
#define ll long long
using namespace std;

int main() {
  int tk;
  cin >> tk;
  for (int tk1 = 1; tk1 <= tk; tk1++) {
    int n, p;
    cin >> n >> p;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    int res = 0;
    vector<int> c(p);
    for (int i = 0; i < n; i++) {
      c[a[i] % p]++;
    }
    if (p == 2) {
      res = c[0] + (c[1] + 1) / 2;
    } else if (p == 3) {
      res = c[0] + min(c[1], c[2]);
      int diff = abs(c[1] - c[2]);
      res += (diff + 2) / 3;
    } else if (p == 4) {
      res += c[0] + min(c[1], c[3]) + c[2] / 2;
      int diff = abs(c[1] - c[3]);
      if (c[2] % 2 == 1 && diff >= 2) {
        res++;
        diff -= 2;
      }
      res += (diff + 3) / 4;
    }
    cout << "Case #" << tk1 << ": " << res<< endl;
  }
  return 0;
}
