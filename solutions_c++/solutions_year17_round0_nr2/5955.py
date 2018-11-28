#include <bits/stdc++.h>
#define rep( i, a, b ) for( i=a; i<b; i++ )
#define dwn( i, a, b ) for( i=a; i>=b; i-- )

using namespace std;

const int MAXN = 10010;

int T;
char num[ MAXN ];

int main() {
  int Case;

  cin >> T;
  rep( Case, 0, T ) {
    int i, j, k;
    int len;
    int cur, pre;

    scanf( "%s", num );
    printf( "Case #%d: ", Case + 1 );
    len = strlen( num );
    pre = 0;
    if ( len == 1 ) {
      printf( "%c\n", num[ pre ] );
    } else if ( num[ 1 ] < num[ pre ] ) {
      if ( num[ pre ] == '1' ) {
        rep( i, 0, len - 1 ) {
          printf( "9" );
        }
        printf( "\n" );
      } else {
        printf( "%c", num[ pre ] - 1 );
        rep( i, 0, len - 1 ) {
          printf( "9" );
        }
        printf( "\n" );
      }

    } else {
      rep( cur, 1, len ) {
        if ( num[ cur ] > num[ pre ] ) {
          rep( i, pre, cur ) {
            printf( "%c", num[ i ] );
          }
          pre = cur;
        } else if ( num[ cur ] < num[ pre ] ) {
          if ( num[ pre ] - 1 > '0' ) {
            printf( "%c", num[ pre ] - 1 );
          }
          rep( i, pre + 1, len ) {
            printf("9");
          }
          pre = cur = len;
        }
      }
      rep( i, pre, len ) {
        printf( "%c", num[ i ] );
      }
      printf("\n");
    }
  }
  return 0;
}
