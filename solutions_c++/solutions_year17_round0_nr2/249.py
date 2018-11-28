#include <iostream>
#include <string>

using namespace std;
typedef long long ll;

void dec(string& S, ll i) {
  if(S[i]=='0') {
    S[i]='9';
    dec(S, i-1);
  } else {
    S[i]--;
  }
}

int main() {
  ll T;
  cin >> T;
  for(ll cas=1; cas<=T; cas++) {
    ll n;
    cin >> n;
    string S = to_string(n);
    for(ll i=S.size()-1; i>=1; i--) {
      if(S[i] < S[i-1]) {
        for(ll j=i; j<S.size(); j++) {
          S[j] = '9';
        }
        dec(S, i-1);
      }
    }
    while(S[0]=='0') {
      S = S.substr(1);
    }
    cout << "Case #" << cas << ": " << S << endl;
  }
}
