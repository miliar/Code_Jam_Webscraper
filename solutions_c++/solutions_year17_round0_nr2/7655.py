#include<bits/stdc++.h>
using namespace std;

string str;

int tidy( int initial, int final ) {
    
    for( int i = initial; i < final; i++ ) {
        if( str[i] > str[i+1] ) return 0;
    }
    return 1;
}

int main() {
    int t;
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
    while( cin >> t ) {
        int tests = 0;
        while( t-- ) {            
            cin >> str;
            int len = (int)str.length();
            int position = len-1;
            while( 1 ) {
                
                if( tidy( 0, position ) ) break;
                
                int i;
                for( i = 0; i < position; i++ ) {
                    if( str[i] > str[i+1] ) {
                        str[i]--;
                        for( int j = i+1; j <= position; j++ ) {
                            str[j] = '9';
                        }
                        break;
                    }
                }
                position = i;
            }
            cout << "Case #" << ++tests << ": ";
            for( int i = 0; i < len; i++ ) {
                if( i == 0 && str[i] == '0' ) continue;
                cout << str[i];
            }
            cout << endl;
        }
    }
    return 0;
}
