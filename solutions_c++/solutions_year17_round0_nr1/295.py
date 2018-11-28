#include <bits/stdc++.h>
#define FOR(x,n) for(int x = 0; x < n; x++)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int)(a).size())
using namespace std;
typedef long long ll;

int main() {
  int T; cin >> T;
  for(int cases = 1; cases <= T; cases++){
    string S; int K; cin >> S >> K;
    int ans = 0, possible = true;

    for(int i = 0; i + K - 1 < SZ(S); i++)
      if(S[i] == '-'){
        for(int j = 0; j < K; j++)
          S[j+i] = S[j+i] == '-' ? '+' : '-';
        ans++;
      }

    for(int i = 0; i < SZ(S); i++)
      possible &= S[i] == '+';

    cout << "Case #" << cases << ": ";

    if(!possible)
      cout << "IMPOSSIBLE\n";
    else
      cout << ans << "\n";
  }
}
