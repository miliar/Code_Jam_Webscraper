#include <iostream>
#include <string>

using namespace std;
typedef long long ll;


int main() {
  ll T;
  cin >> T;
  for(ll cas=1; cas<=T; cas++) {
    string S;
    cin >> S;
    ll k;
    cin >> k;
    ll ans = 0;
    for(ll i=0; i+k-1<S.size(); i++) {
      if(S[i] == '-') {
        ans++;
        for(ll j=0; j<k; j++) {
          S[i+j] = (S[i+j]=='-' ? '+' : '-');
        }
      }
    }
    bool ok = true;
    for(ll i=0; i<S.size(); i++) {
      if(S[i]=='-') {
        ok = false;
      }
    }
    cout << "Case #" << cas << ": ";
    if(ok) {
      cout << ans;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }
}
