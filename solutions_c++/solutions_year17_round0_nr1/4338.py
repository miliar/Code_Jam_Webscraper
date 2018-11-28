#include <bits/stdc++.h>

using namespace std;

void solve(string s, int n, int t) {
  int i;
  int steps = 0;
  for (i = 0; i < s.size()-n+1; i++) {
    if (s[i] == '+') {
      continue;
    } else {
      for (int j = 0; j < n; j++) {
        if (s[i+j] == '+')
          s[i+j] = '-';
        else
          s[i+j] = '+';
      }
      steps++;
    }
  }
  bool neg = false;
  for (; i < s.size(); i++) {
    if (s[i] == '-') {
      neg = true;
      break;
    }
  }
  if (neg)
    cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
  else
    cout << "Case #" << t+1 << ": " << steps << endl;
}


int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    string s; int n;
    cin >> s >> n;
    bool neg = false;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '-') {
        neg = true;
        break;
      }
    }
    if (!neg) {
      cout << "Case #" << t+1 << ": 0" << endl;
    } else {
      solve(s, n, t);
    }
  }
    
  return 0;
}
