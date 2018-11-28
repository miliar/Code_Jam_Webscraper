//In the name of Allah
#include <bits/stdc++.h>
using namespace std; 

const int maxN = 1000 + 10;
int a[maxN];

int solve() { 
    string s; int k; 
    cin >> s >> k; 
    int n = s.size();
    for( int i = 0 ; i < n ; i++ ) 
        a[i] = (s[i] == '+'); 
    int ans = 0;
    for( int i = 0 ; i + k <= n ; i++ ) 
        if( a[i] == 0 ) { 
            for( int j = 0 ; j < k ; j++ ) 
                a[i+j] ^= 1; 
            ans++; 
        }
    for( int i = n - k + 1 ; i < n ; i++ ) 
        if( !a[i] ) return -1; 
    return ans;
}

int main() { 
    int t; 
    cin >> t;
    for( int i = 1 ; i <= t ; i++ ) { 
        int ret = solve(); 
        if( ret != -1 ) 
            cout << "Case #" << i << ": " << ret << endl;
        else
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;

    }

}
