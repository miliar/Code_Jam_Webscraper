#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define size(n) ( int( n.size() ) )
#define sqr(n) ( (n) * (n) )

using namespace std;

typedef long double ld;

const int N = 100;
ld f[N][N][N];
int r[N], h[N];

vector < pair < int, int > > q;

int cmp( int x, int y ){
    if ( r[x] < r[y] ){
        swap( r[x], r[y] );
        swap( h[x], h[y] );
        return true;
    }
    return false;
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases, t, n, i, j, k, cnt;
    scanf("%d",&t);
    for( cases = 1; cases <= t; cases++ ){
        q.clear();
        scanf("%d %d",&n,&k);
        for ( i = 1; i <= n; i++ ){
            scanf("%d %d",&r[i],&h[i]);
            q.pb( mp( r[i], h[i] ) );
        }
        sort( q.begin(), q.end() );
        for ( i = 1; i <= n; i++ ){
            r[i] = q[i-1].first;
            h[i] = q[i-1].second;
        }
        for ( i = 1; i <= n; i++ ){
            for ( j = n + 1; j >= i + 1; j-- ){
                for ( cnt = 0; cnt <= k; cnt++ ){
                    f[i][j][cnt] = 0.0;
                    if ( cnt != 0 ){
                        ld add = f[i-1][i][cnt-1] + 2 * M_PI * ( r[i] + 0.0 ) * ( h[i] + 0.0 );
                        if ( j == n + 1 ){
                            add += M_PI * ( r[i] + 0.0 ) * ( r[i] + 0.0 );
                        }
                        f[i][j][cnt] = max( f[i][j][cnt], add );
                    }
                    f[i][j][cnt] = max( f[i][j][cnt], f[i-1][j][cnt] );
                }
            }
        }
        cout << "Case #" << cases << ": ";
        cout << fixed << setprecision(15) << f[n][n+1][k] << endl;
    }


    return 0;
}
