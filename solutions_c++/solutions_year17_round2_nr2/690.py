#include<bits/stdc++.h>
using namespace std;

int c[10];
int n;

int step[6] = {0, 2, 4, 1, 3, 5};
char mp[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int ans[1005];
int st;

bool ok(int a, int b) {
  if ( a > b ) swap(a, b);
  return !( ( a == b ) || ((a+1)%6==b ) );
}

bool res = false;

void solve() {
  res = 0;
  int prev;
  for ( int i = 0 ; i < n ; i++ ) {
    if ( c[i] > 0 ) {
      st = i;
      c[i]--;
      ans[0] = i;
      prev = i;
      break;
    }
  }
  for ( int i = 1 ; i < n ; i++ ) {
    int mx = -1, u = -1;
    for ( int j = 0 ; j < 6 ; j++ ) {
      if ( ok(prev, j) && c[j] > 0 ) {
        if ( c[j] > mx ) {
          mx = c[j];
          u = j;
        }
      }
    }
    if ( u == -1 ) {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
    c[u]--;
    ans[i] = u;
    prev = u;

  }
  if ( prev == st ) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  for ( int i = 0 ; i < n ; i++ ) {
    cout << mp[ans[i]];
  }
  cout << endl;
}

int main() {
  freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);
  int T, kase = 0;
  cin >> T;
  while ( T-- ) {
    cin >> n;
    for ( int i = 0 ; i < 6;  i++ ) cin >> c[i];
      printf("Case #%d: ", ++kase);
    solve();

  }

}
