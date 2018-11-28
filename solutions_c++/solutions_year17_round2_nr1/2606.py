#include <bits/stdc++.h>
using  namespace std ;

int t ,cs,  n, k ;
double d , s , m , ans , mt ;
int main()
{
        freopen("in.txt","r" , stdin ) ;
        freopen("out.txt","w" , stdout ) ;

        cin >> t ;

        while( cs< t )
        {
            cs++ ;
            scanf("%lf %d",&d,&n ) ;
            mt = 0 ;
            for( int i = 0 ; i < n ; i++ )
            {
                scanf("%lf %lf",&m,&s ) ;
                double t = ( d - m ) / s ;
                if( mt <= t ) mt = t ;
            }
            printf("Case #%d: %0.6lf\n", cs , d / mt  ) ;
        }





return 0 ;
}
