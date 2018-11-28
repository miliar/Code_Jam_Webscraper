#include <iostream>
#include <string>
using namespace std;

int main () {
    int t, i, j, l, num, flips;
    cin >> t;
    bool **a = new bool*[t];
    int *size = new int[t];
    int *k = new int[t];
    bool *temp;
    for ( i = 0; i < t; i++ ) {
        string s;
        cin >> s;
        size[i] = s.size();
        a[i] = new bool[size[i]];
        for ( j = 0; j < s.size(); j++ ) {
            if (s[j] == '+') {
                a[i][j] = 1; }
            else{
                a[i][j] = 0;}
        }
        cin >> k[i];
    }

    for ( i = 0; i < t; i++ ) {
        temp = a[i];
        num = size[i];
        flips = 0;
        for ( j = 0; j < size[i]; j++ ) {
            if ( a[i][j] == 0 ){
                if ( size[i] - j >= k[i] ){
                    flips++;
                    for ( l = j; l - j < k[i]; l++ ){
                        if ( a[i][l] )
                            a[i][l] = 0;
                        else a[i][l] = 1;
                    }
                }
                else {
                    flips = -1;
                    continue;
                }
            }
        }
        if ( flips == -1 ){
            cout << "Case #" << i+1 << ": IMPOSSIBLE"<< endl;
        }
        else
            cout << "Case #" << i+1 << ": "<< flips << endl;
    }
}
