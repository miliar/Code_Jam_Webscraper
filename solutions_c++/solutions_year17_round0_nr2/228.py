#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define rep(i,from,to) for(int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define FOR(i,to) for(int i=0;i<(to);++i)
#define Nmax 101010
vi v1,v2;
ll best[20][10][2];

ll inc(vi v) {
  FOR(i,20) FOR(j,10) FOR(k,2) best[i][j][k] = 0;
  
  FOR(j,v[0]) best[1][j][0] = 1;
  best[1][v[0]][1] = 1;
  FOR(j,10) if(j) {
    best[1][j][1] += best[1][j-1][1];
    best[1][j][0] += best[1][j-1][0];
  }
  rep(i,2,sz(v)+1) {
    FOR(j,10) {
      if(j == v[i-1] && v[i-1] >= v[i-2]) {
        best[i][j][1] = best[i-1][v[i-2]][1];
      }
      best[i][j][0] += best[i-1][j][0];
      if(j < v[i-1]) {
        best[i][j][0] += best[i-1][min(v[i-2],j)][1];
      }
    }
    rep(j,1,10) {
      best[i][j][1] += best[i][j-1][1];
      best[i][j][0] += best[i][j-1][0];
    }
  }
  return best[v.size()][9][0] + best[v.size()][9][1];
}

ll make(ll x) {
  vi v;
  ll xa=x;
  if(x <= 9) return x;
  while(xa) {
    v.pb(xa%10);
    xa=xa/10;
  }
  reverse(all(v));
  return inc(v);
}
ll T,tt,X;
int main() {
  cin >> T;
  while(T--) {
    ++tt;
    cin >> X;
    ll num = make(X);
    //cout << num << endl;
    ll st = 1;
    ll dr = X;
    ll ret = 0;
    while(st <= dr) {
      ll mij = (st+dr)/2;
      ll val = make(mij);
      if(val == num) {
        dr = mij - 1;
        ret = mij;
      } else {
        st = mij + 1;
      }
    }
    cout << "Case #" << tt <<": ";
    cout << ret << "\n";
   
  }
}
