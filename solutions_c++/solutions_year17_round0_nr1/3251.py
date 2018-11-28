#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl

#define SIZE(a) ((int) a.size())

typedef pair<int, int> pii;

int solve(string s, int k) {
  int n = (int) s.size();
  int res = 0;

  for (int i = 0; i + k - 1 < n; i++) {
    if (s[i] == '-') {
      res ++;
      for (int j = i; j < i + k; j++) {
        s[j] = s[j] == '-' ? '+' : '-';
      }
    }
  }

  for (int i = n - k + 1; i < n; i++) {
    if (s[i] == '-') {
      return -1;
    }
  }

  return res;
}

int main() {
  int t;
  cin >> t;

  FOR (i, 1, t) {
    string s;
    int k;
    cin >> s >> k;

    int res = solve(s, k);
    cout << "Case #" << i << ": ";

    if (res == -1) {
      cout << "IMPOSSIBLE";
    } else {
      cout << res;
    }

    cout << endl;
  }

  return 0;
}
