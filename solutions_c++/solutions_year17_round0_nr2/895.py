#include <bits/stdc++.h>

using namespace std;

typedef long long int64;

string A;

bool rec(int last, int idx, bool free, bool ue, int64 value)
{
  if(idx == A.size()) {
    cout << value << endl;
    return (true);
  }

  int end = (ue ? 9 : A[idx] - '0');
  for(int i = end; i >= 0; i--) {
    if(i < last) continue;
    if(free == false && i == 0) {
      if(rec(i, idx + 1, false, ue | (i != end), value * 10 + i)) return (true);
    } else {
      if(rec(i, idx + 1, true, ue | (i != end), value * 10 + i)) return (true);
    }
  }
  return (false);
}

void solve()
{
  cin >> A;
  rec(0, 0, 0, 0, 0);
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
