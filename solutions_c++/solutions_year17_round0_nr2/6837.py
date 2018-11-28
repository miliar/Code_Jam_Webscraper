#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 10;

void check(const string& str) {
  char pidx = str[0];
  for (auto &ch : str) {
    if (ch < pidx) assert(false);
    pidx = ch;
  }
  return;
}

int main() {
  ios_base::sync_with_stdio(false);
  //cin.tie(NULL);
  int T; cin >> T;
  for (int qq = 1; qq <= T; ++qq) {
    cout << "Case #" << qq << ": ";
    string num, ans;
    cin >> num;
    const int n = num.length();
    char pidx = num[0];
    ans.push_back(pidx);
    int idx = 1;
    while (idx < n && num[idx] >= pidx) {
      ans.push_back(num[idx]);
      pidx = num[idx];
      ++idx;
    }
    if (idx < n) {
      --idx;
      while (idx > 0 && num[idx] == num[idx - 1]) {
        --idx;
        ans.pop_back();
      }
      ans[idx]--;
      for (idx++; idx < n; idx++) ans.push_back('9'); 
    }
    check(ans);
    cout << stoll(ans) << "\n";
  }
  return 0;
}
