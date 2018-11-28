#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main() {
  int t, n;
  string panc;
  scanf("%d", &t);
  for (int cas = 1; cas <= t; ++cas) {
    cin >> panc >> n;
    int ans = 0;
    for (int i = 0; i <= panc.size() - n; ++i) {
      if (panc[i] == '-') {
        for (int j = i; j < i + n; ++j) {
          panc[j] = (panc[j] == '-') ? '+' : '-';
        }
        ans++;
      }
    }

    bool poss = true;
    for (int i = 0; i < panc.size(); ++i)
      if (panc[i] == '-')
        poss = false;
    if (poss)
      printf("Case #%d: %d\n", cas, ans);
    else
      printf("Case #%d: IMPOSSIBLE\n", cas);
  }
  return 0;
}
