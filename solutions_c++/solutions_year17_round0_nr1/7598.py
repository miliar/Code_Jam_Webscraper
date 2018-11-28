#include <bits/stdc++.h>

using namespace std;

#define ios        ios_base::sync_with_stdio(false); cin.tie(false); cout.tie(false);
#define eps 1e-9

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template < class T > T power(T N , T P) { return (P == 0) ?  1 : N * power(N , P - 1); }


typedef long long ll ;


/// S , E  , N , W
//int rr [] = {1 ,0,-1, 0};
//int cc [] = {0 ,1, 0,-1};
///S , SE , E , NE , N , NW , W , SW
//int rr [] = {1 ,1 ,0,-1,-1,-1, 0, 1};
//int cc [] = {0 ,1 ,1 ,1, 0,-1,-1,-1};
///Knight Direction
int rr[]={2 ,1 ,-1,-2,-2,-1, 1, 2};
int cc[]={1 ,2 , 2, 1,-1,-2,-2,-1};

//#define Maxi 65005

//bool siv[Maxi];
//ll sz = 0;
//ll prime[6709];
//ll cnt = 0 ;
//
//void is_prime()
//{
//    ll n = sqrt(Maxi);
//    prime[sz++] = 2;
//    for(ll i = 3 ; i < n ; i += 2) if(!siv[i]) for(ll j = i * i ; j < Maxi ; j += (2 * i)) siv[j] = true;
//    for(ll i = 3 ; i < Maxi ; i += 2) if(!siv[i])   prime[sz++] = i;
////    cout << prime[sz-1] << endl ;
////    cout << sz << endl ;
//}
//
//ll bigmod(ll num , ll p , ll mod)
//{
//    ll sum = 1 , temp = num;
//    while(p)
//    {
//        if(p & 1) sum = (sum * temp) % mod;
//        temp = (temp * temp) % mod; p = p >> 1;
//    }
//    return sum;
//}


int main()
{
    freopen("in.txt", "r", stdin) ;
    freopen("out.txt", "w", stdout) ;

    int tst, l, cas = 0, k , cnt ;
    string a, b ;
    cin >> tst ;
    while(tst--)
    {
        cin >> a >> k ;
        k-- ;
        b = a;
        int posi = 0, neg = 0, cnt = 0 ;
        l = a.size() ;
        for(int i = 0; i < l - k; i++ )
        {
            if( a[i] == '-' )
            {
                for( int j = i ; j <= i + k; j++ )
                {
                    if( a[j] == '-' )
                        a[j] = '+' ;
                    else
                        a[j] = '-' ;
                }
                cnt++ ;
//                puts("yes") ;
            }
//            puts("hello") ;
         }
        int fl = 0 ;
        for(int i = 0; i < l; i++ )
        {
            if( a[i] == '-' )
            {
                fl++ ;
                break ;
            }
        }


        a = b ;
        neg = cnt ;
        cnt = 0 ;
        for(int i = l - 1; i - k  >= 0; i-- )
        {
//            puts("loop Hi") ;
            if( a[i] == '-' )
            {
                for( int j = i ;  j >=  i - k ; j-- )
                {
                    if( a[j] == '-' )
                        a[j] = '+' ;
                    else
                        a[j] = '-' ;
                }
//                puts("hi") ;
                cnt++ ;
            }
        }
        int gk = 0 ;
        for(int i = 0; i < l; i++ )
        {
            if( a[i] == '-' )
            {
                gk++ ;
                break ;
            }
        }
        if( !fl && !gk )
            cnt = min(cnt, neg) ;
        else if( !fl && gk )
            cnt = neg ;
        else if( fl && !gk )
            cnt = cnt ;
        else
            cnt = -1 ;
        printf("Case #%d: ", ++cas) ;
        if( cnt != -1 )
            printf("%d\n", cnt) ;
        else
            puts("IMPOSSIBLE") ;
    }
    return 0 ;
}


