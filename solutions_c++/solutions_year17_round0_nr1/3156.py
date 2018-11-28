#include <cassert>
#include <cstring>

#include <algorithm>
#include <iostream>

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define REP(i,n) FOR(i,0,n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

using namespace std;

int main(void) {
  int ntc; cin >> ntc;
  REP(itc, ntc) {
    cout << "Case #" << itc+1 << ": ";
    string s; cin >> s;
    int k; cin >> k;
    int n = s.size();

    int sol = 0;
    REP(i, n-k+1)
      if (s[i] == '-') {
        ++sol;
        REP(j, k) s[i+j] = (s[i+j] == '+') ? '-' : '+';
      }

    if (s != string(n, '+'))
      cout << "IMPOSSIBLE";
    else
      cout << sol;
    cout << endl;
  }
  return 0;
}
