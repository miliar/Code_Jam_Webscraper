#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T; cin>>T;
  for(int t=1; t<=T; t++){
    string s; cin>>s;
    int k; cin>>k;
    int ans=0;
    int last=s.size()-k;
    for(int i=0; i<=last; i++){
      if(s[i]=='-'){
        ans++;
        for(int j=i; j<i+k; j++){
          if(s[j]=='-') s[j]='+';
          else s[j]='-';
        }
      }
    }
    bool ok=1;
    for(auto i:s) if(i=='-')ok=0;
    if(ok) printf("Case #%d: %d\n", t, ans);
    else printf("Case #%d: IMPOSSIBLE\n", t);
  }
}
