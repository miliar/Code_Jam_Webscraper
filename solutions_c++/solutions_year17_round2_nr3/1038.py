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
    int n, q;
    double dp[105];
    double dist[105], cap[105], speed[105];
    cin >> n >> q;

    for( int i = 1; i <= n; i++ ){
        cin >> cap[i] >> speed[i];
    }

    for( int i = 1; i <= n; i++ ){
        for( int j = 1; j <= n; j++ ){
            double t;
            cin >> t;
            if( j == i + 1 )   dist[i] = t;
        }
    }

    dist[n] = 0;
    double pre_sum[105];
    pre_sum[1] = 0;

    for( int i = 2; i <= n; i++ ){
        pre_sum[i] = pre_sum[i-1] + dist[i-1];
    }

    dp[n] = 0;

    for( int i = n-1; i >= 0; i-- ){
        dp[i] = DBL_MAX;

        for( int j = i + 1; j <= n; j++ ){
            double temp = pre_sum[j] - pre_sum[i];
            if( cap[i] < temp ) continue;
            double time = temp / speed[i];
            dp[i] = min( dp[i], time + dp[j] );
        }
    }

    for( int i = 1; i <= q; i++ ){
        int x, y;
        cin >> x >> y;
        printf( "%.8lf", dp[1] );
    }
}

int main()
{
    freopen( "C.in", "r", stdin );
    freopen( "C.out", "w", stdout );

    int T;
    si(T);

    f(g,T){
        cout << "Case #" << g + 1 << ": ";
        solveTC( g + 1 );
        cout << endl;
    }

    return 0;
}
