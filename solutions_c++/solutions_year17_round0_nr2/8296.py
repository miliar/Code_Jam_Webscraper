#include <iostream>
#include <cstdlib>
using namespace std;

string solve(string s) {
  // Base case
  if (s.size() == 1) {
    return s;
  }

  int l = s.size();
  string rec_sol = solve(s.substr(1, l-1));
  if (rec_sol[0] < s[0]) {
    string ans;
    ans += s[0] - 1;
    for (int i = 0; i < l - 1; ++i) {
      ans += '9';
    }
    return ans;
  } else {
    return s[0] + rec_sol;
  }


  // string ans;
  // for (int i = 0; i < l; ++i) {
  //   int cur_dig = (s[i] - '0');
  //   int min_tail = 9;
  //   for (int j = i; j < l; ++j) {
  //     min_tail = min(min_tail, s[j] - '0');
  //   }
  //   if (cur_dig - 1 >= min_tail) {
  //     if ((cur_dig - 1 != 0) || ans.size() != 0)
  //       ans += (cur_dig - 1 + '0');
  //     for (int j = i + 1; j < l; ++j) {
  //       ans += '9';
  //     }
  //     return ans;
  //   } else {
  //     if (min_tail != 0 || ans.size() != 0)
  //       ans += (min_tail + '0');
  //   }
  // }
  // return ans;
}

void tcase(int t) {
  string n;
  cin >> n;
  string ans = solve(n);
  int i = 0;
  while (ans[i] == '0') {
    ++i;
  }
  cout << "Case #" << t << ": ";
  while (i < ans.size())
    cout << ans[i++];
  cout << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    tcase(i);
  }
  return 0;
}
