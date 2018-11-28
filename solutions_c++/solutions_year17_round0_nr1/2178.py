#include <bits/stdc++.h>

using namespace std;

void solve()
{
  string S;
  int K;
  cin >> S >> K;

  int flip = 0;
  for (int i = 0; i+K-1 < S.length(); i++) {
    if (S[i] == '+') continue;
    for (int k = 0; k < K; k++) {
      if (S[i+k] == '+') S[i+k] = '-';
      else S[i+k] = '+';
    }
    flip++;
  }

  if (S.find('-') == string::npos) {
    cout << flip << endl;
  } else {
    cout << "IMPOSSIBLE" << endl;
  }
}

int main()
{
  int T;
  cin >> T;

  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }

  
  return 0;
}
