#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, cc = 0; cin >> t;
    while (t--) {
        int r, c; cin >> r >> c;
        char gr[r][c];
        set<char> ch;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> gr[i][j];
            }
        }
        for (int i = 0; i < r-1; i++) {
            for (int j = 0; j < c; j++) {
                if (gr[i+1][j] == '?') gr[i+1][j] = gr[i][j]; 
            }
        }
        for (int i = 1; i < r; i++) {
            for (int j = 0; j < c; j++) {
                //cerr << "b " << gr[i-1][j] << " -> " << gr[i][j] << endl;
                if (gr[i-1][j] == '?') gr[i-1][j] = gr[i][j];
            }
        }
        for (int i = r-2; i >= 0; i--) {
            for (int j = 0; j < c; j++) {
                if (gr[i+1][j] == '?') gr[i+1][j] = gr[i][j]; 
            }
        }
        for (int i = r-1; i > 0; i--) {
            for (int j = 0; j < c; j++) {
                //cerr << "b " << gr[i-1][j] << " -> " << gr[i][j] << endl;
                if (gr[i-1][j] == '?') gr[i-1][j] = gr[i][j];
            }
        }
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c-1; j++) {
                if (gr[i][j+1] == '?') gr[i][j+1] = gr[i][j]; 
            }
        }
        for (int i = 0; i < r; i++) {
            for (int j = 1; j < c; j++) {
                if (gr[i][j-1] == '?') gr[i][j-1] = gr[i][j]; 
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = c-2; j >= 0; j--) {
                if (gr[i][j+1] == '?') gr[i][j+1] = gr[i][j]; 
            }
        }
        
        for (int i = 0; i < r; i++) {
            for (int j = c-1; j > 0; j--) {
                if (gr[i][j-1] == '?') gr[i][j-1] = gr[i][j]; 
            }
        }
       cout << "Case #" << ++cc << ":" << endl;
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cout << gr[i][j];
            }
            cout << endl;
        }
    }
}
