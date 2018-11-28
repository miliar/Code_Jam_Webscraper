#include<bits/stdc++.h>
using namespace std;

char s[1005];
int k;

void input() {
  cin >> s >> k;
}

int dp(int idx, char cp[]) {

  if ( idx == k - 2 ) {
    for ( int i = idx ; i >= 0 ; i-- ) {
      if ( cp[i] == '-' ) return -1000000;
    }
    return 0;
  }

  if ( cp[idx] == '+' ) return dp(idx - 1, cp);
  else {

    for ( int i = idx ; i > idx - k ; i-- ) {
      cp[i] = (cp[i] == '+') ? '-' : '+';
    }

    return dp(idx - 1, cp) + 1;
  }
}

void solve() {
  int n = strlen(s);
  int res = dp(n - 1, s);
  if ( res >= 0 ) {
    cout << res << endl;
  } else {
    cout << "IMPOSSIBLE" << endl;
  }

}


int main() {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
  int T, kase = 0;
  cin >> T;
  while (T--) {
    input();
    cout << "Case #" << ++kase << ": ";
    solve();
  }

}
