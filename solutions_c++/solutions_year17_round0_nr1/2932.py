#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int main() {
  int T, k;
  char ss[2000];
  cin >> T;
  for (int t = 1; t<=T; t++) {
    cin >> ss >> k;
    int ll = strlen(ss);
    int ans = 0, light = 0;
    for (int i = 0; i<ll; i++) {
      if (ss[i]=='-') {
        for (int j=0;j<k;j++){
          if (i+j >= ll) {
            light = 1;
            break;
          }
          ss[i+j] = ss[i+j]=='+'?'-':'+';
        }
        ans++;
      } 
    }
    if (light == 1) cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
    else cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}