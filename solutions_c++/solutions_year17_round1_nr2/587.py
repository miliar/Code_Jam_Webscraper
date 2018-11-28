#include<bits/stdc++.h>
using namespace std;
#define si( a ) scanf("%d",&a)
#define FOR( i, n ) for( int i = 0; i < n; i++ )
#define FOR1( i, n ) for( int i = 1; i <= n; i++ )
#define pb push_back
#define fst first
#define snd second

const int maxn = 50 + 5;
int R[ maxn ];
vector<int> Q[ maxn ];
int n, p;

void input(){
    cin >> n >> p;
    FOR( i, n ){
        si( R[ i ] );
    }
    FOR( i, n ){
        Q[ i ].clear();
        FOR( j, p ){
            int a; si( a );
            Q[ i ].pb( a );
        }
        sort( Q[ i ].begin(), Q[ i ].end() );
    }
}

int solve(){
    int cnt = 0;
    while( true ){
        bool going = true;
        FOR( i, n ){
            if( Q[ i ].empty() ) going = false;
        }
        if( going == false ) break;
        int big = 0;
        int posi;
        FOR( i, n ){
            if( big < ( ( Q[ i ].back() * 10 - 1 ) / ( R[ i ] * 11 ) ) + 1 ){
                big = ( ( Q[ i ].back() * 10 - 1 ) / ( R[ i ] * 11 ) ) + 1;
                posi = i;
            }
        }

        bool use = true;
        FOR( i, n ){
            int x = Q[ i ].back();
            if( x < ( big * R[ i ] * 9 + 1 ) / 10 ) use = false;
            if( x > ( big * R[ i ] * 11 ) / 10 ) use = false;
        }
        if( use ){
            cnt++;
            FOR( i, n ) Q[ i ].pop_back();
        }
        else Q[ posi ].pop_back();
    }
    return cnt;
}

int main(){
    int T; si( T );
    FOR1( tt, T ){
        input();
        int ans = solve();
        printf("Case #%d: %d\n", tt, ans );
    }
    return 0;
}
