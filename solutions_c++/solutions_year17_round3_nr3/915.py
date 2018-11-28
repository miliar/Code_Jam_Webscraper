#include <bits/stdc++.h>

using namespace std;

const int N = 55, MAX = 10000;

int n, k;
int p[N];

int main() {
//  freopen("input.in", "r", stdin);
  freopen("C-small-1-attempt1.in", "r", stdin);
  freopen("C-small-1-attempt1.out", "w", stdout);
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    scanf("%d %d", &n, &k);
    int x, y;
    scanf("%d.%d", &x, &y);
    x = x * MAX + y;
    for (int i = 0; i < n; ++i) {
      int a;
      scanf("%d.%d", p + i, &a);
      p[i] = p[i] * MAX + a;
    }
    priority_queue<int> q;
    for (int i = 0; i < n; ++i) {
      q.push(-p[i]);
    }
    while (q.top() < MAX && x > 0) {
      int cur = -q.top();
      q.pop();
      q.push(-(cur + 1));
      --x;
    }
    double res = 1;
    while (!q.empty()) {
      res *= (double)-q.top() / MAX;
      q.pop();
    }
    printf("Case #%d: %.10lf\n", tst++, res);
  }
}

