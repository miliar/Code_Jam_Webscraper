#include <bits/stdc++.h>

using namespace std;

using ll = long long;

const int MAXN = 1123;

int n, c, m;
int t[MAXN][MAXN];

int promo(int k) {
  int cost = 0;
  int slack = 0;
  for (int j = 0; j < n; j++) {
    int sum = 0;
    for (int i = 0; i < c; i++) sum += t[i][j];
    if (sum > k) {
      if (sum - k > slack) return -1;
      cost += sum - k;
      slack -= sum - k;
    } else {
      slack += k - sum;
    }
  }
  return cost;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    memset(t, 0, sizeof(t));
    cin >> n >> c >> m;
    for (int i = 0; i < m; i++) {
      int pi, bi;
      cin >> pi >> bi;
      t[bi - 1][pi - 1]++;
    }

    int ub = m;
    int lb = 1;
    for (int i = 0; i < c; i++) {
      int sum = 0;
      for (int j = 0; j < n; j++) sum += t[i][j];
      lb = max(lb, sum);
    }

    while (lb < ub) {
      int mid = (lb + ub) / 2;
      if (promo(mid) == -1) {
        lb = mid + 1;
      } else {
        ub = mid;
      }
    }

    int cost = promo(lb);

    cout << "Case #" << tc << ": " << lb << ' ' << cost << endl;

    
  }

}
