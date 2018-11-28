#include <bits/stdc++.h>
using namespace std;
#define ll long long

bool isOk(ll x) {
  string s = to_string(x);
  bool ret = true;
  for(int i = 0; i < s.length() - 1; i++)
    if(s[i] > s[i + 1])
      return false;

  return true;
}

ll pw10(ll a) {
  ll ret = 1;
  for(ll i = 0; i < a; i++)
    ret *= 10;
  return ret;
}

ll convert(ll x) {
  string s = to_string(x);
  int len = s.length();

  for(int i = 0; i < len - 1; i++) {
    if(s[i] > s[i + 1]) {
      s[i] -= 1;
      for(int k = i + 1; k < len; k++)
        s[k] = '9';
      return stoll(s);
    }
  }

}

int main() {
  int T;
  cin >> T;

  for(int t = 0; t < T; t++) {


    ll N;
    cin >> N;

    while(!isOk(N)) {
      N = convert(N);
    }
    cout << "Case #" << t + 1 << ": ";
    cout << N << endl;

  }


}
