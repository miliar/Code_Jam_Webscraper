#include<bits/stdc++.h>
using namespace std;

int main (void) {
  int t, k;
  string s;
  cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    cin >> s >> k;
    int n = s.size();
    int ans = 0;
    for (int i = 0; i <= n-k; i++) {
      if (s[i] == '-') {
        for (int j = 0; j < k; j++)
          s[i+j] = '+' + '-' - s[i+j];
        ans++;
      }
      //cerr << s << '\n';
    }
    bool ok = true;
    for (int i = n-k+1; i < n; i++)
      if (s[i] == '-')
        ok = false;
    printf("Case #%d: ",tt);
    if (ok)
      printf("%d\n",ans);
    else
      printf("IMPOSSIBLE\n");
  }
}
