#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define mmax(a,b,c) max(max(a,b),c)
#define mmin(a,b,c) min(min(a,b),c)
#define sqr(n) ( ( n ) * ( n ) )
#define pb push_back
#define mp make_pair
#define size(x) ((int)(x).size())

const int N = 1 * 100500;
const int mod = 1e9 + 7;
const int inf = 1e9;

bool used[N];
vector < int > dig;

void check( int pos ){
    if ( !pos ) return;
    if ( dig[ pos ] < dig[ pos - 1 ] ){
        dig[ pos ] = 9;
        used[ pos ] = true;
        if ( !used[ pos - 1 ] ){
            dig[ pos - 1 ]--;
            check( pos - 1 );
        }
    }
}

int main()
{
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
    ofstream cout( "output.txt" );
    int t;
    int x = 1;
    cin >> t;
    while ( t ){
        dig.clear();
        for (int i = 0; i < 20; i++) used[i] = 0;
        ll n;
        cin >> n;
        while( n ){
            dig.pb( n % 10 );
            n /= 10;
        }
        reverse( dig.begin(), dig.end() );
        for (int i = 1; i < size( dig ); i++){
            check( i );
        }
        cout << "Case #" << x << ": ";
        if ( dig[0] != 0 ) cout << dig[0];
        for (int i = 1; i < size( dig ); i++){
            cout << dig[i];
        }
        cout << '\n';
        --t;
        ++x;
    }
    return 0;
}
