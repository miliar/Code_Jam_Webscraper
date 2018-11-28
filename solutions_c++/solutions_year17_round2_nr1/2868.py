#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("salida.out","w",stdout);
    int tc; cin >> tc;

    for( int caso = 1 ; caso <= tc; ++caso ){
        double ki, si, d;
        int n; cin >> d >> n;
        double tmax = 0;
        for( int i = 0 ; i < n ; ++i ){
            cin >> ki >> si;
            tmax = max( tmax, ( d-ki )/si );
        }
        cout << "Case #"<<caso<<": ";
        cout << fixed << setprecision(7);
        cout << d/tmax << '\n';
    }

}
