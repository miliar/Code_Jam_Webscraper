#include <bits/stdc++.h>
using namespace std;

void solve() {
  string num; cin >> num;
  if (num.size() == 1) {
    cout << num;
    return;
  }
  int i;
  for (i = 0; i + 1 < num.size(); i++) {
    if (num[i] > num[i + 1]) {
      break;
    }
  }
  if (i + 1 >= num.size()) {
    cout << num;
    return;
  }
  while (i > 0 && num[i] == num[i - 1]) i--;
  num[i]--;
  for (int j = i + 1; j < num.size(); j++) num[j] = '9';
  if (num[0] == '0') num = num.substr(1, num.size() - 1);
  cout << num;
}

int main() {
  ios_base::sync_with_stdio(false);
  int tt; cin >> tt;
  for (int t = 1; t <= tt; t++) {
    cout << "Case #" << t << ": ";
    solve();
    cout << '\n';
  }
}
