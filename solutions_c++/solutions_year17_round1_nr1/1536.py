#include<bits/stdc++.h>
using namespace std;

int R, C;
char m[30][30];
int ln[1000] = {0};

void fill_vertical() {
  memset(ln, 0, sizeof(ln));
  for ( int i = 0 ; i < R ; i++ ) {
    for ( int j = 0 ; j < C ; j++ ) {
      if ( m[i][j] != '?' && !ln[m[i][j]] ) {
        ln[m[i][j]] = 1;
        for ( int k = j - 1 ; k >= 0 ; k--) {
          if ( m[i][k] == '?' ) m[i][k] = m[i][j], ln[m[i][j]]++;
          else break;
        }
        for ( int k = j + 1 ; k < C ; k++) {
          if ( m[i][k] == '?' ) m[i][k] = m[i][j], ln[m[i][j]]++;
          else break;
        }
      }
    }
  }

}

void fill_horizontal() {

  for ( int i = 0 ; i < R ; i++ ) {
    for ( int j = 0 ; j < C ; j++ ) {
      if ( m[i][j] != '?' ) {
        for ( int far = 1; far + i < R ; far++ ) {
          bool flag = true;
          for ( int k = 0 ; k < ln[m[i][j]] ; k++ ) {
            for ( int r = 0 ; r <= far ; r++ ) {
              if ( m[i + r][j + k] != '?' && m[i + r][j + k] != m[i][j] ) {
                flag = false;
              }
            }
          }
          if ( flag ) {
            for ( int k = 0 ; k < ln[m[i][j]] ; k++ ) {
              for ( int r = 0 ; r <= far ; r++ ) {
                m[i + far][j + k] = m[i][j];
              }
            }
          }
        }


        for ( int far = 1; i - far >= 0 ; far++ ) {
          bool flag = true;
          for ( int k = 0 ; k < ln[m[i][j]] ; k++ ) {
            for ( int r = 0 ; r <= far ; r++ ) {
              if ( m[i - r][j + k] != '?' && m[i - r][j + k] != m[i][j] ) {
                flag = false;
              }
            }
          }
          if ( flag ) {
            for ( int k = 0 ; k < ln[m[i][j]] ; k++ ) {
              for ( int r = 0 ; r <= far ; r++ ) {
                m[i - far][j + k] = m[i][j];
              }
            }
          }
        }
      }
    }
  }

}

void solve() {
  fill_vertical();
  fill_horizontal();

  for ( int i = 0 ; i < R ; i++ ) {
    cout << m[i] << endl;
  }
}

int main() {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
  int T;
  int kase = 0;
  cin >> T;
  while ( T-- ) {
    cin >> R >> C;
    for ( int i = 0 ; i < R ; i++ ) {
      cin >> m[i];
    }
    printf("Case #%d:\n", ++kase);
    solve();
  }

}
