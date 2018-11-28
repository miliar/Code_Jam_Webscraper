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
    FOR(t, 0, T) {
        ll D, N;
        cin >> D >> N;
        vector<pair<ll, ll>> H( N );
        
        F(N) cin >> H[ i ].first >> H[ i ].second;
        double maxTime = 0;
        F(N) {
            double time = (double)( D - H[ i ].first ) / (double)H[ i ].second;
            maxTime = max( maxTime, time );
        }

        double result = D / maxTime;
        cout << "Case #" << (t + 1) << ": " << setprecision( 8 ) << fixed << result << endl;
    }
    
    return 0;
}