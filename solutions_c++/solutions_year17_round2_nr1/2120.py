#include <bits/stdc++.h>
#define ll long long

using namespace std;

const int N = 123456;

int n;
double d;
double k[N];
double s[N];

void io() {
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
}

int main() {
  io();
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; test++) {
    printf("Case #%d: ", test);
    cin >> d >> n;
    for (int i = 0; i < n; i++) {
      cin >> k[i] >> s[i];
    }
    double tt = 0.0;
    for (int i = 0; i < n; i++) {
      tt = max(tt, (d - k[i]) / s[i]);
    }
    double ans = d / tt;
    cout.precision(12);
    cout << fixed << ans << endl;
  }
  return 0;
}
