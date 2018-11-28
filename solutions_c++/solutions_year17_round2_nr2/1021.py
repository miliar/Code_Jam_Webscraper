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

char get_choice( int r, int b, int y, char ch ){
    if( ch != 'r' && r >= b && r >= y ) return 'r';
    if( ch != 'b' && b >= r && b >= y ) return 'b';
    if( ch != 'y' && y >= b && y >= r ) return 'y';

    if( ch != 'r' && ( r >= b || r >= y ) ) return 'r';
    if( ch != 'b' && ( b >= r || b >= y ) ) return 'b';
    if( ch != 'y' && ( y >= b || y >= r ) ) return 'y';
}

void solveTC( int tc ){
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    if( r + b < y || r + y < b || b + y < r ){
        cout << "IMPOSSIBLE";
        return;
    }

    string ans = "";
    char ch = 'x';

    while( r || b || y ){
        char choice = get_choice( r, b, y, ch );
        switch( choice ){
            case 'r':
                r--;
                ans += "R";
                ch = 'r';
                break;
            case 'b':
                b--;
                ans += "B";
                ch = 'b';
                break;
            case 'y':
                y--;
                ans += "Y";
                ch = 'y';
                break;
        }
    }

    if( ans.size() > 1 && ans[0] == ans[n-1] ){
        swap( ans[n-1], ans[n-2] );
    }
    cout << ans;
}

int main()
{
    freopen( "B.in", "r", stdin );
    freopen( "B.out", "w", stdout );

    int T;
    si(T);

    f(g,T){
        cout << "Case #" << g + 1 << ": ";
        solveTC( g + 1 );
        cout << endl;
    }

    return 0;
}
