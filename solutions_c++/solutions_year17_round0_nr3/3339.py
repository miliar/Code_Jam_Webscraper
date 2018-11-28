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



int main()
{
//    freopen("input.txt", "r", stdin);
    ofstream cout( "out.txt" );
    int t, x = 1;
    cin >> t;
    while ( t ){
        ll n, k;
        cin >> n >> k;
        map < ll, ll > lens;
        lens[ n ] = 1;
        while( k > ( *prev( lens.end() ) ).second ){
            ll len = ( *prev( lens.end() ) ).first, cnt = ( *prev( lens.end() ) ).second;
//            cout << len << " " << cnt << '\n';
            if ( len & 1 ){
                lens[ len / 2 ] += 2 * cnt;
                lens.erase( len );
            }
            else{
                lens[ len / 2 ] += cnt;
                lens[ len / 2 - 1 ] += cnt;
                lens.erase( len );
            }
            k -= cnt;
        }
        ll len = ( *prev( lens.end() ) ).first;
//        cout << len << '\n';
        cout << "Case #" << x << ": ";
        if ( len & 1 ){
            cout << len / 2 << " " << len / 2;
        }
        else{
            cout << len / 2 << " " << max( len / 2 - 1, 0LL );
        }
        cout << '\n';
        --t; ++x;
    }
    return 0;
}
