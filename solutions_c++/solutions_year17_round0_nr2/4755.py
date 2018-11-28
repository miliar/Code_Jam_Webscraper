#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define size(n) ( int( n.size() ) )
#define sqr(n) ( (n) * (n) )

using namespace std;

int d[10], len, ans;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases, n, j, i, t;
    cin >> cases;
    for ( t = 1; t <= cases; t++ ){
        cin >> n;
        ans = 0;
        for ( i = 1; i <= n; i++ ){
            int tmp = i;
            len = 0;
            while( tmp != 0 ){
                d[++len] = tmp % 10;
                tmp /= 10;
            }
            reverse( d + 1, d + len + 1 );
            for ( j = 2; j <= len; j++ ){
                if ( d[j] < d[j-1] ){
                    break;
                }
            }
            if ( j == len + 1 ){
                ans = max( ans, i );
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
