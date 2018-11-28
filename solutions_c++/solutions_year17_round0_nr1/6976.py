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
    string str;
    int k;
    cin >> str >> k;
    int n = str.size();
    int cnt = 0, i = 0;

    for( i = 0; i <= n - k; i++ ){
        if( str[i] == '-' ){
            cnt++;

            for( int j = i; j < i + k; j++ ){
                if( str[j] == '-' ) str[j] = '+';
                else    str[j] = '-';
            }
        }
    }

    for( ; i < n; i++ ){
        if( str[i] == '-' ){
            cout << "IMPOSSIBLE";
            return;
        }
    }
    cout << cnt;
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
