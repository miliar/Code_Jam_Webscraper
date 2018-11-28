#include <bits/stdc++.h>

using namespace std;

#define SZ(x) ((int) x.size())

string fu(string str) {
  if (is_sorted(str.begin(), str.end())) {
    return str;
  }
  int firstUnsortedIdx = SZ(str);
  for (int i = SZ(str) - 1; i > 0; --i) {
    if (str[i] < str[i - 1]) {
      firstUnsortedIdx = i;
    }
  }
  int idxToBeChanged = firstUnsortedIdx - 1;
  while (idxToBeChanged > 0 && str[idxToBeChanged] == str[idxToBeChanged - 1]) {
    --idxToBeChanged;
  }
  --str[idxToBeChanged];
  for (int i = idxToBeChanged + 1; i < str.size(); ++i) {
    str[i] = '9';
  }
  if (str[0] == '0') {
    str = str.substr(1);
  }
  return str;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL), cout.tie(NULL);

  freopen("B-large.in", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  int t;
  cin >> t;
  for (int caseId = 1; caseId <= t; ++caseId) {
    cout << "Case #" << caseId << ": ";
    string str;
    cin >> str;
    cout << fu(str) << '\n';
  }

  return 0;
}

