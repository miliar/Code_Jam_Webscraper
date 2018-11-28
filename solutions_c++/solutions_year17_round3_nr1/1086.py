#include <bits/stdc++.h>

using namespace std;

const int N = 1003;

int n, k;
pair<int, int> a[N]; // r, h
double memo[N][N];

double area(int i) {
  return M_PI * 2.0 * a[i].first * (a[i].first + a[i].second);
}

double surface(int i) {
  return M_PI * a[i].first * 1ll * a[i].first;
}

double solve(int i, int rem) {
  if (i == n) {
    return rem == 0 ? 0 : -1e15;
  }
  double &ret = memo[i][rem];
  if (ret == ret) {
    return ret;
  }
  ret = solve(i + 1, rem);
  if (rem > 0) {
    ret = max(ret, solve(i + 1, rem - 1) + area(i) - surface(i) * (rem == k ? 1.0 : 2.0));
  }
  return ret;
}

//void print(int i, int rem) {
//  if (i == n) {
//    return;
//  }
//  if (rem > 0) {
//    if (solve(i + 1, rem - 1) + area(i) - surface(i) * (rem == k ? 1.0 : 2.0) > solve(i + 1, rem)) {
//      cout << i + 1 << endl;
//      print(i + 1, rem - 1);
//    }
//  }
//}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; ++i) {
      scanf("%d %d", &a[i].first, &a[i].second);
    }
    sort(a, a + n, greater<pair<int, int>>());
    memset(memo, -1, sizeof memo);
//    cout << fixed << area(0) - surface(0) << endl;
    printf("Case #%d: %.10lf\n", tst++, solve(0, k));
//    print(0, k);
  }
}

