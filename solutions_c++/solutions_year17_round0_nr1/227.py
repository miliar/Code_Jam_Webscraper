#include<bits/stdc++.h>
#define pb push_back
using namespace std;
typedef long long ll;
int T,N,K;
string s;

int main() {
  cin.sync_with_stdio(false);
  cin>>T;
  for(int t=1;t<=T;++t) {
    cin>>s>>K;
    N = s.size();
    int ret = 0;
    cout<<"Case #"<<t<<": ";
    for(int i=0;i+K-1<N;++i) {
      if(s[i] == '-') {
        ++ret;
        for(int j=i;j<i+K;++j) {
          s[j] = '-' + '+' - s[j];
        }
      }
    }
    int ok = 1;
    for(int i=0;i<N;++i) if(s[i] == '-') { ok = 0; break;}
    if(ok) cout<<ret<<"\n";
    else cout<<"IMPOSSIBLE\n";
  }
  return 0;
}
