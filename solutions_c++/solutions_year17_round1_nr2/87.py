#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
using ll = long long;
using ld = double;

bool ok(ld lo, ld hi) {
  ll nlo = static_cast<ll>(ceil(hi/1.1));
  ll nhi = static_cast<ll>(floor(lo/0.9));
  return nlo <= nhi;
}

int main() {
  ll T;
  cin >> T;
  for(ll cas=1; cas<=T; cas++) {
    ll n, p;
    cin >> n >> p;
    vector<ll> R(n, 0);
    for(ll i=0; i<n; i++) {
      cin >> R[i];
    }
    vector<vector<ld>> Q(n, vector<ld>(p, 0.0));
    for(ll i=0; i<n; i++) {
      for(ll j=0; j<p; j++) {
        cin >> Q[i][j];
        Q[i][j] /= R[i];
      }
      sort(Q[i].begin(), Q[i].end());
    }
    vector<ll> I(n, 0);
    ll ans = 0;
    while(true) {
      bool done = false;
      for(ll i=0; i<n; i++) {
        if(I[i]==p) {
          done = true;
        }
      }
      if(done) { break; }

      ll ilo = 0;
      ll ihi = 0;
      for(ll i=0; i<n; i++) {
        if(Q[i][I[i]] < Q[ilo][I[ilo]]) {
          ilo = i;
        }
        if(Q[i][I[i]] > Q[ihi][I[ihi]]) {
          ihi = i;
        }
      }
      ld lo = Q[ilo][I[ilo]];
      ld hi = Q[ihi][I[ihi]];
      if(ok(lo, hi)) {
        ans++;
        for(ll i=0; i<n; i++) {
          I[i]++;
        }
      } else {
        I[ilo]++;
      }
    }
    cout << "Case #" << cas << ": " << ans << endl;
  }
}
