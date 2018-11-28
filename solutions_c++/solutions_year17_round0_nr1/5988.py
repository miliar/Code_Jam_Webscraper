#include <bits/stdc++.h>
#define rep( i, a, b ) for( i=a; i<b; i++ )
#define dwn( i, a, b ) for( i=a; i>=b; i-- )
using namespace std;

const int MAXN = 10100;
int T, k;
int tmp;
bool cake[ MAXN ];
char str[MAXN];

int main() {
  int Case;

  cin >> T;
  rep( Case, 0, T ) {
    int i, j;
    int len;
    int st;
    int ans;

    st = 0;
    scanf( "%s", str );
    printf( "Case #%d: ", Case + 1 );
    cin >> k;
    len = strlen( str );
    rep( i, 0, len ) {
      cake[ i ] = ( str[ i ] == '+' );
    }

    rep( i, 0, len - k + 1 ) {
      if ( !cake[ i ] ) {
        rep( j, 0, k ) {
          cake[ i + j ] = ! cake[ i + j ];
        }
        st++;
      }
    }
    bool flag = true;
    rep( i, 0, len ) {
      if ( !cake[ i ] ) {
        printf( "IMPOSSIBLE\n" );
        flag = false;
        break;
      }
    }
    if ( flag ) {
      printf( "%d\n", st );
    }
  }
}
