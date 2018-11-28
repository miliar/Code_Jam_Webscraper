#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std ;

int cnt[3];
int a[1001], b[1001];

int get(int a, int b ) {
        return a/b + ((a%b)!=0);
}

int main() {
        int T ;

        scanf("%d",&T);
        for ( int test = 0 ; test < T ; ++test ) {
                int N,M,C;
                scanf("%d%d%d",&N,&C,&M);

                cnt[0] = cnt[1] = cnt[2] = 0 ;
                for ( int i = 0 ; i <= N ; ++i )
                        a[i] = b[i] = 0 ;

                for ( int i = 0 ; i < M ; ++i ) {
                        int pos, buyer;
                        scanf("%d%d",&pos,&buyer);
                        cnt[buyer] ++ ;
                        if ( buyer == 1 )
                                a[pos] ++ ;
                        else
                                b[pos] ++ ;

                }
                if ( C != 2 ) continue ;
                
                int ans = 0;
                int sum = 0 ;
                int ans2 = 0 ;

                for ( int i = 1 ; i <= N ; ++i ) {
                        sum += a[i] + b[i] ;
                        if ( get(sum,i) > ans )
                                ans = get(sum,i);
                }
                ans = max( ans, max(cnt[1], cnt[2]));

                int r = 0 , last = 0 ;
                for ( int i = N ; i > 0 ; --i ) {
                        ans2 += max( 0, a[i]+b[i]-ans);
                }
                
                printf("Case #%d: %d %d\n",test+1,ans,ans2);
        }
        
        return 0;
}
