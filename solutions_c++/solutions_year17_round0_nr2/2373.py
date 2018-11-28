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
    cout << "Case #" << test << ": ";

    string s;
    cin >> s;

    string current = s;

    char last = '0';

    REP (i, s.size()) {
      FOR (d, last, '9') {
        FORN (j, i, s.size()) current[j] = d;
        if (current > s) break;
        last = d;
      }
      current[i] = last;
    }

    ll res = 0;
    REP (i, current.size()) res = res * 10 + current[i] - '0';
    cout << res << endl;
  }
}

