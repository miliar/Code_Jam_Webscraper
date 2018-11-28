#include <bits/stdc++.h>
using namespace std;

int n, p;
int req[55];
int ing[55][55];
pair<int, int> range[55][55];

long long ceill(long long x, long long y) {
  if (x % y == 0) return x / y;
  return x / y + 1;
}

int Main() {
  scanf("%d %d", &n, &p);
  for (int i=0; i<n; i++) scanf("%d", req + i);
  for (int i=0; i<n; i++) for (int j=0; j<p; j++) scanf("%d", &ing[i][j]);
  
  int ans = 0;
  for (int i=0; i<n; i++) {
    for (int j=0; j<p; j++) {
      range[i][j] = {ceill(ing[i][j] * 10, 11 * req[i]), ing[i][j] * 10 / (req[i] * 9)};
      if (range[i][j].first > range[i][j].second) range[i][j] = {0, -1};
      // cerr << range[i][j].first << " " << range[i][j].second << endl;
    }
  }
  
  if (n == 1) {
    int sum = 0;
    for (int i=0; i<p; i++) sum += range[0][i].second > 0;
    printf("%d\n", sum);
  } else {
    int ans = 0;
    sort(range[1], range[1] + p);
    do {
      int tmp = 0;
      for (int i=0; i<p; i++) {
        int a = range[0][i].first;
        int b = range[0][i].second;
        int c = range[1][i].first;
        int d = range[1][i].second;
        
        if (a > d || b < c) continue;
        tmp += min(b, d) > 0;
      }
      
      ans = max(ans, tmp);
    } while (next_permutation(range[1], range[1] + p));
    
    printf("%d\n", ans);
  }
  return 0;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc=0; tc<t; tc++) {
    printf("Case #%d: ", tc+1);
    Main();
  }
  return 0;
}