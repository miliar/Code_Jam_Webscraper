#include <bits/stdc++.h>

using namespace std;

int main() {
  /* code */
  freopen("alarge.in","r",stdin);
  freopen("alarge-out.txt","w",stdout);
  int t;
  cin>>t;
  for(int test=1;test<=t;test++) {
    string s;
    int k,n,ans=0;
    cin>>s>>k;
    n = s.length();
    for(int i=0;i<n-k+1;i++) {
      if (s[i]=='-'){
        ans++;
        for(int j=0;j<k;j++) {
          if(s[i+j]=='-'){
            s[i+j] = '+';
          } else {
            s[i+j] ='-';
          }
        }
      }
    }

    for(int i=n-k+1;i<n;i++) {
      if(s[i]=='-') {
        ans=-1;
      }
    }

    if(ans==-1) {
      cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
    }else {
      cout<<"Case #"<<test<<": "<<ans<<endl;
    }
  }
  return 0;
}
