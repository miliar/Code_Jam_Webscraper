#include <iostream>
#include <string>
#include <vector>

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
    string N;
    cin >> N;
    vector<ll> M(N.length());
    vector<ll> Ns(N.length());
    M[0] = N[0]-'0';
    Ns[0] = M[0];
    for(ll j = 1; j < N.length(); j++) {
      M[j] = max(M[j-1], (ll)N[j]-'0');
      Ns[j] = N[j] - '0';
    }
    for(ll j = N.length()-1; j > 0; j--) {
      if(Ns[j] < M[j-1]) {
        Ns[j] = 9;
        Ns[j-1] --;
      }
    }

    cout << "Case #" << i+1 << ": ";
    ll j = 0;
    while (Ns[j] == 0) j++;
    bool nine = false;
    while(j < Ns.size()) {
      if(Ns[j] == 9) nine = true;
      if(nine) {
        cout << 9;
      }else{
        cout << Ns[j];
      }
      j++;
    }
    cout << "\n";

  }



  return 0;
}
