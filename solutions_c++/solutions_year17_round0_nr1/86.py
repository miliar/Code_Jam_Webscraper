#include <bits/stdc++.h>
using namespace std;

int Main() {
  string s;
  int k;
  cin >> s >> k;
  
  int n = s.size();
  int ans = 0;
  for (int i=0; i<n-k+1; i++) {
    if (s[i] == '-') {
      ans++;
      for (int j=i; j<i+k; j++) {
        if (s[j] == '-') s[j] = '+';
        else s[j] = '-';
      }
    }
  }
  
  for (int i=0; i<n; i++) if (s[i] == '-') return 0 * printf("IMPOSSIBLE\n");
  printf("%d\n", ans);
  return 0;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc=0; tc<t; ++tc) {
    printf("Case #%d: ", tc+1);
    Main();
  }
  return 0;
}