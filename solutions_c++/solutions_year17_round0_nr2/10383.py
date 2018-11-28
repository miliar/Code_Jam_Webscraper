#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

set < ll > res;

bool isIncreasing( ll number )
{
    while( number )
    {
        if( number/10LL != 0 )
        {
            if( number%10 < (number/10LL)%10 )
                return false;
        }
        number /= 10LL;
    }
    return true;
}

void precalc()
{
    ll lim = 1000;
    for( ll i = 1 ; i <= lim ; i++ )
    {
        if( isIncreasing( i ) )
            res.insert( i );
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    precalc();
    int cases;
    ll number,ans;
    cin >> cases;
    for( int i = 0 ; i < cases ; i++ )
    {
        cin >> number;
        cout << "Case #" << i+1 <<": ";
        set < ll >::iterator it;
        ans = -1LL;
        for(it = res.begin() ; it != res.end() ; ++it )
        {
            if( *it <= number )
                ans = *it;
            else
                break;
        }
        cout << ans << endl;
    }
    return 0;
}
