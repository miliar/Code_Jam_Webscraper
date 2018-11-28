#include <bits/stdc++.h>
using namespace std;

int n, d;
pair<int, int> horses[1002];

int Main() {
  scanf("%d %d", &d, &n);
  for (int i=0; i<n; i++) scanf("%d %d", &horses[i].first, &horses[i].second);
 
  double t = 0;
  for (int i=0; i<n; i++) {
    t = max(t, (double) (d - horses[i].first) / horses[i].second);
  }
  
  printf("%.12lf\n", (double) d / t);
 
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