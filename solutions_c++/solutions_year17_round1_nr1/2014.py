#include <iostream>
#include <string>

using namespace std;



int main() {
    int t, r, c;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string cake[25];
        bool nblank[25] = {};
        bool fnbb = false;
        int fnb;
        cin >> r >> c;
        for (int j = 0; j < r; ++j) {
            cin >> cake[j];
            for (int k = 0; k < c; ++k) {
                if (cake[j][k] != '?') {
                    nblank[j] = 1;
                    if (!fnbb) {
                        fnbb = true;
                        fnb = j;
                        //cout << "FNB: " << j << endl;
                    }
                    break;
                }
            }
        }
        for (int j = fnb; j < r; ++j) {
            if (nblank[j]) {
                char cur;
                bool fc = false;
                for (int k = 0; k < c && !fc; ++k) {
                    if (cake[j][k] != '?') {
                        fc = true;
                        cur = cake[j][k];
                    }
                }
                for (int k = 0; k < c; ++k) {
                    if (cake[j][k] == '?' || cake[j][k] == cur) {
                        cake[j][k] = cur;
                    }
                    else {
                        cur = cake[j][k];
                    }
                }
                if (j == fnb) {
                    int m = j-1;
                    while (m >= 0) {
                        for (int k = 0; k < c; ++k) {
                            cake[m][k] = cake[j][k];
                        }
                        --m;
                    }
                }
            }
            else {
                for (int k = 0; k < c; ++k) {
                    cake[j][k] = cake[j-1][k];
                }
            }
        }
        cout << "Case #" << i << ":" << endl;
        for (int j = 0; j < r; ++j) {
            cout << cake[j] << endl;
        }    
    }
    

    return 0;
}
