#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std ;

int a[1001];
int cnt[4];
int f[105][105][105][4] = {0};

int main() {
        int T , N , P ;

        scanf("%d",&T);
        for ( int test = 0 ; test < T ; ++test ) {
                scanf("%d%d",&N,&P);
                cnt[0] = cnt[1] = cnt[2] = cnt[3] = 0 ;
                for ( int i = 0 ; i < N ; ++i ) {
                        scanf("%d",&a[i]);
                        cnt[a[i]%P] ++ ;
                }
                int ans = 0;
                for ( int i = 0 ; i <= cnt[1] ; ++i )
                        for ( int j = 0 ; j <= cnt[2] ; ++j )
                                for ( int k = 0 ; k <= cnt[3] ; ++k ) {
                                        for ( int l = 0 ; l < 4 ; ++l )
                                                f[i][j][k][l] = 0 ;
                                }
                for ( int i = 0 ; i <= cnt[1] ; ++i )
                        for ( int j = 0 ; j <= cnt[2] ; ++j )
                                for ( int k = 0 ; k <= cnt[3] ; ++k ) {

                                        for ( int l = 0 ; l < 4 ; ++l ) {
                                                
                                                int c = 1 ;
                                                f[i+1][j][k][ (l+c)%P ] = max( f[i][j][k][l] + (l == 0) , f[i+1][j][k][ (l+c)%P] );
                                                c = 2 ;
                                                f[i][j+1][k][ (l+c)%P ] = max( f[i][j][k][l] + (l == 0) , f[i][j+1][k][ (l+c)%P] );
                                                c = 3 ;
                                                f[i][j][k+1][ (l+c)%P ] = max( f[i][j][k][l] + (l == 0) , f[i][j][k+1][ (l+c)%P] );
                                                
                                                if ( i == cnt[1] && j == cnt[2] && k == cnt[3] )
                                                        ans = max( ans, f[i][j][k][l] );
                                        }
                                
                                }
                ans += cnt[0];
                printf("Case #%d: %d\n",test+1,ans);
        }
        
        return 0;
}
