#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <list>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <stack>
#include <unordered_map>
#include <unordered_set>

#define what_is(x) cout << #x << " is " << x << endl;

using namespace std;

typedef long long ll;

void solve(const string &n, int pos, char minv, string &ans) {
  if (pos == n.size()) {
    ans = string(n);
    return;
  }
  if (n[pos] < minv) {
    ans = "0";
    return;
  }
  string compet2;
  solve(n, pos + 1, n[pos], compet2);
  if (compet2 != "0") {
    ans = compet2;
    return;
  }
  string compet = "0";
  if (n[pos] - 1 >= minv) {
    compet = "";
    for (int i = 0; i < pos; i++) {
      compet.push_back(n[i]);
    }
    compet.push_back(n[pos] - 1);
    for (int i = pos + 1; i < n.size(); i++) {
      compet.push_back('9');
    }
  }
  ans = compet;
  return;
}

int main () {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    string n;
    cin >> n;
    string ans;
    solve(n, 0, '0', ans);
    while (ans.size() && ans[0] == '0') {
      ans.erase(0, 1);
    }
    if (!ans.size()) {
      ans = "0";
    }
    cout << "Case #" << i << ": " << ans << endl;
  }
  return 0;
}
