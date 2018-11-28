#include <bits/stdc++.h>

using namespace std;

typedef long long ll ;


int t ;
ll d ;
int n ;
ll a[1111], b[1111];

int main()
{
    freopen("A-large.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    scanf("%d",&t) ;
    for ( int ctr = 1 ; ctr <= t; ctr++ )
    {
        scanf("%I64d%d",&d,&n) ;
        for ( int i = 0 ; i < n; i++ )
            scanf("%I64d%I64d",&a[i],&b[i]);
        double l = 0 , r = 1e15 , m ;
        for ( int i = 0 ; i < 150 ; i++ )
        {
            m = (l+r)/2 ;
            bool kk = 1 ;
            for ( int j = 0 ; j < n ; j++ )
            {
                if ( b[j]-m >= -1e-9 ) continue ;
                double d2 = -m*a[j] + b[j]*0 ;
                d2 /= (b[j]-m) ;

                if ( d2-d >= -1e-9) ;
                else kk = 0 ;
            }
            if ( kk )
                l = m;
            else r = m;
        }
        printf("Case #%d: %.9f\n",ctr,l) ;
    }
    return 0;
}
