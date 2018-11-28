#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef double ld;

typedef pair<ll, ll> ii;
typedef vector<ll> vi;
typedef vector<ii> vii;

#define PB push_back

#define FOR(prom,a,b) for ( ll prom = (a); prom < (ll)(b); ++prom )
#define F(a) FOR(i,0,a)
#define FF(a) FOR(j,0,a)

#define EPS (1e-10)

#define EQ(a,b) (fabs(a-b) <= fabs(a+b) * EPS)

int main ()
{
    ll T; cin >> T;
    for ( ll t = 0; t < T; ++t ) {
        ll R, C; cin >> R >> C;
        vector<vector<char>> CAKE( R, vector<char>( C, '?' ) );
        vector<bool> EMPTYLINE( R, true );
        
        for (ll r = 0; r < R; ++r) {
            for (ll c = 0; c < C; ++c) {
                cin >> CAKE[ r ][ c ];
                if ( CAKE[ r ][ c ] != '?' )
                    EMPTYLINE[ r ] = false;
            }
        }
        
        for (ll r = 0; r < R; ++r) {
            if ( EMPTYLINE[ r ] )
                continue;
            bool start = false;
            for (ll c = 0; c < C; ++c) {
                if ( CAKE[ r ][ c ] != '?' )
                    start = true;
                if ( CAKE[ r ][ c ] == '?' && start )
                    CAKE[ r ][ c ] = CAKE[ r ][ c - 1 ];
            }
            start = false;
            for (ll c = C - 1; c >= 0; --c) {
                if ( CAKE[ r ][ c ] != '?' )
                    start = true;
                if ( CAKE[ r ][ c ] == '?' && start )
                    CAKE[ r ][ c ] = CAKE[ r ][ c + 1 ];
            }
        }
        
        bool start = false;
        for (ll r = 0; r < R; ++r) {
            if ( !EMPTYLINE[ r ] )
                start = true;
            if ( EMPTYLINE[ r ] && start )
                CAKE[ r ] = CAKE[ r - 1 ];
        }
        
        start = false;
        for (ll r = R - 1; r >= 0; --r) {
            if ( !EMPTYLINE[ r ] )
                start = true;
            if ( EMPTYLINE[ r ] && start )
                CAKE[ r ] = CAKE[ r + 1 ];
        }
        
        cout << "Case #" << (t + 1) << ":" << endl;
        for (ll r = 0; r < R; ++r) {
            for (ll c = 0; c < C; ++c) {
                cout << CAKE[ r ][ c ];
            }
            cout << endl;
        }
        
    }
    return 0;
}