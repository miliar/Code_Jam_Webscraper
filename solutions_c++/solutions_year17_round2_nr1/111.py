#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> ii;
typedef long double ld;

const int maxn = 1010;
ll n,d;
ii k[maxn];

int main(){
  cout.precision(10);
  cout.setf(ios::fixed);
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    cin >> d >> n;
    for(int i = 0; i < n; ++i) cin >> k[i].first >> k[i].second;
    ld maxt = 0.0;
    for(int i = 0; i < n; ++i){
      maxt = max(maxt,ld(d-k[i].first)/ld(k[i].second));
    }
    cout << "Case #" << cass << ": " << ld(d)/ld(maxt) << '\n';
  }
}