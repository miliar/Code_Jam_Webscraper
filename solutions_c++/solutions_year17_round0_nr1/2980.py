#include <iostream>
using namespace std;

string s;
int k;

void flip(int from, int to) {
  for(;from <= to; from++) {
    s[from] = s[from] == '-' ? '+' : '-';
  }
}

void solve() {
  cin >> s >> k;

  int res = 0;
  for(int i = 0; i < (int)s.size() + 1 - k; i++) {
    if(s[i] == '-') {
      res ++;
      flip(i, i+k-1);
    }
  }

cout << (find(s.begin() + s.size() - k + 1, s.end(), '-') == s.end() ? to_string(res) : "IMPOSSIBLE") << endl;

}

int main () {
  int t;

  cin >> t;
  for(int i = 1; i <= t; i++)
  {
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}
