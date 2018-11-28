#include <bits/stdc++.h>

using namespace::std;

template<unsigned N, unsigned M>
void assign(char (&Cake)[M][N], int R, int C, int caseno) {
    int r, c;

    cout << "Case #" << caseno << ":" << endl;
    // for (r = 0; r < R; r++) {
    //     for (c = 0; c < C; c++)
    //         cout << Cake[r][c];
    //     cout << endl;
    // }
    // return;
            

    //case 1
    for(c = 0; c < C; c++) {
        for(r = 1; r < R; r++) {
            if (Cake[r][c] == '?' && Cake[r-1][c] != '?')
                Cake[r][c] = Cake[r-1][c];
        }
    }

    //case 2
    for(c = 0; c < C; c++) {
        for (r = R-2; r>= 0; r--) {
            if (Cake[r][c] == '?' && Cake[r+1][c] != '?')
                Cake[r][c] = Cake[r+1][c];
        }
    }

    //case 3
    for(c = 1; c < C; c++) {
        if (Cake[0][c] == '?' && Cake[0][c-1] != '?') {
            for (r = 0; r < R; r++) 
                Cake[r][c] = Cake[r][c-1];
        }
    }

    //case 4
    for(c = C-2; c>= 0; c--) {
        if (Cake[0][c] == '?' && Cake[0][c+1] != '?') {
            for (r = 0; r < R; r++)
                Cake[r][c] = Cake[r][c+1];
        }
    }

    //print results

    for(r = 0; r < R; r++) {
        for (c = 0; c < C; c++) {
            cout << Cake[r][c];
        }
        cout << endl;
    }
}

int main() {
    int T;
    int R, C;
    int caseno = 1;

    char Cake[100][100] = {0};

    freopen("alphabet_large.in", "r", stdin);
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> R >> C;
        for(int r = 0; r < R; r++) {
            string line;
            cin >> line;
            for(int c = 0; c < C; c++) {
                Cake[r][c] = line[c];
            }
        }
        assign(Cake, R, C, t);
    }
    
    return 0;
}