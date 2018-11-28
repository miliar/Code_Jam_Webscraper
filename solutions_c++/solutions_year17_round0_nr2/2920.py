#include<bits/stdtr1c++.h>
using namespace std;

int T;
string S;

int main() {
  ios::sync_with_stdio(0);
  cin.tie();

  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> S;
    bool dec = false;
    int i;
    for (i = 0; i < int(S.size())-1; ++i) {
      if (S[i] > S[i+1]) {
        dec = true;
        break;
      }
    }
    if (dec) {
      for (; i > 0; --i) {
        if (S[i] != S[i-1]) {
          break;
        }
      }
      S[i]--;
      for (++i; i < int(S.size()); ++i) {
        S[i] = '9';
      }
      for (i = 0; i < int(S.size()); ++i) {
        if (S[i] != '0') break;
      }
      S = S.substr(i);
    }
    cout << "Case #" << t << ": " << S << endl;
  }

  return 0;
}
