#include <bits/stdc++.h>
#define ll long long

using namespace std;

void io() {
  freopen("C-small-1-attempt2.in", "r", stdin);
  freopen("output.txt", "w", stdout);
}

const int N = 1234;

int n, k;
long double u;
long double p[N];

struct compare  {
   bool operator()(const double &l, const double &r) {
       return l > r;
   }
};

bool check(long double mid) {
  long double ret = 0.0;
  for (int i = 0; i < n; i++) {
    if (p[i] < mid) {
      ret += (mid - p[i]);
    }
  }
  if (ret - u <= 1e-6) return true;
  else return false;
}

int main() {
  io();
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; test++) {
    printf("Case #%d: ", test);
    cin >> n >> k;
    cin >> u;
    for (int i = 0; i < n; i++) {
      cin >> p[i];
    }
    long double low = 0.0, high = (long double) 1, mid, ans = 0.0;
    while (abs(low - high) > 1e-9) {
      mid = (low + high) / 2;
      if (check(mid)) {
        low = mid;
        ans = max(ans, low);
      } else {
        high = mid;
      }
    }
    long double ret = (long double) 1;
    for (int i = 0; i < n; i++) {
      ret = ret * max(ans, p[i]);
    }
    cout.precision(12);
    cout << fixed << ret << endl;
  }
  return 0;
}
