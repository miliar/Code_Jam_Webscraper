#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef long long int ll;

ll log2 ( ll x )
{
    ll cnt = 0;
    while ( x > 1 ) {
        ++cnt; x >>= 1;
    }
    return cnt;
}

ll stall ( ll N, ll K )
{
    ll G = 1LL << log2(K);
    return ( N - ( K - 1 ) + ( G - 1 ) ) / G;
}

int main ( void )
{
    ll T; cin >> T; 
    string line; getline( cin, line );
    for ( ll t = 0; t < T; ++t ) {
        ll N, K; cin >> N >> K;
        ll result = stall( N, K );
        cout << "Case #" << (t + 1) << ": " << result / 2  << " " << ( result - 1 ) / 2 << endl;
    }
    
    return 0;
}