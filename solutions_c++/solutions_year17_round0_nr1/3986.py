#include <bits/stdc++.h>
using namespace std;
int main() {
  freopen("A-large.in","r",stdin);
  freopen("ans.txt","w",stdout);
  int T,K;
  string s;
  cin >> T;
  for(int tt=1;tt<=T;tt++) {
     printf("Case #%d: ",tt);
     cin >> s >> K;
     int N = s.length();
     vector<int> a(N);
     for(int i=0;i<N;i++) {
          if(s[i] == '-') a[i] = 0;
          else a[i] = 1;
     }
     int cnt = 0;
     for(int i=0;i<N-K+1;i++) {
        if(a[i] == 0) {
          cnt++;
          for(int j=i;j<i+K;j++) {
               a[j] = 1-a[j];
          }
        }
     }
     bool flag = true;
     for(int i=0;i<N;i++) {
          if(a[i] == 0) {
               flag = false;
               break;
          }
     }
     if(!flag) puts("IMPOSSIBLE");
     else printf("%d\n",cnt);
  }
  return 0;
}
