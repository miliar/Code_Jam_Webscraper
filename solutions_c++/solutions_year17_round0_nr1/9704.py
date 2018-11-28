#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = ~(1<<31); // 2147483647

const double EPS = 1e-6;
const double pi = acos(-1);
typedef unsigned long long ull;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int main()
{
    int T ; cin >> T ; 
    for ( int it = 1 ; it<= T ; it++ )
    {   
        string s ; 
        cin >> s ; 
        int k ; cin >> k ; 
        int ans = 0 ; 
        bool impossible = false ; 
        int l = s.size() ; 

        int a[ l ] ; 
        for ( int i = 0 ; i < l ; i++ ) a[ i ] = ( s[i] == '+' ) ; 

        for ( int i = 0 ; i < l-k+1; i++ )
        {
            if ( a[ i ] == 0 )
            {
                for ( int j = i ; j < i+k ; j++ ) a[ j ] = 1 - a[ j ] ;
                ans++;
            }
        }

        for ( int i = 0; i < l ; i++ ) 
        {
            if ( a[ i ] == 0 )
            {
                impossible = true ; 
                break ; 
            }
        }

        if ( impossible ) printf("Case #%d: IMPOSSIBLE\n",it);
        else printf("Case #%d: %d\n",it,ans);
    }
    return 0;
}