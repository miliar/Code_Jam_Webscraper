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
    int n, c, m;
    cin >> n >> c >> m;
    vector<int> ncnt(n + 1), ccnt(c + 1);
    for (int i = 0; i < m; i++) {
      int x, y;
      cin >> x >> y;
      ncnt[x]++;
      ccnt[y]++;
    }
    int res = max(ncnt[1], max(ccnt[1], ccnt[2]));
    int res1 = 0;
    for (int i = 2; i <= n; i++) {
      res1 = max(res1, ncnt[i] - res);
    }
    cout << "Case #" << tk1 << ": " << res << " " << res1 << endl;
  }
  return 0;
}
