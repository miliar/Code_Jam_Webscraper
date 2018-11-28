#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <utility>
#include <queue>
#include <unordered_set>
#include <cstdlib>
#include <cassert>

using namespace std;

int solve(string s, int k) {
  string target = string(s.size(), '+');

  queue<pair<string, int>> q;
  q.push(make_pair(s, 0));
  unordered_set<string> us;
  us.insert(s);

  while (!q.empty()) {
    auto t = q.front();
    q.pop();
    if (t.first == target) return t.second;
    auto& ts = t.first;
    // cout << ts << endl;

    for (int i = 0; i < ts.size(); i++) {
      if (ts[i] == '+' || i+k > ts.size()) continue;
      auto tsc = ts;
      for (int j = 0; j < k; j++) {
        tsc[i+j] = (ts[i+j] == '+' ? '-' : '+');
      }
      if (us.find(tsc) == us.end()) {
       // cout << ts << "->" << tsc << endl;
       q.push(make_pair(tsc, t.second+1));
       us.insert(tsc);
      }
    }
  }
  return 1e9;
}

int solveBetter(string s, int k) {
  string target = string(s.size(), '+');
  int steps = 0;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] == '+' || i+k > s.size()) continue;
    for (int j = 0; j < k; j++) {
      s[i+j] = (s[i+j] == '+' ? '-' : '+');
    }
    steps++;
  }
  if (s != target) return 1e9;
  return steps;
}

string getStr(int mask, int len) {
  string s;
  s.resize(len);
  for (int i = 0; i < len; i++) {
    if (mask & (1<<i)) {
      s[i] = '+';
    } else s[i] = '-';
  }
  return s;
}

int assertCheck() {
  srand(time(NULL));
  int tests = 100;
  for (int test = 0; test < tests; test++) {
    int mask = rand() % (1<<20);
    for (int k = 2; k < 20; k++) {
      string s = getStr(mask, 20);
      cout << "Checking " << s << " " << k << endl;
      assert(solveBetter(s, k) == solve(s, k));
    }
  }
  return 0;
}

// #define TEST

int main() {
#ifdef TEST
  assertCheck();
#else
  int n;
  cin >> n;
  int i = 0;
  while (n--) {
    i++;
    string s;
    int k;
    cin >> s;
    cin >> k;
    int res = solve(s, k);
    cout << "Case #" << i << ": ";
    if (res < 1e9)
      cout << res << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
#endif
  return 0;
}
