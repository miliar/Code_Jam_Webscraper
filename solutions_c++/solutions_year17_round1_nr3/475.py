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

ll dp[102][202][102][102];
ll hd_save;

ll compute(ll hd, ll ad, ll hk, ll ak, ll b, ll d){
  if(hk <= 0) return 0;
  if(hd <= 0) return oo;
  if(ad > 201) return oo;
  if(dp[hd][ad][hk][ak] == -1) return oo;
  if(dp[hd][ad][hk][ak] < oo){
    return dp[hd][ad][hk][ak];
  }
  dp[hd][ad][hk][ak] = -1;
  ll res = oo;
  res = min(res, compute(hd - ak, ad, hk - ad, ak, b, d));
  res = min(res, compute(hd - ak, ad + b, hk, ak, b, d));
  res = min(res, compute(hd_save - ak, ad, hk, ak, b, d));
  res = min(res, compute(hd - max(0ll, ak-d), ad, hk, max(0ll,ak - d), b, d));
  dp[hd][ad][hk][ak] = res + 1;
  return res + 1;
}

int main(){
	ios::sync_with_stdio(false);
  ll TC;
  cin >> TC;
  FOR(tc,0,TC){
    cout << "Case #" << tc+1 << ": ";
    ll hd, ad, hk, ak, b, d;
    cin >> hd >> ad >> hk >> ak >> b >> d;
    hd_save = hd;
    FOR(i,0,102){
      FOR(j,0,202){
        FOR(k,0,102){
          FOR(l,0,102){
            dp[i][j][k][l] = oo;
          }
        }
      }
    }
    ll res = compute(hd, ad, hk, ak, b, d);
    if(res < oo)
    cout << res << endl;
    else
      cout << "IMPOSSIBLE" << endl;
  }
}
