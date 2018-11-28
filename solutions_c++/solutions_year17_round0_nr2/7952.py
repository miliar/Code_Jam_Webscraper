#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
    int t,m;
    int64_t n;
    int arr[19];
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        m = -1;
        while ( n != 0) {
            arr[++m] = n % 10;
            n = n / 10;
        }
        for( int p=m; p > 0; p-- ) {
            if( arr[p] > arr[p-1] ) {
                arr[p]--;
                for( int q=p-1; q >= 0; q-- ) {
                    arr[q] = 9;
                }
                for( int q=p; q < m; q++ )
                {
                    if( arr[q] < arr[q+1]  ) {
                            arr[q+1]--;
                            arr[q] = 9;
                    }
                }
            }
        }
        cout << "Case #" << i << ": ";
        while( m >= 0) {
            if( arr[m] == 0 ) {
                m--;
            } else {
                break;
            }
        }
        for( ; m >= 0; m--) {
            cout << arr[m];
        }
        cout << endl;
    }
}