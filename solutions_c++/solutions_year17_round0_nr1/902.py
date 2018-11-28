#include <bits/stdc++.h>

using namespace std;

void solve()
{
  string S;
  int K;

  cin >> S;
  cin >> K;

  int ret = 0;

  for(int i = 0; i <= S.size() - K; i++) {
    if(S[i] == '-') {
      for(int j = 0; j < K; j++) {
        S[i + j] = "+-"[S[i + j] == '+'];
      }
      ++ret;
    }
  }

  bool impossible = false;

  for(int i = 0; i < S.size(); i++) {
    if(S[i] == '-') impossible = true;
  }

  if(impossible) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << ret << endl;
  }
}

int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
}

