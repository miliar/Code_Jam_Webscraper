#include <bits/stdc++.h>

using namespace std;

const int N = 1005;

int cnt[N], cntBuyers[N], n;

int calc(int res) {
  int reserved = 0;
  int shifts = 0;
  for (int i = 0; i < n; i++) {
    if (cnt[i] <= res) {
      reserved += res - cnt[i];  
    } else if (cnt[i] <= res + reserved) {
      shifts += cnt[i] - res;
      reserved -= cnt[i] - res;
    } else {
      return -1;
    }
  }
  return shifts;
}

int main() {
  int numTests;
  cin >> numTests;
  for (int t = 0; t < numTests; t++) {
    int c, m;
    cin >> n >> c >> m;
    for (int i = 0; i < c; i++) {
      cntBuyers[i] = 0;
    }
    for (int i = 0; i < n; i++) {
      cnt[i] = 0;
    }
    for (int i = 0; i < m; i++) {
      int p, b;
      cin >> p >> b;
      cntBuyers[b - 1]++;
      cnt[p - 1]++;
    }
    int l = 0, r = int(1e8);
    for (int i = 0; i < c; i++) {
      l = max(l, cntBuyers[i]);  
    }
    l--;
    while (l + 1 < r) {
      int mid = (l + r) / 2;
      if (calc(mid) != -1) {
        r = mid;
      } else {
        l = mid;
      }
    }
    cout << "Case #" << t + 1 << ": " << r << " " << calc(r) << endl;
  }  
  return 0;
}
