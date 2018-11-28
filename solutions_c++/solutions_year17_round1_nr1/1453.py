#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        int R, C; cin >> R >> C;
        char cake[25][25];
        for (int r = 0; r < R; r++) {
            string s;
            cin >> s;
            for (int c = 0; c < C; c++) {
                cake[r][c] = s[c];
            }
        }
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (cake[r][c] != '?') continue;
                else {
                    if (c > 0) {
                        for (int q = c-1; q >=0; q--) {
                            if (cake[r][q] != '?') {
                                cake[r][c] = cake[r][q];
                                break;
                            }
                        }
                    }
                }
            }
        }
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (cake[r][c] != '?') continue;
                else {
                    if (c < C-1) {
                        for (int q = c+1; q < C; q++) {
                            if (cake[r][q] != '?') {
                                cake[r][c] = cake[r][q];
                                break;
                            }
                        }
                    }
                }
            }
        }
        for (int c = 0; c < C; c++) {
            for (int r = 0; r < R; r++) {
                if (cake[r][c] != '?') continue;
                else {
                    if (r > 0) {
                        for (int q = r-1; q >= 0; q--) {
                            if (cake[q][c] != '?') {
                                cake[r][c] = cake[q][c];
                                break;
                            }
                        }
                    }
                }
            }
        }
        for (int c = 0; c < C; c++) {
            for (int r = 0; r < R; r++) {
                if (cake[r][c] != '?') continue;
                else {
                    if (r < R-1) {
                        for (int q = r+1; q < R; q++) {
                            if (cake[q][c] != '?') {
                                cake[r][c] = cake[q][c];
                                break;
                            }
                        }
                    }
                }
            }
        }
        cout << "Case #" << (t+1) << ":" << endl;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                cout << cake[r][c];
            }
            cout << endl;
        }
    }
    return 0;
}

