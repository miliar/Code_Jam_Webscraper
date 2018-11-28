#include<bits/stdc++.h>
using namespace std;
#define si( a ) scanf("%d",&a)
#define FOR( i, n ) for( int i = 0; i < n; i++ )
#define FOR1( i, n ) for( int i = 1; i <= n; i++ )
#define pb push_back
#define fst first
#define snd second

const int maxn = 25 + 5;
char mp[ maxn ][ maxn ];
int r, c;


int rgt[ 30 ];
int lft[ 30 ];
int up[ 30 ];
int down[ 30 ];

void init(){
    FOR( i, 30 ){
        rgt[ i ] = down[ i ] = 0;
        lft[ i ] = up[ i ] = maxn;
    }
}

void print(){
    FOR( i, r ){
        cout << mp[ i ] << endl;
    }
}

void pre(){
    FOR( x, 26 ){
        for( int i = up[ x ]; i <= down[ x ]; i ++ ){
            for( int j = lft[ x ]; j <= rgt[ x ]; j ++ ){
                //printf("change %d %d, %c\n", i, j, x + 'A' );
                mp[ i ][ j ] = 'A' + x;
            }
        }
    }
    print();
}

void solve(){
    FOR( i, r ){
        FOR( j, c ){
            if( mp[ i ][ j ] != '?' ){
                char now = mp[ i ][ j ];
                int tp = j;
                while( tp - 1 >= 0 && mp[ i ][ tp - 1 ] == '?' ){
                    mp[ i ][ tp - 1 ] = now;
                    tp--;
                }
                while( j + 1 < c && mp[ i ][ j + 1 ] == '?' ){
                    mp[ i ][ j + 1 ] = now;
                    j++;
                }
            }
        }
    }
    FOR( i, r ){
        if( mp[ i ][ 0 ] != '?' ){
            for( int pp = i - 1; pp >= 0 ; pp -- ){
                if( mp[ pp ][ 0 ] == '?' ){
                    for( int j = 0; j < c; j++ )
                        mp[ pp ][ j ] = mp[ i ][ j ];
                }
            }
            for( int dd = i + 1; dd < r && mp[ dd ][ 0 ] == '?' ; dd++ ){
                if( mp[ dd ][ 0 ] == '?' ){
                    for( int j = 0; j < c; j++ )
                        mp[ dd ][ j ] = mp[ i ][ j ];
                }
            }
        }
    }
}

int main(){
    int T; si( T );
    FOR1( tt, T ){
        init();
        si( r ); si( c );
        FOR( i, r ){
            cin >> mp[ i ];
        }
        solve();
        printf("Case #%d:\n", tt );
        print();
    }
    return 0;
}
