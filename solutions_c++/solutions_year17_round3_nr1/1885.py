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

inline ll radius ( ll r ) 
    { return 2 * r; }
inline ll area ( ll r )
    { return r * r; }
    
struct Pancake {
    int R, H;
    ll radiusArea, heightArea;
};

#define PI 3.14159265358979323846  /* pi */

void solve ()
{
    ll N, K;
    cin >> N >> K;
    
    vector<Pancake> P(N);
    FOR(i, 0, N) { cin >> P[ i ].R >> P[ i ].H; }
    FOR(i, 0, N) { P[ i ].radiusArea = area( P[ i ].R ); }
    FOR(i, 0, N) { P[ i ].heightArea = radius( P[ i ].R ) * P[ i ].H; }
    
    sort( P.begin(), P.end(), []( const Pancake & a, const Pancake & b ) {
        return tie(a.heightArea, a.radiusArea) > tie(b.heightArea, b.radiusArea);
    } );
    vector<Pancake> KK( P.begin(), P.begin() + K );
    
    ll maxidK = 0, mmaxR = KK[ 0 ].radiusArea;
    F(K) 
        if ( KK[ i ].radiusArea >= mmaxR ) 
            mmaxR = KK[ maxidK = i ].radiusArea;
    
    ll maxid = K - 1; 
    ll mmax = P[ K - 1 ].heightArea + mmaxR;
    
    FOR(i, K, N) if ( P[ i ].radiusArea > mmaxR && P[ i ].heightArea + P[ i ].radiusArea > mmax ) {
        maxid = i;
        mmax = P[ i ].heightArea + P[ i ].radiusArea;
    }
    
    if ( maxid >= K ) { KK[ K - 1 ] = P[ maxid ]; }
    
    F(K) 
        if ( KK[ i ].radiusArea >= mmaxR ) 
            mmaxR = KK[ maxidK = i ].radiusArea;
    
    ll sum = KK[ maxidK ].radiusArea;
    FOR(i, 0, K) { sum += KK[ i ].heightArea; }
    
    cout << fixed << setprecision(9) << (PI * sum) << endl;
}

int main ()
{
    ll T; cin >> T;
    FOR(t,0,T) {
        cout << "Case #" << (t + 1) << ": ";
        solve();
    }
    return 0;
}