#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vl = vector<ll>;
using vvl = vector<vl>;
using pll = pair<ll,ll>;
using vb = vector<bool>;
const ll oo = 0x3f3f3f3f3f3f3f3fLL;
const double eps = 1e-9;
#define	sz(c) ll((c).size())
#define	all(c) begin(c),end(c)
#define	mp make_pair
#define mt make_tuple
#define	pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define	has(c,i) ((c).find(i) != end(c))
#define FOR(i,a,b) for (ll i = (a); i < (b); i++)
#define	FORD(i,a,b) for (ll i = (b)-1; i >= (a); i--)
ll n, c, m;

ll poss(ll r, vl &tps){
  ll fs = 0;
  ll p = 0;
  FOR(i,0,n){
    if(tps[i] > r){
      if(fs < tps[i] - r)
        return oo;
      fs -= tps[i] - r;
      p += tps[i] - r;
    } else{
      fs += r - tps[i];
    }
  }
  return p;
}

int main(){
	ios::sync_with_stdio(false);
    ll TC;
    cin >> TC;
    FOR(tc,1,TC+1){
        cin >> n >> c >> m;
        vl tpc(c, 0);
        vl tps(n, 0);
        ll min_rides = 0;
        FOR(i,0,m){
          ll p, b;
          cin >> p >> b;
          p--; b--;
          tpc[b]++;
          tps[p]++;
          min_rides = max(tpc[b], min_rides);
        }
        ll a = min_rides-1, b = 1000000;
        while(a + 1 < b){
          ll c = (a+b)/2;
          ll p = poss(c, tps);
          if(p != oo){
            b = c;
          } else {
            a = c;
          }
        }
        cout << "Case #" << tc << ": " << b << " " << poss(b, tps) << endl;
    }
}
