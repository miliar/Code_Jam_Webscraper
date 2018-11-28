#include<bits/stdc++.h>
#define pb push_back
using namespace std;
typedef long long ll;
int T;
ll N, K;

void afis(ll N) {
  //cout<<N<<"! ";
  cout<<N-(N+1)/2<<" "<<(N-1)/2<<"\n";
}

int main() {
  cin.sync_with_stdio(false);
  cin>>T;
  for(int t=1;t<=T;++t) {
    cin>>N>>K;
    cout<<"Case #"<<t<<": ";
    ll sum = 0, ret = 0;
    ll l = N, nrl = 0;
    ll r = N, nrr = 1;
    
    while(true) {
      //cout<<l<<" "<<nrl<<", "<<r<<" "<<nrr<<", "<<sum<<endl;
      if(sum + nrr >= K) {
        ret = r;
        break;
      }
      if(sum + nrr + nrl >= K) {
        ret = l;
        break;
      }
      sum += (nrr + nrl);
      ll newl = (l-1)/2, cntl = nrl;
      ll newr = r - (r+1)/2, cntr = nrr;
      
      if(l - (l+1)/2 == newl) cntl += nrl;
      else cntr += nrl;
      
      if((r-1)/2 == newl) cntl += nrr;
      else cntr += nrr;
      
      l = newl; r = newr; nrl = cntl; nrr = cntr;
    }
    
    afis(ret);
  }
  return 0;
}
