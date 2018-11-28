#include <bits/stdc++.h>

using namespace std;

void find_prev(string S)
{
  
  int first = -1;
  for (int i = 0; i < S.length()-1; i++) {
    if (S[i] > S[i+1]) {
      first = i;
      break;
    }
  }
  if (first < 0) {
    cout << S << endl;
    return;
  }

  string prefix = to_string(stoll(S.substr(0, first+1))-1);
  if (prefix == "0") prefix = "";
  find_prev(prefix + string(S.length()-1-first, '9'));
}

void solve()
{
  string S;
  cin >> S;

  find_prev(S);
  
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
