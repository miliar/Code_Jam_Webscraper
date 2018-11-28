#include <iostream>
#include <algorithm>
#include <string>

#define N 26

using namespace std;

char cake[N][N];

void zoom(int i, int j, int ir, int jc, int r, int c, char letter) {

    if (i > r-1 or j > c-1 or i < 0 or j < 0 or cake[i][j] != '?') {
        return;
    }

    cake[i][j] = letter;
    zoom(i+ir,j+jc,ir,jc,r,c,letter);
}

int solve() {

    int r, c;
    cin >> r >> c;
    char cc;
    string s;
    for (int i = 0; i < r; i++) {
        cin >> s;
        for (int j = 0; j < s.length(); j++) cake[i][j] = s.at(j);
    }

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (cake[i][j] == '?') continue;
            if (i < r) {                
                zoom(i+1,j,1,0,r,c,cake[i][j]);
                if (i > 0)
                    zoom(i-1,j,-1,0,r,c,cake[i][j]);
            } 
        }        
    }

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (cake[i][j] == '?') continue;
            if (j < c) {                
                zoom(i,j+1,0,1,r,c,cake[i][j]);
                if (j > 0)
                    zoom(i,j-1,0,-1,r,c,cake[i][j]);
            } 
        }        
    }

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cout << cake[i][j];
        }
        cout << endl;
    }

    return 0;
}

int main() {

    int t, p = 1;
    for (cin >> t; t--;) {
        cout << "Case #" << p++ << ": " << endl;
        solve();
    }

    return 0;
}