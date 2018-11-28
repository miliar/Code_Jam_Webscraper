#include <bits/stdc++.h>
using namespace std;

int main () {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; cin >> t;
    for (int cas = 1; cas <= t; cas++) {

        long long n,k;
        cin >> n >> k;

        map< long long , long long > c;
        set< long long > s;
        c[n] = 1; s.insert(n);

        while (true) {

            long long x = *s.rbegin();
            s.erase(x);

            long long y = (x-1)/2;
            long long z = ( (x-1)+1 )/2;

            s.insert( y );
            c[ y ] += c[x];

            s.insert( z );
            c[ z ] += c[x];

            if ( k > c[x] ) {
                k -= c[x];
            } else {
                cout << "Case #" << cas << ": " << z << " " << y << endl;
                break;
            }
        }

    }
}
