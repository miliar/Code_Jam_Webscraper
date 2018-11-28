#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
using namespace std;
typedef long long ll;
int N,T,P, ind[60];
ll R[60], a[60][60];


int check(ll a, ll r) {
  double x = 1.0*a/r;
  if(x < 0.9) return -1;
  if(x > 1.1) return 1;
  return 0;
}

int main() {
  cin.sync_with_stdio(false);
  cin>>T;
  for(int t=1;t<=T;++t) {
    cin>>N>>P;
    for(int i=1;i<=N;++i) {
      cin>>R[i];
    }
    ll vmax = 0, ret = 0;
    
    for(int i=1;i<=N;++i) {
      ind[i] = 1;
      for(int j=1;j<=P;++j) {
        cin>>a[i][j];
      }
      sort(a[i]+1,a[i]+P+1);
      double lim = 1.0 * a[i][P] / (R[i] * 0.9);
      ll l = (ll)(ceil(lim));
      vmax = max(vmax, l);
    }
    
    for(int k=1;k<=vmax;++k) {
      int kits = P;
      for(int i=1;i<=N;++i) {
        int val = 0;
        while(ind[i] <= P && check(a[i][ind[i]],R[i]*k) == -1) {
          ++ind[i];
        }
        int curr = ind[i];
        while(val<=kits && curr <= P && check(a[i][curr],R[i]*k) == 0) {
          ++val;
          ++curr;
        }
        kits = min(kits,val);
      }
      ret += kits;
      for(int i=1;i<=N;++i) {
        ind[i] += kits;
      }
    }
    cout<<"Case #"<<t<<": "<<ret<<"\n";
  }
  return 0;
}
