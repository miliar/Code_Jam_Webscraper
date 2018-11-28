#include <bits/stdc++.h>
#define si(n) scanf( "%d", &n )
#define sl(n) scanf( "%lld", &n )
#define sf(n) scanf( "%lf", & n )
#define sc(c) scanf( "%c", &c )
#define pb(n) push_back(n)
#define mp(a,b) make_pair( a, b )
#define f(i,n) for( int i = 0; i < n; i++ )
#define fv(v) for( int i = 0; i < v.size(); i++ )
#define sv(v) sort( v.begin(), v.end() )
#define sa(a,n) sort( a, a + n )
#define pf(n) push_front( n )
# define m_pi 3.14159265358979323846
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<double> vd;
typedef vector<vector<double> > vvd;
typedef vector<pair<int,int> > vpi;
typedef pair<long long, long long> pll;
typedef vector<long long> vl;
typedef vector<pll> vpl;
ll gcd( ll a, ll b ){ return ( b == 0 )? a: gcd( b, a % b ); }
ll modpow( ll a, ll b, ll m ){  ll ans = 1; while( b ){ if( a & 1 ) ans = ( ans * a ) % m;  a = ( a * a ) % m;  }   return ans; }

void solveTC( int tc ){
    int n, k;
    cin >> n >> k;
    vector<pair<double, double> > cake( n );

    for( int i = 0; i < n; i++ ){
        double r, h;
        cin >> r >> h;
        cake[i] = make_pair( r, h );
    }

    sort( cake.begin(), cake.end() );
    double ans = 0;

    for( int i = n - 1; i >= k - 1; i-- ){
        double r = cake[i].first, h = cake[i].second;
        double temp = m_pi * r * r + 2 * m_pi * r * h;
        vector<double> area;

        for( int j = i - 1; j >= 0; j-- ){
            area.push_back( 2 * m_pi * cake[j].first * cake[j].second );
        }

        sort( area.begin(), area.end() );
        reverse( area.begin(), area.end() );
        for( int j = 0; j < k - 1; j++ )    temp += area[j];
        ans = max( ans, temp );
    }

    printf( "%.6lf", ans );

}

int main()
{
    freopen( "A.in", "r", stdin );
    freopen( "A.out", "w", stdout );

    int T;
    si(T);

    f(g,T){
        cout << "Case #" << g + 1 << ": ";
        solveTC( g + 1 );
        cout << endl;
    }

    return 0;
}
