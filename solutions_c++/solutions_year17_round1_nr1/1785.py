#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int n,m;
        cin >> n >> m;
        char cake[n][m];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                cin >> cake[i][j];
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(cake[i][j] != '?') {
                    for(int k = j-1; k >= 0; k--) {
                        if(cake[i][k] != '?') break;
                        cake[i][k] = cake[i][j];
                        // for(int z = i-1; z >= 0; z++) {
                        //     if(cake[z][k] != '?') break;
                        //     cake[z][k] = cake[i][k];
                        // }
                        // for(int z = i+1; z >= n; z++) {
                        //     if(cake[z][k] != '?') break;
                        //     cake[z][k] = cake[i][k];
                        // }
                    }
                    for(int k = j+1; k < m; k++) {
                        if(cake[i][k] != '?') break;
                        cake[i][k] = cake[i][j];
                        // for(int z = i-1; z >= 0; z++) {
                        //     if(cake[z][k] != '?') break;
                        //     cake[z][k] = cake[i][k];
                        // }
                        // for(int z = i+1; z >= n; z++) {
                        //     if(cake[z][k] != '?') break;
                        //     cake[z][k] = cake[i][k];
                        // }
                    }
                }
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(cake[i][j] != '?') {
                    for(int k = i-1; k >= 0; k--) {
                        if(cake[k][j] != '?') break;
                        cake[k][j] = cake[i][j];
                    }
                    for(int k = i+1; k < n; k++) {
                        if(cake[k][j] != '?') break;
                        cake[k][j] = cake[i][j];
                    }
                }
            }
        }

        cout << "Case #" << t << ":" << endl;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                cout << cake[i][j];
            }
            cout << endl;
        }
    }
}