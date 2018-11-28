#include<bits/stdc++.h>
using namespace std;

void solve(char s[]) {
  int len = strlen(s);
  for ( int i = len - 1 ; i >= 1 ; i-- ) {
    if ( s[i - 1] > s[i] ) {

      s[i - 1]--;
      for ( int j = i ; j < len ; j++ ) {
        s[j] = '9';
      }
    }
  }

  bool head = false;
  for ( int i = 0 ; i < len ; i++ ) {
    if ( s[i] != '0' ) {
      head = 1;
      cout << s[i];
    }
    if ( s[i] == '0' && head ) {
      cout << s[i];
    }
  }

}

int main() {
freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);
  int T, kase = 0;
  char s[25];
  cin >> T;
  while ( T-- ) {
    cin >> s;
    printf("Case #%d: ", ++kase);
    solve(s);
    puts("");
  }

}
