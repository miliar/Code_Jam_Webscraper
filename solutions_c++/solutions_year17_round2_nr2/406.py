#include <bits/stdc++.h>
using namespace std;

int i, n, r, o, y, g, b, v;

bool check(string ans) {
  for(int i = 0; i < ans.size(); ++i)
    if(ans[i] == ans[(i + 1) % ans.size()]) return 0;
  return 1;
}

string get(char first, char last, int r, int y, int b) {
  string ans;
  ans += first;

  while(r + y + b > 0) {
    if(first == 'R') {
      if(y + b == 0) return "RR";
      if(y > b) --y, ans += 'Y', first = 'Y';
      else --b, ans += 'B', first = 'B';

      continue;
    }

    if(first == 'Y') {
      if(r + b == 0) return "RR";
      if(r > b) --r, ans += 'R', first = 'R';
      else --b, ans += 'B', first = 'B';

      continue;
    }

    if(first == 'B') {
      if(y + r == 0) return "RR";
      if(y > r) --y, ans += 'Y', first = 'Y';
      else --r, ans += 'R', first = 'R';

      continue;
    }
  }

  ans += last;

  return ans;
}

string solve(int r, int y, int b) {
  if(r) {
    if(y) {
      string ans = get('R', 'Y', r - 1, y - 1, b);
      if(check(ans)) return ans;
    }

    if(b) {
      string ans = get('R', 'B', r - 1, y, b - 1);
      if(check(ans)) return ans;
    }

    if(r > 1) {
      string ans = get('R', 'R', r - 2, y, b);
      if(check(ans)) return ans;
    }
  }

  if(y) {
    if(r) {
      string ans = get('Y', 'R', r - 1, y - 1, b);
      if(check(ans)) return ans;
    }

    if(b) {
      string ans = get('Y', 'B', r, y - 1, b - 1);
      if(check(ans)) return ans;
    }

    if(y > 1) {
      string ans = get('Y', 'Y', r, y - 2, b);
      if(check(ans)) return ans;
    }
  }

  if(b) {
    if(r) {
      string ans = get('B', 'R', r - 1, y, b - 1);
      if(check(ans)) return ans;
    }

    if(y) {
      string ans = get('B', 'Y', r, y - 1, b - 1);
      if(check(ans)) return ans;
    }

    if(b > 1) {
      string ans = get('B', 'B', r, y, b - 2);
      if(check(ans)) return ans;
    }
  }

  return "IMPOSSIBLE";
}

int main() {
  ifstream cin("test1.in");
  ofstream cout("test.out");
  ios_base::sync_with_stdio(0);

  int test, tests;
  cin >> tests;
  for(test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";

    cin >> n >> r >> o >> y >> g >> b >> v;
    cout << solve(r, y, b) << '\n';
  }

  return 0;
}