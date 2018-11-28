#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;

#ifdef DEBUG
#define DB(x) cerr<<#x<<": "<<x<<" ";
#define DBL(x) cerr<<#x<<": "<<x<<endl;
#else
#define DB(x)
#define DBL(x)
#endif


int main(){
  ll d, n;
  int t;
  cin >> t;
  cout<<fixed<<setprecision(6);
  for(int c=1;c<=t;c++){
    vector<pii> h;
    cin >> d >> n;
    ll x, v;
    for(int i=0;i<n;i++){
      cin >> x >> v;
      h.emplace_back(x,v);
    }
    
    double best = -1;
    sort(h.begin(),h.end(),std::greater<pii>());
    for(auto p : h){
      DBL(best)
      x = p.first;
      v = p.second;
      best = max(((d-x)*1.0)/v, best);
    }
    DBL(best)
    cout<<"Case #"<<c<<": "<<d/best<<endl;
  }
}
