//In the name of Allah
#include <bits/stdc++.h>
using namespace std; 

typedef long double ld; 

struct Problem { 
    int a[200]; 
    void solve() { 
        int n, p; 
        cin >> n >> p; 
        int ans = 0;
        int en = 0;
        for( int i = 0 ; i < n ; i++ ) { 
            int x; cin >> x; 
            a[en++] = x % p;
        }
        int rem = 0; 
        for( int i = 0; i < en ; i++ ) { 
            for( int j = i+1 ; j < en ; j++ ) 
                if( ( a[j] + p - rem ) % p == 0 ) 
                    swap( a[j] , a[i] ); 
            if( rem == 0 ) ans++;
            rem = ( p - ( a[i] + p - rem ) % p ) % p; 
        }
        cout << ans << endl;
    }
};

int main() { 
    cout << fixed << setprecision(15); 

    int t; cin >> t; 
    for( int i = 1 ; i <= t ; i++ ) { 
        cout << "Case #" << i << ": "; 
        Problem x; 
        x.solve(); 
    }
}
