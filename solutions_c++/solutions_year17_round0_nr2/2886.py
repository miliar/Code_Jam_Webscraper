#include <bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false); cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

const int inf = 100;
char dp[20][20][5];

int f(int index, int last, bool is_top, string &n) {
  if (index == n.size()) {
    return 0;
  }

  if (dp[index][last][is_top] == inf) {
    dp[index][last][is_top] = -1;

    int large = 9;
    if (is_top) large = n[index] - '0';

    for (int digit = large; digit >= last; --digit) {
      int next = f(index + 1, digit, is_top and (digit == n[index] - '0'), n);
      if (next != -1) {
        dp[index][last][is_top] = digit;
        break;
      }
    }
  }

  return dp[index][last][is_top];
}

int main() { IO;
  int t;
  cin >> t;

  for (int ncase = 1; ncase <= t; ++ncase) {
    cout << "Case #" << ncase << ": ";

    string n;
    cin >> n;

    memset(dp, inf, sizeof dp);
    string ans;
    int last = 0;
    bool is_top = true;

    for (int index = 0; index < n.size(); ++index) {
      int digit = f(index, last, is_top, n);
      is_top = is_top and (digit == n[index] - '0');
      last = digit;

      if (last or ans.size()) {
        ans.push_back(digit + '0');
      }
    }

    cout << ans << endl;
  }

  return 0;
}
