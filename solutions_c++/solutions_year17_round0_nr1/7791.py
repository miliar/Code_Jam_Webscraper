#include <iostream>
#include <algorithm>
using namespace std;

const int INF = 1000000000;

int k;
int ans = INF;

string flip(string str, int index) {
  if(index < k - 1) return str;
  for(int i = index ; i > index - k ; i--) {
    if(str[i] == '1') str[i] = '0';
    else str[i] = '1';
  }
  return str;
}

void f(int cur_index, string s, int total_flips) {
  bool complete = true;
  for(auto x: s) {
    if(x != '1') {
      complete = false;
      break;
    }
  }
  if(complete) {
    ans = min(ans, total_flips);
    return;
  }
  if(cur_index < k - 1) return;
  f(cur_index - 1, s, total_flips);
  f(cur_index - 1, flip(s, cur_index), total_flips + 1);
}

void solve() {
  ans = INF;
  string ss; cin >> ss;
  string s = "";
  for(int i = 0 ; i < ss.size() ; i++) {
    if(ss[i] == '+') s += '1';
    else s += '0';
  }
  int n = (int)s.size();
  cin >> k;
  string flipped = flip(s, n - 1);
  f(n - 1, s, 0);
  f(n - 1, flipped, 1);
}

int main() {
  int t; cin >> t;
  for(int qq = 1 ; qq <= t ; qq++) {
    solve();
    if(ans == INF) cout << "Case #" << qq << ": IMPOSSIBLE\n";
    else cout << "Case #" << qq << ": " << ans  << "\n";
  }
}
