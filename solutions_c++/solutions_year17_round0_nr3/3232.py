#include<bits/stdc++.h>
using namespace std;
#define si( n ) scanf("%d",&n)
#define FOR( i, n ) for( int i = 0; i < n; i++ )
#define FOR1( i, n ) for( int i = 1; i <= n; i++ )
#define pb push_back
#define fst first
#define snd second

typedef long long ll;
typedef pair<ll, ll> pll;
const ll inf = 1e18 + 100;

pll solve( ll n, ll k ){
    ll tmp = k;
    ll tp = 1;
    int cnt = 0;
    while( tmp > 1 ){
        tmp /= 2;
        cnt ++;
        tp *= 2;
    }
    ll p = 1, q = 0;//sma, big
    ll sma = n;
    ll big = n + 1;
    for( int i = 0; i < cnt; i ++ ){
        ll nsma = ( sma - 1 ) / 2;
        ll nbig = nsma + 1;
        ll np = p, nq = q;
        if( sma - 1 - nsma == nsma ) np += p;
        else nq += p;
        if( q > 0 ){
            if( sma / 2 == nsma ) np += q;
            else nq += q;
        }
        p = np; q = nq;
        sma = nsma; big = nbig;
    }
    ll idx = k - tp + 1;
    ll x;
    if( idx > q )
        x = sma;
    else x = big;
    sma = ( x - 1 ) / 2;
    big = x - 1 - sma;
    return { big, sma };
}


int main(){
    int T; si( T );
    FOR1( tt, T ){
        ll n, k;
        cin >> n >> k;
        pll ans = solve( n, k );
        printf("Case #%d: %lld %lld\n", tt, ans.fst, ans.snd );
    }
}
