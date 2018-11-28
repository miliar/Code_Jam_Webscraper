#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl
#define PB push_back
#define MP make_pair

int main() {
  int ntest;
  cin >> ntest;

  FOR (test, 1, ntest) {
    string s;
    int k;
    cin >> s >> k;

    int res = 0;

    REP (i, s.size() - k + 1) {
      if (s[i] == '-') {
        res++;
        FORN (j, i, i + k) {
          s[j] = '+' + '-' - s[j];
        }
      }
    }

    REP (i, s.size()) if (s[i] == '-') res = -1;

    cout << "Case #" << test << ": ";
    if (res == -1) cout << "IMPOSSIBLE" << endl;
    else cout << res << endl;
  }
}

