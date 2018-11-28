#include <bits/stdc++.h>
using namespace std;

const double pi = 3.14159265;
int r[1005], h[1005];

double area(int r, int h) {
  return 2 * pi * r * h;
}

double topdown(int r) {
  return pi * r * r;
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A.out", "w", stdout);
  int t;
  scanf("%d", &t);
  int n, k;
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++) {
      scanf("%d %d", &r[i], &h[i]);
    }
    double ans = 0;
    for (int i = 0; i < n; i++) {
      vector<double> arr;
      double ret = area(r[i], h[i]);
      for (int j = 0; j < n; j++) {
        if (i == j) continue;
        arr.push_back(area(r[j], h[j]));
      }
      sort(arr.begin(), arr.end());
      reverse(arr.begin(), arr.end());
      for (int j = 0; j < k - 1; j++) ret += arr[j];
      ret += topdown(r[i]);
      ans = max(ans, ret);
    }
    printf("%lf\n", ans);
  }  
}