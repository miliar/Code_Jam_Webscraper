#include <bits/stdc++.h>

using namespace std;

int fu(string str, int k) {
  queue<int> unFlip;
  int res = 0, flip = 0;
  for (int i = 0; i < str.size(); ++i) {
    if (unFlip.size() && unFlip.front() == i) {
      flip ^= 1, unFlip.pop();
    }
    if (flip != (str[i] == '-')) {
      if (i <= str.size() - k) {
        ++res, flip ^= 1, unFlip.push(i + k);
      } else {
        return INT_MAX;
      }
    }
  }
  return res;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL), cout.tie(NULL);

  freopen("A-large.in", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  int t;
  cin >> t;
  for (int caseId = 1; caseId <= t; ++caseId) {
    int k;
    string str;
    cin >> str >> k;
    int ans = INT_MAX;
    ans = min(ans, fu(str, k));
    reverse(str.begin(), str.end());
    ans = min(ans, fu(str, k));
    cout << "Case #" << caseId << ": ";
    if (ans == INT_MAX) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << ans << '\n';
    }
  }

  return 0;
}

