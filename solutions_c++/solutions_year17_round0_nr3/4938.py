
#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define size(n) ( int( n.size() ) )
#define sqr(n) ( (n) * (n) )

using namespace std;

typedef long long ll;

ll n, k, low, high, mid;
map < ll, ll > f;
map < ll, ll > :: iterator it;

void calc( ll x ){
    if ( x < mid ){
        return;
    }
    it = f.find(x);
    if ( it == f.end() ){
        ll res = 1;
        if ( x % 2 == 0 ){
            calc( (x>>1) );
            calc( (x>>1) - 1 );
            if ( (x>>1) >= mid ){
                res += f[(x>>1)];
            }
            if ( (x>>1) - 1 >= mid ){
                res += f[(x>>1)-1];
            }
        }
        else{
            calc(x>>1);
            res += f[(x>>1)] * 2;
        }
        f[x] = res;
    }
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases, t;
    scanf("%d",&cases);
    for ( t = 1; t <= cases; t++ ){
        cin >> n >> k;
        low = 0;
        high = n + 1;
        while( high - low > 1 ){
            mid = ( ( high + low ) >> 1 );
            f.clear();
            calc(n);
            if ( f[n] > k - 1 ){
                low = mid;
            }
            else{
                high = mid;
            }
        }
        cout << "Case #" << t << ": ";
        if ( low % 2 == 0 ){
            cout << ( low >> 1 ) << " " << ( low >> 1 ) - 1;
        }
        else{
            cout << ( low >> 1 ) << " " << ( low >> 1 );
        }
        cout << endl;
    }

    return 0;
}

