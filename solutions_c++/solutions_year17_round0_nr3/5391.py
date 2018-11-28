#include <iostream>
#include <vector>
#include <stack>

using namespace std;

#ifdef DEBUG
  #define DEB(x) cerr << x << '\n'
#else
  #define DEB(x)
#endif

typedef long long int ll;

int main () {

  ios_base::sync_with_stdio(false);
  cin.tie(0);

  ll T;
  cin >> T;

  for(ll i = 0; i < T; i++) {
    ll best = 0;
    ll LS,LR;
    ll N,K;
    cin >> N >> K;
    vector<bool> S(N+2, false);
    S[0] = true;
    S[N+1] = true;
    for(ll j = 0; j < K; j++) {
      vector<ll> Maxs(N+2, 0);
      vector<ll> Mins(N+2, N+3);
      stack<ll> St;
      ll curCount = 0;
      curCount = 0;
      for(ll k = N+1; k >= 0; k--) {
        if(S[k]) {
          curCount = 0;
          Mins[k] = 0;
        }else{
          Mins[k] = min(Mins[k], curCount);
          Maxs[k] = max(Maxs[k], curCount);
          curCount ++;
        }
      }
      best = 0;
      for(ll k = 0; k <= N+1; k++) {
        if(S[k]) {
          curCount = 0;
        }else{
          Mins[k] = min(Mins[k], curCount);
          Maxs[k] = max(Maxs[k], curCount);
          curCount ++;
        }
        if(Mins[k] >= Mins[best]) {
          if(Mins[k] > Mins[best] || Maxs[k] > Maxs[best]) {
            best = k;
          }
        }
      }
      S[best] = true;
      LS = Mins[best];
      LR = Maxs[best];
      // for(bool p : S) {
      //   cout << p;
      // }cout << endl;
      // for(ll m : Mins) {
      //   cout << m << " ";
      // }cout << endl;
      // for(ll m : Maxs) {
      //   cout << m << " ";
      // }cout << endl;
    }
    cout << "Case #" << i+1 << ": " << LR << " " << LS << "\n";
  }

  return 0;
}
