#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int main() {
    int t;
    freopen( "in.txt", "r", stdin );
//    freopen( "out.txt", "w", stdout );
    while( cin >> t ) {
        int cases = 0;
        while( t-- ) {
            int k;
            string str;
            cin >> str;
            cin >> k;
            int len = (int)str.length();
            int ans = 0;
            for( int i = 0; i <= len - k; i++ ) {
                if( str[i] == '-' ) {
                    for( int j = i; j <= i + k - 1; j++ ) {
                        if( str[j] == '-' ) str[j] = '+';
                        else str[j] = '-';
                        
                    }
                    ans++;
                }
            }
            
            int flag = 0;
            for( int i = len - k + 1; i < len; i++ ) {
                if( str[i] == '-' ) {
                    flag = 1;
                    break;
                }
            }
            
            if( flag ) cout << "Case #" << ++cases << ": " << "IMPOSSIBLE" << endl;
            else cout << "Case #" << ++cases << ": " << ans << endl;
            
        }
    }
    return 0;
}
