#include <iostream>
#include <bitset>
#include <string>

using namespace std;

typedef unsigned int uint;

int get_blank(string s, int start) {
    uint i = start;
    
    for (; i < s.size() && s[i] != '-'; i++);

    return i;
}


int main() {
    int t;
    cin >> t;

    for (int x = 0; x < t; ++x) {
        int r, c;
        cin >> r >> c;

        string cakes[r];
        bool mark[r];

        for (int i = 0; i < r; i++) {
            cin >> cakes[i];
        }

        for (int i =0; i<r; i++) {

            int j = 0;

            while (cakes[i][j] == '?') {
                j++;
            }

            int start = j;

            if (j != c) {

                for (int k = 0; k < start; k++) {
                    cakes[i][k] = cakes[i][start];
                }
            } else {
                mark[i] = true;
                continue;
            }

            mark[i] = false;

            char ch = cakes[i][start];

            for (j = start + 1; j < c; j++) {

                if (cakes[i][j] == '?') {
                    cakes[i][j] = ch;
                } else {
                    ch = cakes[i][j];
                }
            }
        }

        int i = 0;

        while (mark[i] == true) {
            i++;
        }

        for (int k = i - 1; k >= 0; k--) {
            cakes[k] = cakes[k+1];
        }

        for (i += 1; i < r; i++) {

            if (mark[i] == true) {

                cakes[i] = cakes[i-1];
            }
        }
        
        cout << "Case #" << x + 1 << ":\n";
        for (int k = 0; k < r; k++) {
            cout << cakes[k] << '\n';
        }
        // cout << '\n';
    }
}
