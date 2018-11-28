#include<bits/stdc++.h>
using namespace std;
#define si( n ) scanf("%d", &n )
#define FOR( i, n ) for( int i = 0; i < n; i++ )
#define FOR1( i, n ) for( int i = 1; i <= n; i++ )
#define pb push_back
typedef long long ll;

bool istidy( ll x ){
    ll digit[ 20 ] = { 0 };
    int idx = 0;
    ll tmp = x;
    while( tmp > 0 ){
            digit[ idx ] = tmp % 10;
        tmp /= 10;
        idx++;
    }
    for( int i = idx; i > 0; i-- ){
        if( digit[ i ] > digit[ i - 1 ] ){
            return false;
        }
    }
    return true;
}

ll adjust( ll x ){
    ll digit[ 20 ] = { 0 };
    int idx = 0;
    ll tmp = x;
    while( tmp > 0 ){
        digit[ idx ] = tmp % 10;
        tmp /= 10;
        idx++;
    }
    for( int i = idx; i > 0; i-- ){
        if( digit[ i ] > digit[ i - 1 ] ){
            for( int j = i - 2; j >= 0; j -- ) digit[ j ] = 9;
            digit[ i - 1 ] --;
            if( digit[ i - 1 ] < 0 ){
                digit[ i ] -= 1;
                digit[ i - 1 ] += 10;
            }
            break;
        }
    }
    tmp = 0;
    ll tp = 1;
    FOR( i, idx ){
        tmp += tp * digit[ i ];
        tp *= 10;
    }
    return tmp;
}

int main(){
    int T; si( T );
    FOR1( tt, T ){
        ll n; cin >> n;
        while( istidy( n ) == false ) n = adjust( n );
        printf("Case #%d: %lld\n", tt, n );
    }
    return 0;
}
