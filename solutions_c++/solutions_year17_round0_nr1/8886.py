#include <bits/stdc++.h>

using namespace std;

int a[1234];
int s[1234];
int n;
int k;
int sum;
int ans;
string str;

void sol() {
  cin >> str >> k;
  n = (int)str.size();
  for(int i = 0; i < n; i++) {
    a[i] = (str[i] == '+') ? 1 : 0;
  }

  sum = 0;
  ans = 0;
  memset(s, 0, sizeof s);

  for(int i = 0; i < n; i++) {
    s[i] = (a[i] + sum) % 2 != 1;
    sum += s[i] - (i >= k - 1 ? s[i - k + 1] : 0);
    ans += s[i];
    if(i > n - k && s[i] != 0) {
      cout << "IMPOSSIBLE" << '\n';
      return;
    }
  }
  cout << ans << '\n';
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    sol();
  }

  return 0;
}
