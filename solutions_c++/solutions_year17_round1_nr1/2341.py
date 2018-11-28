#include <bits/stdc++.h>
#define rep( i, a, b ) for( i=a; i<b; i++ )
#define dwn( i, a, b ) for( i=a; i>=b; i--)
#define X first
#define Y second
#define fi first
#define se second
#define mp make_pair
#define pb push_back
using namespace std;
typedef long long ll;
typedef pair< int, int > pii;
typedef vector< int > vi;
const int MAXN = 60;

char g[ MAXN ][ MAXN ];
bool ori[ MAXN ][ MAXN ];

bool dfs(int u, int d, int l, int r) {
  int i, j;
  char tmp[2] = {0};
  int rn[MAXN] = {0};
  int cn[MAXN] = {0};
  rep( i, u, d ) rep( j, l, r ) {
    rn[i] += ( g[ i ][ j ] != '?' );
    cn[j] += ( g[ i ][ j ] != '?' );
    if (g[i][j] != '?')
      if (!tmp[0]) tmp[0] = g[i][j];
      else if(!tmp[1] && g[i][j] != tmp[0])
        tmp[1] = g[i][j];
  }
  int rs[MAXN] = {0};
  int cs[MAXN] = {0};
  rs[ u ] = rn[ u ];
  rep(i, u + 1, d) rs[i] += rn[i] + rs[i - 1];
  cs[ l ] = cn[ l ];
  rep(j, l + 1, r) cs[j] += cn[j] + cs[j - 1];
  if ( rs[ d - 1 ] == 1 || cs[ r-1 ]==1) {
    rep(i, u, d) rep(j, l, r) g[i][j] = tmp[0];
    return true;
  }
  else {
    int flag;
    rep(i, u, d - 1)
      if (rs[i] > 0 && rs[i + 1] > rs[i]) {
        bool ans1 = dfs(u, i+1, l, r),
          ans2 = dfs(i+1, d, l, r);
        return ans1 && ans2;
      }
    rep(i, l, r - 1)
      if (cs[i] > 0 && cs[i + 1] > cs[i]) {
        bool ans1 = dfs(u, d, l, i+1);
        bool ans2 = dfs(u, d, i + 1, r);
        return ans1 && ans2;
      }
  }
}
bool chk( int u, int x, int y, int ind ) {
  int i;
  if ( ind ) {
    rep( i, x, y ) {
      if ( g[ i ][ u ] != '?' ) {
        return false;
      }
    }
  } else {
    rep( i, x, y ) {
      if ( g[ u ][ i ] != '?' ) {
        return false;
      }
    }
  }

  return true;
}
main() {
  int T;
  int r, c;
  int Case;
  cin >> T;
  rep( Case, 1, T + 1 ) {
    int i, j, k;
    memset( ori, false, sizeof( ori ) );
    cin >> r >> c;
    rep( i, 0, r ) {
      scanf( "%s", g[ i ] );
      rep( j, 0, c ) {
        if ( g[ i ][ j ] != '?' ) {
          ori[ i ][ j ] = true;
        }
      }
    }
    printf("Case #%d:\n", Case);
    /*rep( i, 0, r ) rep( j, 0, c ) {
      if ( ori[ i ][ j ] ) {
        int u = i + 1;
        while( u >= 0 && chk( u, j, j + 1, 0 ) ) {
          g[ u ][ j ] = g[ i ][ j ];
          u++;
        }
        u++;
        int d = j - 1;
        while( d >= 0 && chk( d, u, i + 1, 1 ) ) {
          rep( k, u, i + 1 ) {
            g[ k ][ d ] = g[ i ][ j ];
          }
          d--;
        }
        d++;
        int u1 = i + 1;
        while( u1 < r && chk( u1, d, j + 1, 0 ) ) {
          rep( k, d, j + 1 ) {
            g[ u1 ][ k ] = g[ i ][ j ];
          }
          u1++;
        }
        u1--;
        int d1 = j + 1;
        while( d1 < c && chk( d1, u, u1 + 1, 1 ) ) {
          rep( k, u, u1 + 1 ) {
            g[ k ][ d1 ] = g[ i ][ j ];
          }
          d1++;
        }
      }
      }*/
    dfs(0, r, 0, c);
    rep( i, 0, r ) {
      rep( j, 0, c ) {
        printf( "%c", g[ i ][ j ] );
      }
      printf( "\n" );
    }

  }

  return 0;
}
