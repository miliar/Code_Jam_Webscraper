#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
    int t,n,hope;
    string str;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        hope = 0;
        cin >> str;
        cin >> n;

        for( int p = 0; p < str.length()-n+1; p++ ) {
            if( str[p] == '-' ) {
                for (int q = p; q < p+n; q++) {
                    if( str[q] == '+' ) {
                        str[q] = '-';
                    } else {
                        str[q] = '+';
                    }
                }
                hope++;
            }
        }

        cout << "Case #" << i << ": ";
        for(int p = 0; p < str.length(); p++) {
            if( str[p] == '-' ) {
                hope = -1;
            }
        }
        if( hope == -1 ) {
            cout << "IMPOSSIBLE";
        } else {
            cout << hope;
        }
        cout << endl;
    }
}