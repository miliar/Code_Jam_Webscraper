#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int T;

int main () {

  cin >> T;

  for(int tc=1;tc<=T;tc++) {

    string s;
    int k;
    cin >> s >> k;
    int ret = 0;
    for(int i=0; i + k<=s.size();i++) {
      if(s[i] == '-') {
        ret ++;
        for(int j=i; j<i+k;j++) {
          if(s[j] == '-') s[j] = '+';
          else s[j] = '-';
        }
      }
    }

    bool flipped = true;

    for(int i=0;i<s.size();i++) if (s[i] == '-') flipped = false;
    printf("Case #%d: ",tc);

    if(flipped) printf("%d", ret);
    else printf("IMPOSSIBLE");
    printf("\n");
  }

  return 0;
}