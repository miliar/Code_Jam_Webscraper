#include<bits/stdc++.h>
using namespace std;

int main (void) {
  int t;
  cin >> t;
  string s;
  for (int tt = 1; tt <= t; tt++) {
    cin >> s;
    int l = s.size();
    for (int i = l-2; i >= 0; i--) {
      if (s[i] > s[i+1]) {
        s[i]--;
        for (int j = i+1; j < l; j++)
          s[j] = '9';
      }
    }
    printf("Case #%d: ",tt);
    bool start = false;
    for (int i = 0; i < l; i++) {
      if (s[i] != '0')
        start = true;
      if (start)
        printf("%c",s[i]);
    }
    printf("\n");
  }
}
