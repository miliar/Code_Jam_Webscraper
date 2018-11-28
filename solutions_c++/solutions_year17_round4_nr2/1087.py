#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
void solve() {
  int n, c, m;
  cin >> n >> c >> m;
  vector<int> pos1(1001, 0);
  vector<int> pos2(1001, 0);
  int c1 = 0;
  int c2 = 0;
  for(int i = 0; i < m; ++i) {
    int p, b;
    cin >> p >> b;
    if (b == 1) {
      ++pos1[p];
      ++c1;
    } else {
      ++pos2[p];
      ++c2;
    }
  }
  int rides = max(pos1[1] + pos2[1], max(c1,c2));
  int maxp = 0;
  int maxv = 0;
  for (int i = 2; i < 1001; ++i) {
    if (pos1[i] > maxv) {
      maxv = pos1[i];
      maxp = i;
    }
  }
  bool from2;
  for (int i = 2; i < 1001; ++i) {
    if (pos2[i] > maxv) {
      from2 = true;
      maxv = pos2[i];
      maxp = i;
    }
  }
  int promo = 0;
  if (maxv && from2 && pos1[maxp]) {
      promo = pos1[maxp] - (c2 - pos2[maxp]);
  } else if (maxv && not from2 && pos2[maxp]) {
      promo = pos2[maxp] - (c1 - pos1[maxp]);
  }
  promo = max(0, promo);
  cout << rides << " " << promo;
}

int main() {
  int tests;
  cin >> tests;
  for (int t = 0; t < tests; ++t) {
    cout << "Case #" << t + 1 << ": ";
    solve();
    cout << "\n";
  }
  return 0;
}
