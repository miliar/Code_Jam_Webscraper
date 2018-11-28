#include<bits/stdc++.h>
#define pb push_back
using namespace std;
typedef long long ll;
ll N;
int T;

ll build(vector<int> &v) {
  ll ret = 0;
  for(auto x: v) {
    ret = ret*10 + x;
  }
  return ret;
}

ll f(ll N) {
  vector<int> dig;
  while(N) {
    dig.pb(N%10);
    N /= 10;
  }
  int k = dig.size();
  reverse(dig.begin(),dig.end());
  int maxx = 0;
  for(int i=1;i<k;++i) {
    if(dig[i] >= dig[i-1]) maxx = i;
    else break;
  }
  if(maxx < k-1) {
    int ind = maxx;
    for(int i=maxx-1;i>=0;--i) {
      if(dig[i] == dig[maxx]) ind = i;
      else break;
    }
    --dig[ind];
    for(int i=ind+1;i<k;++i) dig[i] = 9;
  }
  return build(dig);
}

int main() {
  cin.sync_with_stdio(false);
  cin>>T;
  for(int t=1;t<=T;++t) {
    cin>>N;
    cout<<"Case #"<<t<<": "<<f(N)<<"\n";
  }
  return 0;
}
