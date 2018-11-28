#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <iterator>
using namespace std;

string str;

int check( int start, int end ) {
    
    for( int i = start; i < end; i++ ) {
        if( str[i] > str[i+1] ) return 0;
    }
    return 1;
}

int main() {
    int t;
    while( cin >> t ) {
        int cases = 0;
        while( t-- ) {
            
            cin >> str;
            int len = (int)str.length();
            int pos = len-1;
            while( 1 ) {
                
                if( check( 0, pos ) ) break;
                
                int i;
                for( i = 0; i < pos; i++ ) {
                    if( str[i] > str[i+1] ) {
                        str[i]--;
                        for( int j = i+1; j <= pos; j++ ) {
                            str[j] = '9';
                        }
                        break;
                    }
                }
                pos = i;
            }
            cout << "Case #" << ++cases << ": ";
            for( int i = 0; i < len; i++ ) {
                if( i == 0 && str[i] == '0' ) continue;
                cout << str[i];
            }
            cout << endl;
        }
    }
    return 0;
}