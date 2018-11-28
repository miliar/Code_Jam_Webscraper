#include <iostream>
#include <string>

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

    string S;
    ll K;
    cin >> S;
    cin >> K;

    ll cost = 0;

    for(ll j = 0; j < S.length()-K+1; j++) {
      if(S[j] == '-') {
        for(ll k = j; k < j+K; k++) {
          if(S[k] == '-') {
            S[k] = '+';
          }else{
            S[k] = '-';
          }
        }
        cost ++;
      }
      //cout << S << endl;
    }
    bool possible = true;
    for(ll j = S.length()-K+1; j < S.length(); j++) {
      if(S[j] == '-') possible = false;
    }

    cout << "Case #" << i+1 << ": ";
    if(possible) {
      cout << cost << "\n";
    }else{
      cout << "IMPOSSIBLE" << "\n";
    }

  }



  return 0;
}
